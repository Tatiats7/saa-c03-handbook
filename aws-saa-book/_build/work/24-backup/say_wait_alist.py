import os, re, sys, time
p = 'aws-saa-book/24-backup/2-deep.md'
need = ['backup-snapshot-hourly-and-100-years', 'backup-retention-continuous-range',
        'backup-pitr-latest-restorable-time-by-service', 'backup-cold-storage-min-90-days-retention-rule',
        'backup-vault-lock-grace-time-minimum-3-days']
limit = float(sys.argv[1]) if len(sys.argv) > 1 else 560
t0 = time.time()
while time.time() - t0 < limit:
    if os.path.exists(p):
        txt = open(p).read()
        i = txt.find('### A-list')
        if i >= 0:
            seg = txt[i:]
            j = seg.find('\n### ', 5)
            seg = seg[:j] if j > 0 else seg
            found = [n for n in need if n in seg]
            if len(found) == len(need):
                print('READY', found)
                sys.exit(0)
            print('partial', found)
    time.sleep(20)
print('TIMEOUT exists=%s' % os.path.exists(p))
