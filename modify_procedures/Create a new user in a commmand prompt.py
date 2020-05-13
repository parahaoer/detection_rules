import json
from elasticsearch import Elasticsearch

es = Elasticsearch('10.25.23.161:9200')

doc = {
  "query": {
    "constant_score": {
      "filter": {
        "match_phrase": {
          "event_id": "4720"
        }
      }
    }
  }
}

res = es.search(index="logs-endpoint-winevent-*",body=doc)

count = res['hits']['total']['value']
tactic = "Persistence"
technique = "Create Account"
procedure = "Create a new user in a commmand prompt"
tech_code = "T1136"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 61)

json_str = json.dumps(doc)
with open("dst_procedures/Create a new user in a commmand prompt.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Persistence"\n')
	f.write('technique = "Create Account"\n')
	f.write('procedure = "Create a new user in a commmand prompt"\n')
	f.write('tech_code = "T1136"\n')
