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
                "should": [
                  {
                    "wildcard": {
                      "process_parent_path.keyword": "*\\\\wmiprvse.exe"
                    }
                  }
                ]
              }
            },
            {
              "bool": {
                "should": [
                  {
                    "wildcard": {
                      "process_path.keyword": "*\\\\powershell.exe"
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
technique = "Scripting"
procedure = "WMI Spawning Windows PowerShell"
tech_code = "T1064"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 45)

json_str = json.dumps(doc)
with open("dst_procedures/WMI Spawning Windows PowerShell.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Execution"\n')
	f.write('technique = "Scripting"\n')
	f.write('procedure = "WMI Spawning Windows PowerShell"\n')
	f.write('tech_code = "T1064"\n')
