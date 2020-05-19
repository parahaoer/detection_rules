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
                      "process_command_line.keyword": "*/NODE:*process call create *"
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
procedure = "WMI Execute Remote Process"
tech_code = "T1047"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 119)

json_str = json.dumps(doc)
with open("dst_procedures/WMI Execute Remote Process_2.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Execution"\n')
	f.write('technique = "Windows Management Instrumentation"\n')
	f.write('procedure = "WMI Execute Remote Process"\n')
	f.write('tech_code = "T1047"\n')
