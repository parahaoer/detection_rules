{"query": {"constant_score": {"filter": {"bool": {"must": [{"bool": {"must": [{"match_phrase": {"event_id": "3"}}, {"bool": {"should": [{"match_phrase": {"dst_port": "5985"}}, {"match_phrase": {"dst_port": "5986"}}]}}]}}, {"bool": {"must_not": [{"bool": {"must": [{"match_phrase": {"user_account": "NT AUTHORITY\\NETWORK SERVICE"}}]}}]}}]}}}}}
tactic = "Execution"
technique = "PowerShell"
procedure = "Remote PowerShell Session_2"
tech_code = "T1086"
