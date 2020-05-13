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
                "event_id": "517"
              }
            },
            {
              "match_phrase": {
                "event_id": "1102"
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
tactic = "Defense Evasion"
technique = "Indicator Removal on Host"
procedure = "Delete Security Logs Using Clear-EventLogId"
tech_code = "T1070"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 66)

json_str = json.dumps(doc)
with open("dst_procedures/Delete Security Logs Using Clear-EventLogId.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Defense Evasion"\n')
	f.write('technique = "Indicator Removal on Host"\n')
	f.write('procedure = "Delete Security Logs Using Clear-EventLogId"\n')
	f.write('tech_code = "T1070"\n')
