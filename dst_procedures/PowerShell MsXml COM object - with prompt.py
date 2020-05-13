{"query": {"bool": {"must": [{"match": {"process_parent_path": "cmd.exe"}}, {"match": {"process_name": "powershell.exe"}}, {"wildcard": {"process_command_line.keyword": {"value": "*$commsxml*"}}}]}}}
tactic = "Execution"
technique = "PowerShell"
procedure = "PowerShell MsXml COM object - with prompt"
tech_code = "T1086"
