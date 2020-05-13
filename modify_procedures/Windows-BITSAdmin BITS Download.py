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
                    "bool": {
                      "should": [
                        {
                          "wildcard": {
                            "process_path.keyword": "*\\\\bitsadmin.exe"
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
                            "process_command_line.keyword": "* /transfer *"
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
                "should": [
                  {
                    "wildcard": {
                      "process_command_line.keyword": "*copy bitsadmin.exe*"
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
tactic = "Lateral Movement"
technique = "Remote File Copy"
procedure = "Windows-BITSAdmin BITS Download"
tech_code = "T1105"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 114)

json_str = json.dumps(doc)
with open("dst_procedures/Windows-BITSAdmin BITS Download.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Lateral Movement"\n')
	f.write('technique = "Remote File Copy"\n')
	f.write('procedure = "Windows-BITSAdmin BITS Download"\n')
	f.write('tech_code = "T1105"\n')
