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
              "match_phrase": {
                "event_id": "5156"
              }
            },
            {
              "bool": {
                "should": [
                  {
                    "match_phrase": {
                      "dst_port": "5985"
                    }
                  },
                  {
                    "match_phrase": {
                      "dst_port": "5986"
                    }
                  }
                ]
              }
            },
            {
              "match_phrase": {
                "network_layer_id": "44"
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
technique = "PowerShell"
procedure = "Remote PowerShell Session"
tech_code = "T1086"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 26)

json_str = json.dumps(doc)
with open("dst_procedures/Remote PowerShell Session.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Execution"\n')
	f.write('technique = "PowerShell"\n')
	f.write('procedure = "Remote PowerShell Session"\n')
	f.write('tech_code = "T1086"\n')
