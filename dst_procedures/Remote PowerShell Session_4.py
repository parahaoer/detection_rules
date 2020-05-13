{"query": {"constant_score": {"filter": {"bool": {"should": [{"wildcard": {"process_path.keyword": "*\\\\wsmprovhost.exe"}}, {"wildcard": {"process_parent_path.keyword": "*\\\\wsmprovhost.exe"}}]}}}}}
tactic = "Execution"
technique = "PowerShell"
procedure = "Remote PowerShell Session_4"
tech_code = "T1086"
