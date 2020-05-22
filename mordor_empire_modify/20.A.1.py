import json
from elasticsearch import Elasticsearch

es = Elasticsearch('10.25.23.6:9200')

search_doc_a = {
  "size": 10000,
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "event_id": "261"
          }
        }
      ]
    }
  }
}

res_a = es.search(index="logs-endpoint-winevent-*",body=search_doc_a)

count = res_a['hits']['total']['value']

tactic = "Persistence"
technique = "Accessibility Features"
tech_code = "T1015"
eval_phase = "Execution of Persistence"
eval_step = "20.A.1"

action = {
  "Tactic": tactic,
  "Technique": technique,
  "Tech_code": tech_code,
  "EvalStep": eval_step,
  "EvalPhase": eval_phase,
  "EventCount": count,
}

es.index(index="represent_7", body=action, id=49)
with open("mordor_empire_dst/" + eval_step + ".yml", "w") as f:
	search_doc_a = json.dumps(search_doc_a)
	f.write("search_doc_a : " + search_doc_a+"\n")
	f.write("tactic : " + tactic+"\n")
	f.write("technique : " + technique+"\n")
	f.write("tech_code : " + tech_code+"\n")
	f.write("eval_phase : " + eval_phase+"\n")
	f.write("eval_step : " + eval_step+"\n")
