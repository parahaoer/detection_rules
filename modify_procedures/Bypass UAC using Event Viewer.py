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
              "bool": {
                "must": [
                  {
                    "match_phrase": {
                      "event_id": "13"
                    }
                  },
                  {
                    "wildcard": {
                      "registry_key_path.keyword": "HKU\\\\*\\\\mscfile\\\\shell\\\\open\\\\command\\\\*"
                    }
                  }
                ]
              }
            },
            {
              "bool": {
                "must": [
                  {
                    "bool": {
                      "must": [
                        {
                          "match_phrase": {
                            "event_id": "1"
                          }
                        },
                        {
                          "wildcard": {
                            "process_parent_path.keyword": "*\\\\eventvwr.exe"
                          }
                        }
                      ]
                    }
                  },
                  {
                    "bool": {
                      "must_not": [
                        {
                          "bool": {
                            "must": [
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\mmc.exe"
                                }
                              }
                            ]
                          }
                        }
                      ]
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
tactic = "Privilege Escalation"
technique = "Bypass User Account Control"
procedure = "Bypass UAC using Event Viewer"
tech_code = "T1088"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 52)

json_str = json.dumps(doc)
with open("dst_procedures/Bypass UAC using Event Viewer.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Privilege Escalation"\n')
	f.write('technique = "Bypass User Account Control"\n')
	f.write('procedure = "Bypass UAC using Event Viewer"\n')
	f.write('tech_code = "T1088"\n')
