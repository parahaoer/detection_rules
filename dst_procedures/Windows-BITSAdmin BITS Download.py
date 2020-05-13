{"query": {"constant_score": {"filter": {"bool": {"should": [{"bool": {"must": [{"bool": {"should": [{"wildcard": {"process_path.keyword": "*\\\\bitsadmin.exe"}}]}}, {"bool": {"should": [{"wildcard": {"process_command_line.keyword": "* /transfer *"}}]}}]}}, {"bool": {"should": [{"wildcard": {"process_command_line.keyword": "*copy bitsadmin.exe*"}}]}}]}}}}}
tactic = "Lateral Movement"
technique = "Remote File Copy"
procedure = "Windows-BITSAdmin BITS Download"
tech_code = "T1105"
