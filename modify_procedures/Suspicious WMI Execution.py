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
                      "process_path.keyword": "*\\\\wmic.exe"
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
                      "process_command_line.keyword": "*/node:*process call create *"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "* path AntiVirusProduct get *"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "* path FirewallProduct get *"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "* shadowcopy delete *"
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
technique = "Windows Management Instrumentation"
procedure = "Suspicious WMI Execution"
tech_code = "T1047"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 39)

json_str = json.dumps(doc)
with open("dst_procedures/Suspicious WMI Execution.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Execution"\n')
	f.write('technique = "Windows Management Instrumentation"\n')
	f.write('procedure = "Suspicious WMI Execution"\n')
	f.write('tech_code = "T1047"\n')
