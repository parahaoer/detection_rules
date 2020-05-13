import json
from elasticsearch import Elasticsearch

es = Elasticsearch('10.25.23.161:9200')

doc =  {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "param3": "* sekurlsa::logonpasswords *"
          }
        }
      ]
    }
  }
}


res = es.search(index="logs-endpoint-winevent-*",body=doc)

count = res['hits']['total']['value']
tactic = "Credential Access"
technique = "Credential Dumping"
procedure = "Mimikatz Use"
tech_code = "T1003"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 16)

json_str = json.dumps(doc)
with open("dst_procedures/Mimikatz Use.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Credential Access"\n')
	f.write('technique = "Credential Dumping"\n')
	f.write('procedure = "Mimikatz Use"\n')
	f.write('tech_code = "T1003"\n')
