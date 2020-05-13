{"query": {"constant_score": {"filter": {"bool": {"must": [{"match_phrase": {"event_id": "13"}}, {"bool": {"should": [{"wildcard": {"registry_key_path.keyword": "*\\\\SOFTWARE\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\\\\Image File Execution Options\\\\winword.exe\\\\*"}}]}}, {"match_phrase": {"event_type": "SetValue"}}]}}}}}
tactic = "Persistence"
technique = "Image File Execution Option Injection"
procedure = "IFEO Add Debugger"
tech_code = "T1183"
