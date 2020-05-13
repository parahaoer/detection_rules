{"query": {"constant_score": {"filter": {"bool": {"must": [{"match_phrase": {"event_id": "13"}}, {"wildcard": {"registry_key_path.keyword": "*\\CurrentVersion\\Explorer\\Advanced\\HideFileExt*"}}, {"match_phrase": {"registry_key_value": "DWORD (0x00000001)"}}]}}}}}
tactic = "Defense Evasion"
technique = "Modify Registry"
procedure = "Modify Registry of Current User Profile - cmd"
tech_code = "T1112"
