import json
URL={'docs':'https://docs.aws.amazon.com/','www':'https://aws.amazon.com/'}
def url_of(sid):
    try:
        m=json.load(open('/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/corpus/snap/'+sid+'.meta.json'))
        if m.get('url'): return m['url']
    except Exception: pass
    host,path=sid.split('/',1)
    if host=='docs': return URL['docs']+path+'.html'
    p=path
    return URL['www']+p+'/'
def E(sid,quote,th=None,heading=None):
    e={"source_id":sid,"url":url_of(sid),"quote":quote,"table_header":th}
    if heading: e["heading"]=heading
    return e
def F(id,kind,claim,question,values,scope,dom,adj,cond,ev,tier=1,tier0=False,vol="stable",changed=None,rel="reference",bullets=None,note=None,service="cloudwatch",ci=None,hard=True):
    vals=[]
    for k,v in values:
        if isinstance(v,tuple): vals.append({"key":k,"display":v[0],"spoken":v[1]})
        else: vals.append({"key":k,"display":v})
    d={"id":id,"service":service,"home_chapter":"37","kind":kind,"claim":claim,"question":question,"values":vals,
       "qualifiers":{"scope":scope,"default_or_max":dom,"adjustable":adj,"condition":cond},
       "evidence":ev,"source_tier":tier,"hard":hard,"tier0":tier0,"volatility":vol,"changed":changed,
       "exam_relevance":rel,"bullets":bullets or []}
    if note: d["note"]=note
    if ci: d["change_items"]=ci
    return d
def dump(fn,facts):
    json.dump(facts,open(fn,'w'),indent=1,ensure_ascii=False)

import glob
_CH=None
def chg(frag, hist_line=None, svc=None):
    """return change item id whose url contains frag (whatsnew) or history line"""
    global _CH
    if _CH is None:
        _CH=[]
        for fn in glob.glob('/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/corpus/changes/*.jsonl'):
            for l in open(fn):
                try: _CH.append(json.loads(l))
                except: pass
    for r in _CH:
        if hist_line is not None:
            if r.get('source')=='history' and frag in r.get('history_source_id','') and r.get('line')==hist_line:
                return r['history_source_id']+'#'+str(hist_line)
        elif frag in r.get('url','') and r.get('source')=='whatsnew':
            return r['id']
    raise SystemExit('no change item for '+str(frag)+str(hist_line))
def H(sid,heading,line):
    return E(sid,line,None,heading)
