{"query": {"bool": {"must": [{"match_phrase": {"process_path": "*\\\\pcalua.exe"}}, {"wildcard": {"process_command_line.keyword": "*-a*"}}]}}}
tactic = "Defense Evasion"
technique = "Indirect Command Execution"
procedure = "Indirect Command Execution - pcalua.exe"
tech_code = "T1202"
