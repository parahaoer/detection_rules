{"query": {"bool": {"must": [{"wildcard": {"process_command_line.keyword": "*\\\\*.bat"}}]}}}
tactic = "Execution"
technique = "Scripting"
procedure = "Invoke-Command"
tech_code = "T1064"
