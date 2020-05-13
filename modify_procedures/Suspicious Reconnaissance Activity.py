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
                "param3": "net group \"domain admins\" /domain"
              }
            },
            {
              "match_phrase": {
                "param3": "net localgroup administrators"
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
tactic = "Discovery"
technique = "Permission Groups Discovery"
procedure = "Suspicious Reconnaissance Activity"
tech_code = "T1069"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 37)

json_str = json.dumps(doc)
with open("dst_procedures/Suspicious Reconnaissance Activity.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Discovery"\n')
	f.write('technique = "Permission Groups Discovery"\n')
	f.write('procedure = "Suspicious Reconnaissance Activity"\n')
	f.write('tech_code = "T1069"\n')
