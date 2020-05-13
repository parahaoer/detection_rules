{"query": {"constant_score": {"filter": {"bool": {"must": [{"wildcard": {"process_command_line.keyword": "*.cpl"}}, {"bool": {"must_not": [{"bool": {"must": [{"bool": {"should": [{"wildcard": {"process_command_line.keyword": "*\\\\System32\\\\*"}}, {"wildcard": {"process_command_line.keyword": "*%System%*"}}]}}]}}]}}]}}}}}
tactic = "Execution"
technique = "Control Panel Items"
procedure = "Control Panel Items"
tech_code = "T1196"
