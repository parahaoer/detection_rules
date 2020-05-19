import json
from elasticsearch import Elasticsearch

es = Elasticsearch('10.25.23.161:9200')

doc = {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "event_id": "10"
          }
        },
        {
          "match": {
            "process_name": "wsmprovhost.exe"
          }
        },
        {
          "wildcard": {
            "process_target_path.keyword": "*\\\\*.exe"
          }
        }
      ]
    }
  }
}

res = es.search(index="logs-endpoint-winevent-*",body=doc)

count = res['hits']['total']['value']
tactic = "Execution"
technique = "Windows Remote Management"
procedure = "WMIC Process Call Create"
tech_code = "T1028"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 121)

json_str = json.dumps(doc)
with open("dst_procedures/WMIC Process Call Create_2.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Execution"\n')
	f.write('technique = "Windows Remote Management"\n')
	f.write('procedure = "WMIC Process Call Create"\n')
	f.write('tech_code = "T1028"\n')
