"""adjudicate-19: drop rejected facts from brief.v0.json demand rows, add live replacements, recompute status."""
import json, os, sys

book = sys.argv[1]
brief_path = os.path.join(book, '_build/work/19-containers/brief.v0.json')
facts = {}
fdir = os.path.join(book, 'data/facts')
for fn in os.listdir(fdir):
    if fn.endswith('.jsonl'):
        for line in open(os.path.join(fdir, fn)):
            line = line.strip()
            if line:
                f = json.loads(line)
                facts[f['id']] = f
replace = {
    'ecr-max-layer-size-limit': ['ecr-change-image-layers-200-gb-2026-08'],
    'ecs-capacity-ec2-you-manage': ['ecs-cluster-ec2-full-control-you-manage-instances'],
    'ecs-cluster-auto-scaling-vs-service': ['ecs-cluster-auto-scaling-managed-scaling-asg-capacity-provider', 'ecs-service-auto-scaling-application-auto-scaling'],
    'ecs-cluster-fargate-serverless-pay-for-tasks': [],
    'ecs-faq-mi-instance-refresh-14-days': ['ecs-managed-instances-limited-lifetime-patching'],
    'ecs-faq-mi-not-in-govcloud-or-china': [],
    'ecs-service-long-running-stateless': ['ecs-service-scheduler-for-long-running-stateless'],
    'ecs-task-runs-then-stops': ['ecs-task-is-instantiation-of-task-definition'],
    'ecs-anywhere-faq-windows-containers-with-existing-license': ['ecs-anywhere-windows-support-deprecated'],
    'ecs-anywhere-free-tier-2200-instance-hours': [],
    'eks-deployment-options-hybrid-outposts-control-plane-aws-managed': ['eks-outposts-extended-vs-local-clusters'],
    'eks-faq-supports-three-stable-kubernetes-versions': ['eks-supports-at-least-three-versions'],
}
live = lambda i: i in facts and facts[i].get('status') not in ('rejected', 'superseded')
brief = json.load(open(brief_path))
changed = []
for d in brief['demand']:
    ids = d.get('facts') or []
    dead = [i for i in ids if not live(i)]
    if not dead:
        continue
    keep = [i for i in ids if live(i)]
    for i in dead:
        for r in replace.get(i, []):
            if live(r) and r not in keep:
                keep.append(r)
    d['facts'] = keep
    old = d.get('status')
    if not keep:
        d['status'] = 'not-found'
    d.setdefault('adjudication', []).append({'by': 'adjudicate-19', 'removed': dead, 'status_was': old})
    changed.append((d['id'], old, d['status'], dead, keep))
with open(brief_path, 'w') as fh:
    json.dump(brief, fh, indent=1, ensure_ascii=False)
    fh.write('\n')
for c in changed:
    print(c)
print(len(changed), 'demand rows updated')
