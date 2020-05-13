{"query": {"bool": {"must": [{"match": {"process_parent_path": "cmd.exe"}}, {"match": {"process_name": "powershell.exe"}}, {"wildcard": {"process_command_line.keyword": {"value": "*invoke-apppathbypass*"}}}]}}}
tactic = "Execution"
technique = "PowerShell"
procedure = "Invoke-AppPathBypass"
tech_code = "T1086"
