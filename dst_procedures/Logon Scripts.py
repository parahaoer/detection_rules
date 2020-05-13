{"query": {"constant_score": {"filter": {"bool": {"must": [{"bool": {"should": [{"match_phrase": {"event_id": "11"}}, {"match_phrase": {"event_id": "12"}}, {"match_phrase": {"event_id": "13"}}, {"match_phrase": {"event_id": "14"}}]}}, {"wildcard": {"registry_key_path.keyword": "*UserInitMprLogonScript*"}}]}}}}}
tactic = "Persistence"
technique = "Logon Scripts"
procedure = "Logon Scripts"
tech_code = "T1037"
