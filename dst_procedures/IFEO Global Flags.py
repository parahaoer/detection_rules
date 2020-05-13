{"query": {"constant_score": {"filter": {"bool": {"must": [{"match_phrase": {"event_id": "13"}}, {"bool": {"should": [{"wildcard": {"registry_key_path.keyword": "*\\\\SOFTWARE\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\\\\Image File Execution Options\\\\*\\\\GlobalFlag"}}, {"wildcard": {"registry_key_path.keyword": "*\\\\SOFTWARE\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\\\\SilentProcessExit\\\\*\\\\ReportingMode"}}, {"wildcard": {"registry_key_path.keyword": "*\\\\SOFTWARE\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\\\\SilentProcessExit\\\\*\\\\MonitorProcess"}}]}}, {"match_phrase": {"event_type": "SetValue"}}]}}}}}
tactic = "Persistence"
technique = "Image File Execution Option Injection"
procedure = "IFEO Global Flags"
tech_code = "T1183"
