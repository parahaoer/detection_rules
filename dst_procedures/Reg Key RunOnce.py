{"query": {"constant_score": {"filter": {"bool": {"must": [{"match_phrase": {"event_id": "13"}}, {"bool": {"should": [{"wildcard": {"registry_key_path.keyword": "*\\\\Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run\\\\*"}}, {"wildcard": {"registry_key_path.keyword": "*\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\RunOnce\\\\*"}}, {"wildcard": {"registry_key_path.keyword": "*\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\RunOnceEx\\\\*"}}]}}]}}}}}
tactic = "Persistence"
technique = "Registry Run Keys/Startup Folder"
procedure = "Reg Key RunOnce"
tech_code = "T1060"
