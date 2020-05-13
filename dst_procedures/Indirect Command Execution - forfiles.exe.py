{"query": {"bool": {"must": [{"match": {"process_path": "*\\\\forfiles.exe"}}, {"wildcard": {"process_command_line.keyword": "* /m *"}}]}}}
tactic = "Defense Evasion"
technique = "Indirect Command Execution"
procedure = "Indirect Command Execution - forfiles.exe"
tech_code = "T1202"
