import json
from elasticsearch import Elasticsearch

es = Elasticsearch('10.25.23.161:9200')

doc = {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "should": [
            {
              "wildcard": {
                "process_command_line.keyword": "* -decode *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* /decode *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* -decodehex *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* /decodehex *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* -urlcache *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* /urlcache *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* -verifyctl *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* /verifyctl *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* -encode *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* /encode *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*certutil* -URL*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*certutil* /URL*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*certutil* -ping*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*certutil* /ping*"
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
tactic = "Defense Evasion"
technique = "Deobfuscate/Decode Files or Information"
procedure = "Deobfuscate/Decode Files Or Information"
tech_code = "T1140"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 55)

json_str = json.dumps(doc)
with open("dst_procedures/Certutil Rename and Decode.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Defense Evasion"\n')
	f.write('technique = "Deobfuscate/Decode Files or Information"\n')
	f.write('procedure = "Certutil Rename and Decode"\n')
	f.write('tech_code = "T1140"\n')
