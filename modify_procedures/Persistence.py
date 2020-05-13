import json
from elasticsearch import Elasticsearch

es = Elasticsearch('10.25.23.161:9200')

doc = {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "should": [
            {
              "match_phrase": {
                "event_id": "19"
              }
            },
            {
              "match_phrase": {
                "event_id": "20"
              }
            },
            {
              "match_phrase": {
                "event_id": "21"
              }
            }
          ]
        }
      }
    }
  }
}

res = es.search(index="logs-endpoint-winevent-*",body=doc)

count = res['hits']['total']['value']
tactic = "Persistence"
technique = "Windows Management Instrumentation Event Subscription"
procedure = "Persistence"
tech_code = "T1084"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 95)

json_str = json.dumps(doc)
with open("dst_procedures/Persistence.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Persistence"\n')
	f.write('technique = "Windows Management Instrumentation Event Subscription"\n')
	f.write('procedure = "Persistence"\n')
	f.write('tech_code = "T1084"\n')
