{"query": {"constant_score": {"filter": {"bool": {"must": [{"wildcard": {"process_path.keyword": "*\\\\reg.exe"}}, {"bool": {"should": [{"wildcard": {"process_command_line.keyword": "*save*"}}, {"wildcard": {"process_command_line.keyword": "*export*"}}]}}, {"bool": {"should": [{"wildcard": {"process_command_line.keyword": "*hklm*"}}, {"wildcard": {"process_command_line.keyword": "*hkey_local_machine*"}}]}}, {"bool": {"should": [{"wildcard": {"process_command_line.keyword": "*\\system"}}, {"wildcard": {"process_command_line.keyword": "*\\sam"}}, {"wildcard": {"process_command_line.keyword": "*\\security"}}]}}]}}}}}
tactic = "Credential Access"
technique = "Credential Dumping"
procedure = "Grabbing Sensitive Hives via Reg Utility"
tech_code = "T1003"
