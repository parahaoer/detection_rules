import json
from elasticsearch import Elasticsearch

es = Elasticsearch('10.25.23.161:9200')

doc = {
  "query": {
    "bool": {
      "must": [
        {
          "wildcard": {
            "process_command_line.keyword": "*\\\\*.bat"
          }
        }
      ]
    }
  }
}

res = es.search(index="logs-endpoint-winevent-*",body=doc)

count = res['hits']['total']['value']
tactic = "Execution"
technique = "Scripting"
procedure = "Invoke-Command"
tech_code = "T1064"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 83)

json_str = json.dumps(doc)
with open("dst_procedures/Invoke-Command.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Execution"\n')
	f.write('technique = "Scripting"\n')
	f.write('procedure = "Invoke-Command"\n')
	f.write('tech_code = "T1064"\n')
