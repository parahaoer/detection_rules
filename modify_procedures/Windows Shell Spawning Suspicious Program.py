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
              "bool": {
                "must": [
                  {
                    "bool": {
                      "should": [
                        {
                          "wildcard": {
                            "process_parent_path.keyword": "*\\\\mshta.exe"
                          }
                        },
                        {
                          "wildcard": {
                            "process_parent_path.keyword": "*\\\\powershell.exe"
                          }
                        },
                        {
                          "wildcard": {
                            "process_parent_path.keyword": "*\\\\rundll32.exe"
                          }
                        },
                        {
                          "wildcard": {
                            "process_parent_path.keyword": "*\\\\cscript.exe"
                          }
                        },
                        {
                          "wildcard": {
                            "process_parent_path.keyword": "*\\\\wscript.exe"
                          }
                        },
                        {
                          "wildcard": {
                            "process_parent_path.keyword": "*\\\\wmiprvse.exe"
                          }
                        }
                      ]
                    }
                  },
                  {
                    "bool": {
                      "should": [
                        {
                          "wildcard": {
                            "process_path.keyword": "*\\\\schtasks.exe"
                          }
                        },
                        {
                          "wildcard": {
                            "process_path.keyword": "*\\\\nslookup.exe"
                          }
                        },
                        {
                          "wildcard": {
                            "process_path.keyword": "*\\\\certutil.exe"
                          }
                        },
                        {
                          "wildcard": {
                            "process_path.keyword": "*\\\\bitsadmin.exe"
                          }
                        },
                        {
                          "wildcard": {
                            "process_path.keyword": "*\\\\mshta.exe"
                          }
                        }
                      ]
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
                            "process_current_directory.keyword": "*\\\\ccmcache\\\\*"
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
tactic = "Execution"
technique = "Scripting"
procedure = "Windows Shell Spawning Suspicious Program"
tech_code = "T1064"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 41)

json_str = json.dumps(doc)
with open("dst_procedures/Windows Shell Spawning Suspicious Program.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Execution"\n')
	f.write('technique = "Scripting"\n')
	f.write('procedure = "Windows Shell Spawning Suspicious Program"\n')
	f.write('tech_code = "T1064"\n')
