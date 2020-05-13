{"query": {"bool": {"must": [{"match": {"process_name": "wmic.exe"}}, {"bool": {"should": [{"wildcard": {"process_command_line.keyword": {"value": "* /node:*"}}}, {"wildcard": {"process_command_line.keyword": {"value": "* -node:*"}}}]}}, {"wildcard": {"process_command_line.keyword": {"value": "* *process* call *"}}}]}}}
tactic = "Execution"
technique = "Windows Management Instrumentation"
procedure = "WMI Execute Remote Process"
tech_code = "T1047"
