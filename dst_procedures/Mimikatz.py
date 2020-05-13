{"query": {"bool": {"must": [{"match": {"process_parent_path": "cmd.exe"}}, {"match": {"process_name": "powershell.exe"}}, {"wildcard": {"process_command_line.keyword": {"value": "*invoke-mimikatz*"}}}]}}}
tactic = "Execution"
technique = "PowerShell"
procedure = "Mimikatz"
tech_code = "T1086"
