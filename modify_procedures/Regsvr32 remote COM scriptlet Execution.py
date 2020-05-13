import json
from elasticsearch import Elasticsearch

es = Elasticsearch('10.25.23.161:9200')

doc = {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "process_name": "regsvr32.exe"
          }
        },
        {
          "bool": {
            "should": [
              {
                "wildcard": {
                  "process_command_line.keyword": "*scrobj*"
                }
              },
              {
                "wildcard": {
                  "process_command_line.keyword": "*/i:*"
                }
              },
              {
                "wildcard": {
                  "process_command_line.keyword": "*-i:*"
                }
              },
              {
                "wildcard": {
                  "process_command_line.keyword": "*.sct*"
                }
              }
            ]
          }
        }
      ]
    }
  }
}

res = es.search(index="logs-endpoint-winevent-*",body=doc)

count = res['hits']['total']['value']
tactic = "Execution"
technique = "Regsvr32"
procedure = "Regsvr32 remote COM scriptlet Execution"
tech_code = "T1117"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 107)

json_str = json.dumps(doc)
with open("dst_procedures/Regsvr32 remote COM scriptlet Execution.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Execution"\n')
	f.write('technique = "Regsvr32"\n')
	f.write('procedure = "Regsvr32 remote COM scriptlet Execution"\n')
	f.write('tech_code = "T1117"\n')
