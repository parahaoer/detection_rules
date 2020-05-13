from elasticsearch import Elasticsearch

es = Elasticsearch('10.25.23.161:9200')

doc =   {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "param3": "*Mimikatz*"
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
procedure = "Malicious PowerShell Keywords"
tech_code = "T1003"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 12)

