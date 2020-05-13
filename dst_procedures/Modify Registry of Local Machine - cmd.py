{"query": {"constant_score": {"filter": {"bool": {"must": [{"match_phrase": {"event_id": "13"}}, {"wildcard": {"registry_key_path.keyword": "*\\\\Windows\\\\CurrentVersion\\\\Run\\\\SecurityHealth*"}}]}}}}}
tactic = "Defense Evasion"
technique = "Modify Registry"
procedure = "Modify Registry of Local Machine - cmd"
tech_code = "T1112"
