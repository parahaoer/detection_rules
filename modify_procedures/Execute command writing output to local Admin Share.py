import json
from elasticsearch import Elasticsearch

es = Elasticsearch('10.25.23.161:9200')

doc = {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "bool": {
                "must": [
                  {
                    "match_phrase": {
                      "event_id": "5140"
                    }
                  },
                  {
                    "match_phrase": {
                      "share_name": "Admin$"
                    }
                  }
                ]
              }
            },
            {
              "bool": {
                "must_not": [
                  {
                    "bool": {
                      "must": [
                        {
                          "wildcard": {
                            "user_name.keyword": "*$"
                          }
                        }
                      ]
                    }
                  }
                ]
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
tactic = "Lateral Movement"
technique = "Windows Admin Shares"
procedure = "Execute command writing output to local Admin Share"
tech_code = "T1077"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 77)

json_str = json.dumps(doc)
with open("dst_procedures/Execute command writing output to local Admin Share.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Lateral Movement"\n')
	f.write('technique = "Windows Admin Shares"\n')
	f.write('procedure = "Execute command writing output to local Admin Share"\n')
	f.write('tech_code = "T1077"\n')
