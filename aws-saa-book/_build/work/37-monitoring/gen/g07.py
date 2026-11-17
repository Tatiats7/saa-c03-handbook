from lib import *
import json
def A(fn,*a,**k):
    f=F(*a,[],**k); del f['evidence']
    json.dump([f],open('../'+fn,'w'),indent=1,ensure_ascii=False)
A("adopt-ct20.json","cloudtrail-change-lake-closed-to-new-customers-2026-03","change",
 "The CloudTrail document history row dated March 31, 2026 announces that AWS CloudTrail Lake will no longer be open to new customers starting May 31, 2026, and that existing customers can continue to use the service as normal.",
 "When was the CloudTrail Lake closure to new customers announced, and from when does it apply?",
 [("announced","March 31, 2026"),("from","May 31, 2026")],"","",False,"",
 rel="core",bullets=["1.3.K1"],service="cloudtrail",tier=3,vol="frequently-changing",ci=[chg('cloudtrail-document-history',13)],
 note="Current truth: cloudtrail-lake-closed-to-new-customers-2026-05-31.")
