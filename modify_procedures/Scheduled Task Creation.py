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
                    "wildcard": {
                      "process_path.keyword": "*\\\\schtasks.exe"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "* /create *"
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
                          "match_phrase": {
                            "user_account": "NT AUTHORITY\\SYSTEM"
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
tactic = "Persistence"
technique = "Scheduled Task"
procedure = "Scheduled Task Creation"
tech_code = "T1053"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 32)

json_str = json.dumps(doc)
with open("dst_procedures/Scheduled Task Creation.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Persistence"\n')
	f.write('technique = "Scheduled Task"\n')
	f.write('procedure = "Scheduled Task Creation"\n')
	f.write('tech_code = "T1053"\n')
