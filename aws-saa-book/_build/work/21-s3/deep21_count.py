"""deep-21 helper: word count per H2/H3 section of 21-s3/2-deep.md, with the lint's own counter."""
import re, sys
sys.path.insert(0, '/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/tools')
from saalib.lint import word_count
text = open('/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/21-s3/2-deep.md').read()
parts = re.split(r'(?m)^(#{2,3} .*)$', text)
print('total', word_count(text))
for i in range(1, len(parts), 2):
    body = parts[i + 1]
    gd = sum(word_count(b) for b in re.findall(r'(?s)<summary>Go deeper.*?</details>', body))
    print(word_count(body), 'gd', gd, parts[i][:70])
