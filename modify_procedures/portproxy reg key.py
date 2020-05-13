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
              "match": {
                "process_command_line": " interface portproxy add v4tov4 *"
              }
            },
            {
              "match":{
                "process_name": "netsh.exe"
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
technique = "Connection Proxy"
procedure = "portproxy reg key"
tech_code = "T1090"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 96)

json_str = json.dumps(doc)
with open("dst_procedures/portproxy reg key.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Defense Evasion"\n')
	f.write('technique = "Connection Proxy"\n')
	f.write('procedure = "portproxy reg key"\n')
	f.write('tech_code = "T1090"\n')
