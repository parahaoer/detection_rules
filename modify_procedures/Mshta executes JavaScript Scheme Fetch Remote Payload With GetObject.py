import json
from elasticsearch import Elasticsearch

es = Elasticsearch('10.25.23.161:9200')

doc = {
  "query": {
    "bool": {
      "should": [
        {
          "bool": {
            "must": [
              {
                "match": {
                  "process_name": "mshta.exe"
                }
              },
              {
                "wildcard": {
                  "process_command_line.keyword": "*javascript*"
                }
              }
            ]
          }
        },
        {
          "bool": {
            "must": [
              {
                "match": {
                  "process_name": "mshta.exe"
                }
              },
              {
                "match": {
                  "event_id": "3"
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
technique = "Mshta"
procedure = "Mshta executes JavaScript Scheme Fetch Remote Payload With GetObject"
tech_code = "T1170"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 93)

json_str = json.dumps(doc)
with open("dst_procedures/Mshta executes JavaScript Scheme Fetch Remote Payload With GetObject.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Execution"\n')
	f.write('technique = "Mshta"\n')
	f.write('procedure = "Mshta executes JavaScript Scheme Fetch Remote Payload With GetObject"\n')
	f.write('tech_code = "T1170"\n')
