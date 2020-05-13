import json
from elasticsearch import Elasticsearch

es = Elasticsearch('10.25.23.161:9200')

doc = {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "process_parent_path": "cmd.exe"
          }
        },
        {
          "match": {
            "process_name": "powershell.exe"
          }
        },
        {
          "wildcard": {
            "process_command_line.keyword": {
              "value": "*invoke-bloodhound*"
            }
          }
        }
      ]
    }
  }
}



res = es.search(index="logs-endpoint-winevent-*",body=doc)

count = res['hits']['total']['value']
tactic = "Execution"
technique = "PowerShell"
procedure = "BloodHound"
tech_code = "T1086"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 50)

json_str = json.dumps(doc)
with open("dst_procedures/BloodHound.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Execution"\n')
	f.write('technique = "PowerShell"\n')
	f.write('procedure = "BloodHound"\n')
	f.write('tech_code = "T1086"\n')
