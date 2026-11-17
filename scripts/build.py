"""Build docs/index.html (single self-contained file) from src/template.html + data/*.json."""
import json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
db = {k: json.load(open(root/'data'/f'{k}.json', encoding='utf-8'))
      for k in ['recs','classes','purposes','cats','notes','prov']}
html = (root/'src'/'template.html').read_text(encoding='utf-8')
assert '/*__DB__*/' in html
out = html.replace('/*__DB__*/', json.dumps(db, ensure_ascii=False, separators=(',',':')))
d = root/'docs'; d.mkdir(exist_ok=True)
(d/'index.html').write_text(out, encoding='utf-8')
(d/'.nojekyll').write_text('')
print('built', d/'index.html', len(out), 'bytes;', len(db['recs']), 'records')
