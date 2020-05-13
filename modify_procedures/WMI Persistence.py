import json
from elasticsearch import Elasticsearch

es = Elasticsearch('10.25.23.161:9200')

doc =  {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "should": [
            {
              "bool": {
                "must": [
                  {
                    "match_phrase": {
                      "event_id": "5861"
                    }
                  },
                  {
                    "bool": {
                      "should": [
                        {
                          "wildcard": {
                            "Message.keyword": "*ActiveScriptEventConsumer*"
                          }
                        },
                        {
                          "wildcard": {
                            "Message.keyword": "*CommandLineEventConsumer*"
                          }
                        },
                        {
                          "wildcard": {
                            "Message.keyword": "*CommandLineTemplate*"
                          }
                        }
                      ]
                    }
                  }
                ]
              }
            },
            {
              "match_phrase": {
                "event_id": "5859"
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
procedure = "WMI Persistence"
tech_code = "T1047"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 44)

json_str = json.dumps(doc)
with open("dst_procedures/WMI Persistence.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Execution"\n')
	f.write('technique = "Windows Management Instrumentation"\n')
	f.write('procedure = "WMI Persistence"\n')
	f.write('tech_code = "T1047"\n')
