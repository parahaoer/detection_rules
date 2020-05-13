{"query": {"bool": {"must": [{"match": {"process_path": "powershell.exe"}}, {"wildcard": {"process_command_line.keyword": "*version*"}}]}}}
tactic = "Execution"
technique = "PowerShell"
procedure = "PowerShell Downgrade Attack"
tech_code = "T1086"
