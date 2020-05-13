{"query": {"constant_score": {"filter": {"bool": {"must": [{"match_phrase": {"event_id": "13"}}, {"wildcard": {"registry_key_path.keyword": "*\\\\Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Debug*"}}]}}}}}
tactic = "Defense Evasion"
technique = "Modify Registry"
procedure = "Modify registry to store PowerShell code"
tech_code = "T1112"
