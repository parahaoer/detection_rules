import json
from elasticsearch import Elasticsearch

es = Elasticsearch('10.25.23.161:9200')

doc = {
  "query": {
    "bool": {
      "must": [

        {
          "match": {
            "process_parent_name": "psexesvc.exe"
          }
        }
      ]
    }
  }
}

res = es.search(index="logs-endpoint-winevent-*",body=doc)

count = res['hits']['total']['value']
tactic = "Execution"
technique = "Windows Remote Management"
procedure = "Psexec"
tech_code = "T1028"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 102)

json_str = json.dumps(doc)
with open("dst_procedures/Psexec.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Execution"\n')
	f.write('technique = "Windows Remote Management"\n')
	f.write('procedure = "Psexec"\n')
	f.write('tech_code = "T1028"\n')
