import json
from elasticsearch import Elasticsearch

es = Elasticsearch('10.25.23.161:9200')

doc =  {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "match_phrase": {
                "event_id": "4656"
              }
            },
            {
              "match_phrase": {
                "object_type": "Key"
              }
            },
            {
              "match": {
                "object_name": "*\\\\SAM"
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
tactic = "Discovery"
technique = "Query Registry"
procedure = "SAM Registry Hive Handle Request"
tech_code = "T1012"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 31)

json_str = json.dumps(doc)
with open("dst_procedures/SAM Registry Hive Handle Request.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Discovery"\n')
	f.write('technique = "Query Registry"\n')
	f.write('procedure = "SAM Registry Hive Handle Request"\n')
	f.write('tech_code = "T1012"\n')
