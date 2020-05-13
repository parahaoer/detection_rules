import json
from elasticsearch import Elasticsearch

es = Elasticsearch('10.25.23.161:9200')

doc = {
  "query": {
    "bool": {
      "must": [
        {
          "match_phrase": {
            "process_path": "*\\\\pcalua.exe"
          }
        },
        {
          "wildcard": {
            "process_command_line.keyword": "*-a*"
          }
        }
      ]
    }
  }
}


res = es.search(index="logs-endpoint-winevent-*",body=doc)

count = res['hits']['total']['value']
tactic = "Defense Evasion"
technique = "Indirect Command Execution"
procedure = "Indirect Command Execution - pcalua.exe"
tech_code = "T1202"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 81)

json_str = json.dumps(doc)
with open("dst_procedures/Indirect Command Execution - pcalua.exe.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Defense Evasion"\n')
	f.write('technique = "Indirect Command Execution"\n')
	f.write('procedure = "Indirect Command Execution - pcalua.exe"\n')
	f.write('tech_code = "T1202"\n')
