{"query": {"constant_score": {"filter": {"bool": {"must": [{"bool": {"should": [{"wildcard": {"process_path.keyword": "*\\\\net.exe"}}, {"wildcard": {"process_path.keyword": "*\\\\net1.exe"}}]}}, {"bool": {"should": [{"wildcard": {"process_command_line.keyword": "* group*"}}, {"wildcard": {"process_command_line.keyword": "* localgroup*"}}, {"wildcard": {"process_command_line.keyword": "* user*"}}, {"wildcard": {"process_command_line.keyword": "* view*"}}, {"wildcard": {"process_command_line.keyword": "* share"}}, {"wildcard": {"process_command_line.keyword": "* accounts*"}}, {"wildcard": {"process_command_line.keyword": "* use*"}}, {"wildcard": {"process_command_line.keyword": "* stop *"}}]}}]}}}}}
tactic = "Discovery"
technique = "Account Discovery"
procedure = "Net.exe Execution"
tech_code = "T1087"
