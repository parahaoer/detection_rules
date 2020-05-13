import json
from elasticsearch import Elasticsearch

es = Elasticsearch('10.25.23.161:9200')

doc ={
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
tactic = "Execution"
technique = "Scheduled Task"
procedure = "Scheduled Task Remote"
tech_code = "T1053"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 110)

json_str = json.dumps(doc)
with open("dst_procedures/Scheduled Task Remote.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Execution"\n')
	f.write('technique = "Scheduled Task"\n')
	f.write('procedure = "Scheduled Task Remote"\n')
	f.write('tech_code = "T1053"\n')
