import sys, re
sys.path.insert(0, 'aws-saa-book/tools')
from saalib.lint import word_count
raw = open('aws-saa-book/24-backup/2-deep.md').read()
print('file', word_count(raw))
parts = re.split(r'(?m)^(#{2,3} .*)$', raw)
for i in range(1, len(parts), 2):
    head, body = parts[i], parts[i + 1]
    det = re.findall(r'(?s)<details>.*?</details>', body)
    detw = sum(word_count(d) for d in det)
    body_nodet = re.sub(r'(?s)<details>.*?</details>', ' ', body)
    prompts = re.findall(r'(?m)^\*\*(?:Stop and answer|Spot the bug)\.\*\*.*$', body_nodet)
    pw = sum(word_count(p) for p in prompts)
    print('%-80s total=%4d reveals=%4d prompts=%3d body=%4d' % (head[:80], word_count(body), detw, pw, word_count(body_nodet) - pw))
