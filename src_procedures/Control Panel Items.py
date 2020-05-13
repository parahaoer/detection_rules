from elasticsearch import Elasticsearch

es = Elasticsearch('10.25.23.161:9200')

doc = {  
  "query": {  
    "constant_score": {  
      "filter": {  
        "bool": {  
          "must": [  
            {  
              "wildcard": {  
                "process_command_line.keyword": "*.cpl"  
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
                                  "process_command_line.keyword": "*\\\\System32\\\\*"  
                                }  
                              },  
                              {  
                                "wildcard": {  
                                  "process_command_line.keyword": "*%System%*"  
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
technique = "Control Panel Items"
procedure = "Control Panel Items"
tech_code = "T1196"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 121)
