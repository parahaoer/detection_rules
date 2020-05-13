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
                    "match_phrase": {
                      "event_id": "7"
                    }
                  },
                  {
                    "bool": {
                      "should": [
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\wmiclnt.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\WmiApRpl.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\wmiprov.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\wmiutils.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\wbemcomn.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\wbemprox.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\WMINet_Utils.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\wbemsvc.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\fastprox.dll"
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
                          "bool": {
                            "should": [
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\WmiPrvSe.exe"
                                }
                              },
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\WmiAPsrv.exe"
                                }
                              },
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\svchost.exe"
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
tactic = "Execution"
technique = "Windows Management Instrumentation"
procedure = "WMI Modules Loaded"
tech_code = "T1047"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 43)

json_str = json.dumps(doc)
with open("dst_procedures/WMI Modules Loaded.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Execution"\n')
	f.write('technique = "Windows Management Instrumentation"\n')
	f.write('procedure = "WMI Modules Loaded"\n')
	f.write('tech_code = "T1047"\n')
