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
                      "registry_key_path.keyword": "*\\\\SOFTWARE\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\\\\Image File Execution Options\\\\*\\\\GlobalFlag"
                    }
                  },
                  {
                    "wildcard": {
                      "registry_key_path.keyword": "*\\\\SOFTWARE\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\\\\SilentProcessExit\\\\*\\\\ReportingMode"
                    }
                  },
                  {
                    "wildcard": {
                      "registry_key_path.keyword": "*\\\\SOFTWARE\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\\\\SilentProcessExit\\\\*\\\\MonitorProcess"
                    }
                  }
                ]
              }
            },
            {
              "match_phrase": {
                "event_type": "SetValue"
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
tactic = "Persistence"
technique = "Image File Execution Option Injection"
procedure = "IFEO Global Flags"
tech_code = "T1183"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 79)

json_str = json.dumps(doc)
with open("dst_procedures/IFEO Global Flags.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Persistence"\n')
	f.write('technique = "Image File Execution Option Injection"\n')
	f.write('procedure = "IFEO Global Flags"\n')
	f.write('tech_code = "T1183"\n')
