{"query": {"constant_score": {"filter": {"bool": {"should": [{"bool": {"must": [{"bool": {"should": [{"wildcard": {"process_command_line.keyword": "* -ma *"}}]}}, {"bool": {"should": [{"wildcard": {"process_command_line.keyword": "* lsass*"}}]}}]}}, {"bool": {"should": [{"wildcard": {"process_command_line.keyword": "* -ma ls*"}}]}}]}}}}}
tactic = "Credential Access"
technique = "Credential Dumping"
procedure = "Dump LSASS.exe Memory using ProcDump"
tech_code = "T1003"
