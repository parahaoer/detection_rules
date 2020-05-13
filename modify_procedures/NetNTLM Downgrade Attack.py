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
                  "event_id": "13"
                }
              },
              {
                "bool": {
                  "should": [
                    {
                      "wildcard": {
                        "registry_key_path.keyword": "*System\\\\*ControlSet*\\\\Control\\\\Lsa\\\\LMCompatibilityLevel"
                      }
                    },
                    {
                      "wildcard": {
                        "registry_key_path.keyword": "*System\\\\*ControlSet*\\\\Control\\\\Lsa\\\\MSV1_0\\\\NtlmMinClientSec"
                      }
                    },
                    {
                      "wildcard": {
                        "registry_key_path.keyword": "*System\\\\*ControlSet*\\\\Control\\\\Lsa\\\\MSV1_0\\\\RestrictSendingNTLMTraffic"
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
tactic = "Credential Access"
technique = "Exploitation for Credential Access"
procedure = "NetNTLM Downgrade Attack"
tech_code = "T1212"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 18)

json_str = json.dumps(doc)
with open("dst_procedures/NetNTLM Downgrade Attack.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Credential Access"\n')
	f.write('technique = "Exploitation for Credential Access"\n')
	f.write('procedure = "NetNTLM Downgrade Attack"\n')
	f.write('tech_code = "T1212"\n')
