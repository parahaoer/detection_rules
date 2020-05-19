{"query": {"constant_score": {"filter": {"bool": {"must": [{"bool": {"should": [{"wildcard": {"process_path.keyword": "*\\\\sdbinst.exe"}}]}}, {"bool": {"should": [{"wildcard": {"process_command_line.keyword": "*.sdb*"}}]}}]}}}}}
tactic = "Persistence"
technique = "Application Shimming"
procedure = "Application Shim Installation"
tech_code = "T1138"
