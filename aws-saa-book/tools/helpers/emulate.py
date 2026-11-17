# /// script
# requires-python = ">=3.9"
# dependencies = ["moto[server]==5.2.3", "awscli==1.46.1"]
# ///
"""Optional emulation of one hands-on task against a local moto server (never a real account).

Run by `saa.py tasks emulate` as:  uv run --script aws-saa-book/tools/helpers/emulate.py
Input (standard input): {"task", "steps": [{"command", "capture": {"name", "query"} or null, "break_it"}],
"cleanup": [commands], "verify": command or null}
Output: {"task", "result": "pass|fail|not-supported", "steps": [{"phase", "command", "rc", "ok"}], "note"}

The server listens on 127.0.0.1 only. Credentials are dummies, the config and credential files are
/dev/null and AWS_ENDPOINT_URL points every call at the local server, so no call can reach AWS.
Commands run as argument lists (no shell). A break-it step must fail; every other command must
return 0. A pass means "moto accepts this sequence"; moto does not enforce every AWS rule, so a
pass is weaker than a run in a real account, and the printed label of a task does not change.
"""
import json
import os
import re
import shlex
import socket
import subprocess
import sys

DEAD_PROXY = "http://127.0.0.1:9"
NOT_SUPPORTED =re.compile(r"not\s+(yet\s+)?implemented|NotImplemented|\(501\)|has not been implemented|Invalid choice", re.I)


def free_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def main() -> int:
    task = json.load(sys.stdin)
    from moto.server import ThreadedMotoServer
    port = free_port()
    server = ThreadedMotoServer(ip_address="127.0.0.1", port=port, verbose=False)
    server.start()
    endpoint = f"http://127.0.0.1:{port}"
    env = dict(os.environ)
    for name in list(env):
        if name.startswith("AWS_"):
            del env[name]
    env.update({"AWS_ACCESS_KEY_ID": "testing", "AWS_SECRET_ACCESS_KEY": "testing", "AWS_SESSION_TOKEN": "testing",
                "AWS_DEFAULT_REGION": "us-east-1", "AWS_CONFIG_FILE": os.devnull, "AWS_SHARED_CREDENTIALS_FILE": os.devnull,
                "AWS_ENDPOINT_URL": endpoint, "AWS_EC2_METADATA_DISABLED": "true", "AWS_PAGER": "",
                # Guard: any request that does not go to the local server is sent to a dead local proxy and fails.
                "HTTP_PROXY": DEAD_PROXY, "HTTPS_PROXY": DEAD_PROXY, "http_proxy": DEAD_PROXY, "https_proxy": DEAD_PROXY,
                "NO_PROXY": "127.0.0.1,localhost", "no_proxy": "127.0.0.1,localhost"})
    variables = {}
    rows = []
    unsupported = []

    def run(phase, command, capture=None, break_it=False):
        words = shlex.split(command)[1:]
        words = [re.sub(r"\$([A-Z][A-Z0-9_]*)", lambda m: variables.get(m.group(1), m.group(0)), w) for w in words]
        if capture:
            words += ["--query", capture["query"], "--output", "text"]
        # --endpoint-url on the command line is honored by every awscli version; the environment variable alone is not.
        proc = subprocess.run([sys.executable, "-m", "awscli", "--endpoint-url", endpoint] + words, env=env,
                              capture_output=True, text=True, timeout=120)
        if proc.returncode != 0 and NOT_SUPPORTED.search(proc.stderr or ""):
            unsupported.append(command)
        ok = (proc.returncode != 0) if break_it else (proc.returncode == 0)
        if capture and proc.returncode == 0:
            variables[capture["name"]] = proc.stdout.strip()
        rows.append({"phase": phase, "command": command, "rc": proc.returncode, "ok": ok,
                     "stderr": (proc.stderr or "").strip()[-200:]})

    try:
        for step in task.get("steps") or []:
            run("step", step["command"], step.get("capture"), bool(step.get("break_it")))
        for command in task.get("cleanup") or []:
            run("cleanup", command)
        if task.get("verify"):
            run("verify", task["verify"])
    finally:
        server.stop()
    if unsupported:
        result, note = "not-supported", "moto does not implement: " + unsupported[0]
    elif all(r["ok"] for r in rows):
        result, note = "pass", "moto accepted every command; not run in a real account"
    else:
        first = next(r for r in rows if not r["ok"])
        result, note = "fail", f"{first['phase']} `{first['command'][:80]}` returned {first['rc']}"
    json.dump({"task": task.get("task"), "result": result, "steps": rows, "note": note}, sys.stdout, indent=1)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
