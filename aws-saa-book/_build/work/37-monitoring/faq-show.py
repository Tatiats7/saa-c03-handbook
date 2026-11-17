import json,sys
name=sys.argv[1]
nums=[int(x) for x in sys.argv[2].split(',')]
rows=[json.loads(l) for l in open(f'aws-saa-book/_build/corpus/faq/{name}.jsonl')]
by={r['position']:r for r in rows}
for n in nums:
    r=by[n]
    print(f"#{n} [{r['section']}] {r['question']}\n{r['answer']}\n")
