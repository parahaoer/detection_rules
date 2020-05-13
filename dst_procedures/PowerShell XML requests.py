{"query": {"bool": {"must": [{"match": {"process_name": "powershell.exe"}}, {"wildcard": {"process_command_line.keyword": {"value": "*$xml*"}}}]}}}
tactic = "Execution"
technique = "PowerShell"
procedure = "PowerShell XML requests"
tech_code = "T1086"
