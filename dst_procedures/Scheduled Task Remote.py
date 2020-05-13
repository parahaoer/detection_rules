{"query": {"constant_score": {"filter": {"bool": {"must": [{"bool": {"must": [{"wildcard": {"process_path.keyword": "*\\\\schtasks.exe"}}, {"wildcard": {"process_command_line.keyword": "* /create *"}}]}}, {"bool": {"must_not": [{"bool": {"must": [{"match_phrase": {"user_account": "NT AUTHORITY\\SYSTEM"}}]}}]}}]}}}}}
tactic = "Execution"
technique = "Scheduled Task"
procedure = "Scheduled Task Remote"
tech_code = "T1053"
