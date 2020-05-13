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
                "event_id": "10"
              }
            },
            {
              "match_phrase": {
                "process_target_path": """C:\windows\system32\lsass.exe"""
              }
            },
            {
              "match_phrase": {
                "process_granted_access": "2097151"
              }
            },
            {
              "bool": {
                "should": [
                  {
                    "wildcard": {
                      "process_call_trace.keyword": "*dbghelp.DLL*"
                    }
                  },
                  {
                    "wildcard": {
                      "process_call_trace.keyword": "*dbgcore.DLL*"
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
technique = "Credential Dumping"
procedure = "LSASS Memory Dump"
tech_code = "T1003"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 10)

json_str = json.dumps(doc)
with open("dst_procedures/LSASS Memory Dump.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Credential Access"\n')
	f.write('technique = "Credential Dumping"\n')
	f.write('procedure = "LSASS Memory Dump"\n')
	f.write('tech_code = "T1003"\n')
