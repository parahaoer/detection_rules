{"query": {"bool": {"must": [{"match": {"process_name": "regsvr32.exe"}}, {"bool": {"should": [{"wildcard": {"process_command_line.keyword": "*scrobj*"}}, {"wildcard": {"process_command_line.keyword": "*/i:*"}}, {"wildcard": {"process_command_line.keyword": "*-i:*"}}, {"wildcard": {"process_command_line.keyword": "*.sct*"}}]}}]}}}
tactic = "Execution"
technique = "Regsvr32"
procedure = "Regsvr32 remote COM scriptlet Execution"
tech_code = "T1117"
