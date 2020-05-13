import json
from elasticsearch import Elasticsearch

es = Elasticsearch('10.25.23.161:9200')

doc = {
  "query": {
    "bool": {
      "must": [
        {
          "bool": {
            "should": [
              {
                "wildcard": {
                  "process_parent_path.keyword": """*\\explorer.exe"""
                }
              },
              {
                "wildcard": {
                  "process_parent_path.keyword": """*\\services.exe"""
                }
              },
              {
                "wildcard": {
                  "process_parent_path.keyword": """*\\wmiprvse.exe"""
                }
              },
              {
                "wildcard": {
                  "process_parent_path.keyword": """*\\mmc.exe"""
                }
              }
            ]
          }
        },
        {
          "wildcard": {
            "process_command_line.keyword": {
              "value": """*\\cmd.exe* /c*"""
            }
          }
        }
      ]
    }
  }
}


res = es.search(index="logs-endpoint-winevent-*",body=doc)

count = res['hits']['total']['value']
tactic = "Lateral Movement"
technique = "Component Object Model and Distributed COM"
procedure = "Impacket Lateralization Detection"
tech_code = "T1175"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 8)

json_str = json.dumps(doc)
with open("dst_procedures/Impacket Lateralization Detection.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Lateral Movement"\n')
	f.write('technique = "Component Object Model and Distributed COM"\n')
	f.write('procedure = "Impacket Lateralization Detection"\n')
	f.write('tech_code = "T1175"\n')
