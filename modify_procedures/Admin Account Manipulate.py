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
                "should": [
                  {
                    "bool": {
                      "should": [
                        {
                          "bool": {
                            "must": [
                              {
                                "match_phrase": {
                                  "event_id": "4738"
                                }
                              }
                            ]
                          }
                        },
                        {
                          "bool": {
                            "must": [
                              {
                                "match_phrase": {
                                  "event_id": "5136"
                                }
                              },
                              {
                                "match_phrase": {
                                  "dsobject_attribute_name": "msDS-AllowedToDelegateTo"
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
                      "must": [
                        {
                          "match_phrase": {
                            "event_id": "5136"
                          }
                        },
                        {
                          "match_phrase": {
                            "dsobject_class": "user"
                          }
                        },
                        {
                          "match_phrase": {
                            "dsobject_attribute_name": "servicePrincipalName"
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
                "must": [
                  {
                    "match_phrase": {
                      "event_id": "5136"
                    }
                  },
                  {
                    "match_phrase": {
                      "dsobject_attribute_name": "msDS-AllowedToActOnBehalfOfOtherIdentity"
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
technique = "Account Manipulation"
procedure = "Admin Account Manipulate"
tech_code = "T1098"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 46)

json_str = json.dumps(doc)
with open("dst_procedures/Admin Account Manipulate.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Credential Access"\n')
	f.write('technique = "Account Manipulation"\n')
	f.write('procedure = "Admin Account Manipulate"\n')
	f.write('tech_code = "T1098"\n')
