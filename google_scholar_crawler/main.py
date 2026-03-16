from scholarly import scholarly
import json
from datetime import datetime
import os

AUTHOR_ID = 'aQkZOqQAAAAJ'

author: dict = scholarly.search_author_id(AUTHOR_ID)
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2, default=str))

os.makedirs('results', exist_ok=True)

# Full scholar data
with open('results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False, default=str)

# Citation badge for shields.io
shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": f"{author.get('citedby', 0)}",
}
with open('results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)

# H-index badge
hindex_data = {
    "schemaVersion": 1,
    "label": "h-index",
    "message": f"{author.get('hindex', 0)}",
}
with open('results/gs_data_shieldsio_hindex.json', 'w') as outfile:
    json.dump(hindex_data, outfile, ensure_ascii=False)

# i10-index badge
i10_data = {
    "schemaVersion": 1,
    "label": "i10-index",
    "message": f"{author.get('i10index', 0)}",
}
with open('results/gs_data_shieldsio_i10.json', 'w') as outfile:
    json.dump(i10_data, outfile, ensure_ascii=False)

print(f"\nUpdated: {author['updated']}")
print(f"Citations: {author.get('citedby', 0)}")
print(f"H-index: {author.get('hindex', 0)}")
print(f"i10-index: {author.get('i10index', 0)}")
print(f"Publications: {len(author['publications'])}")
