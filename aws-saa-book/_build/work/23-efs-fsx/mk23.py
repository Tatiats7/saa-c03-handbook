import json,sys
W="/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/23-efs-fsx/"
URL={"efs-limits":("docs/efs/latest/ug/limits","https://docs.aws.amazon.com/efs/latest/ug/limits.html")}
def fact(id,kind,claim,question,disp,scope,dm="",adj=False,cond="",rel="extended",bul=None,quote=None,src=None,url=None,header=None,vol="stable",hard=True,svc=None,tier=1):
    svc=svc or id.split("-")[0]
    f={"id":id,"service":svc,"home_chapter":"23","kind":kind,"claim":claim,"question":question,
     "values":[{"key":"v%d"%i,"display":d} for i,d in enumerate([disp] if isinstance(disp,str) else disp)],
     "qualifiers":{"scope":scope,"default_or_max":dm,"adjustable":adj,"condition":cond},
     "source_tier":tier,"hard":hard,"tier0":False,"volatility":vol,"changed":None,"exam_relevance":rel,"bullets":bul or []}
    if quote is not None:
        f["evidence"]=[{"source_id":src,"url":url,"quote":quote,"table_header":header}]
    return f
def dump(name,facts):
    json.dump(facts,open(W+name,"w"),indent=0)

CMDS=[]
def adopt(name,source,snippet,id,kind,claim,q,disp,scope,dm="",adj=False,cond="",rel="extended",bul=None,**k):
    dump(name+".json",[fact(id,kind,claim,q,disp,scope,dm,adj,cond,rel,bul or [],**k)])
    CMDS.append((name,source,snippet))
def show_cmds():
    for n,s,t in CMDS:
        print(f"{n}\t{s}\t{t}")
