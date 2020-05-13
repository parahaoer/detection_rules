{"query": {"constant_score": {"filter": {"bool": {"must": [{"match_phrase": {"event_id": "13"}}, {"wildcard": {"registry_key_path.keyword": "*\\\\Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Debug*"}}]}}}}}
tactic = "Defense Evasion"
technique = "Obfuscated Files or Information"
procedure = "Execute base64-encoded PowerShell from Windows Registry"
tech_code = "T1027"
