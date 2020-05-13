{"query": {"constant_score": {"filter": {"bool": {"must": [{"bool": {"must": [{"wildcard": {"process_path.keyword": "*\\\\schtasks.exe"}}, {"wildcard": {"process_command_line.keyword": "* /create *"}}]}}, {"bool": {"must_not": [{"bool": {"must": [{"match_phrase": {"user_account": "NT AUTHORITY\\SYSTEM"}}]}}]}}]}}}}}
tactic = "Persistence"
technique = "Scheduled Task"
procedure = "Scheduled Task Creation"
tech_code = "T1053"
