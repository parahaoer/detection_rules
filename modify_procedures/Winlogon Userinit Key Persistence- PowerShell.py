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
                "event_id": "4104"
              }
            },
            {
              "bool": {
                "should": [
                  {
                    "multi_match": {
                      "query": "*Set-ItemProperty*",
                      "fields": [],
                      "type": "phrase"
                    }
                  },
                  {
                    "multi_match": {
                      "query": "*New-Item*",
                      "fields": [],
                      "type": "phrase"
                    }
                  }
                ]
              }
            },
            {
              "multi_match": {
                "query": "*CurrentVersion\\Winlogon*",
                "fields": [],
                "type": "phrase"
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
technique = "Winlogon Helper DLL"
procedure = "Winlogon Userinit Key Persistence- PowerShell"
tech_code = "T1004"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 117)

json_str = json.dumps(doc)
with open("dst_procedures/Winlogon Userinit Key Persistence- PowerShell.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Persistence"\n')
	f.write('technique = "Winlogon Helper DLL"\n')
	f.write('procedure = "Winlogon Userinit Key Persistence- PowerShell"\n')
	f.write('tech_code = "T1004"\n')
