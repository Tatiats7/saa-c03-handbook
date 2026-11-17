import json,sys
src,dst=sys.argv[1],sys.argv[2]
ids=set(sys.argv[3:])
d=[f for f in json.load(open(src)) if f['id'] in ids]
json.dump(d,open(dst,'w'),ensure_ascii=False,indent=0)
print(len(d))
