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
              "match_phrase": {
                "process_command_line": "vssadmin.exe Delete Shadows"
              }
            },
            {
              "match_phrase": {
                "process_command_line": "vssadmin.exe create shadow /for=C:"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "copy \\\\\\\\?\\\\GLOBALROOT\\\\Device\\\\*\\\\windows\\\\ntds\\\\ntds.dit"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "copy \\\\\\\\?\\\\GLOBALROOT\\\\Device\\\\*\\\\config\\\\SAM"
              }
            },
            {
              "match_phrase": {
                "process_command_line": "vssadmin delete shadows /for=C:"
              }
            },
            {
              "match_phrase": {
                "process_command_line": "reg SAVE HKLM\\SYSTEM "
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "esentutl.exe /y /vss *\\\\ntds.dit*"
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
procedure = "Registry dump of SAM, creds, and secrets"
tech_code = "T1003"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 105)

json_str = json.dumps(doc)
with open("dst_procedures/Registry dump of SAM, creds, and secrets.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Credential Access"\n')
	f.write('technique = "Credential Dumping"\n')
	f.write('procedure = "Registry dump of SAM, creds, and secrets"\n')
	f.write('tech_code = "T1003"\n')
