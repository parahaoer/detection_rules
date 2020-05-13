{"query": {"constant_score": {"filter": {"bool": {"must": [{"bool": {"should": [{"wildcard": {"process_path.keyword": "*\\\\wmic.exe"}}]}}, {"bool": {"should": [{"wildcard": {"process_command_line.keyword": "*/node:*process call create *"}}, {"wildcard": {"process_command_line.keyword": "* path AntiVirusProduct get *"}}, {"wildcard": {"process_command_line.keyword": "* path FirewallProduct get *"}}, {"wildcard": {"process_command_line.keyword": "* shadowcopy delete *"}}]}}]}}}}}
tactic = "Execution"
technique = "Windows Management Instrumentation"
procedure = "Suspicious WMI Execution"
tech_code = "T1047"
