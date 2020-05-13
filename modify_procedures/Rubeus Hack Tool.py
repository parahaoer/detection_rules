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
              "wildcard": {
                "process_command_line.keyword": "* asreproast *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* dump /service:krbtgt *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* kerberoast *"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* createnetonly /program:*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* ptt /ticket:*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* /impersonateuser:*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* renew /ticket:*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* asktgt /user:*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "* harvest /interval:*"
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
procedure = "Rubeus Hack Tool"
tech_code = "T1003"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 30)

json_str = json.dumps(doc)
with open("dst_procedures/Rubeus Hack Tool.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Credential Access"\n')
	f.write('technique = "Credential Dumping"\n')
	f.write('procedure = "Rubeus Hack Tool"\n')
	f.write('tech_code = "T1003"\n')
