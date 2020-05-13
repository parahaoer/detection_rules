import json
from elasticsearch import Elasticsearch

es = Elasticsearch('10.25.23.161:9200')

doc = {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "event_id": "255"
          }
        }
      ]
    }
  }
}


res = es.search(index="logs-endpoint-winevent-*",body=doc)

count = res['hits']['total']['value']
tactic = "Defense Evasion"
technique = "Disabling Security Tools"
procedure = "Unload Sysmon Filter Driver"
tech_code = "T1089"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 111)

json_str = json.dumps(doc)
with open("dst_procedures/Unload Sysmon Filter Driver.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Defense Evasion"\n')
	f.write('technique = "Disabling Security Tools"\n')
	f.write('procedure = "Unload Sysmon Filter Driver"\n')
	f.write('tech_code = "T1089"\n')
