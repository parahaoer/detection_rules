{"query": {"constant_score": {"filter": {"bool": {"must": [{"match_phrase": {"event_id": "524"}}, {"match_phrase": {"source_name": "Backup"}}]}}}}}
tactic = "Defense Evasion"
technique = "File Deletion"
procedure = "wbadmin"
tech_code = "T1107"
