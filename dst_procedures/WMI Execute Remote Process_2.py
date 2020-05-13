{"query": {"constant_score": {"filter": {"bool": {"must": [{"bool": {"should": [{"wildcard": {"process_path.keyword": "*\\\\wmic.exe"}}]}}, {"bool": {"should": [{"wildcard": {"process_command_line.keyword": "*/NODE:*process call create *"}}, {"wildcard": {"process_command_line.keyword": "* path AntiVirusProduct get *"}}, {"wildcard": {"process_command_line.keyword": "* path FirewallProduct get *"}}, {"wildcard": {"process_command_line.keyword": "* shadowcopy delete *"}}]}}]}}}}}
tactic = "Execution"
technique = "Windows Management Instrumentation"
procedure = "WMI Execute Remote Process_2"
tech_code = "T1047"
