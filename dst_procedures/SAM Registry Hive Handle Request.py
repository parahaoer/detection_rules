{"query": {"constant_score": {"filter": {"bool": {"must": [{"match_phrase": {"event_id": "4656"}}, {"match_phrase": {"object_type": "Key"}}, {"match": {"object_name": "*\\\\SAM"}}]}}}}}
tactic = "Discovery"
technique = "Query Registry"
procedure = "SAM Registry Hive Handle Request"
tech_code = "T1012"
