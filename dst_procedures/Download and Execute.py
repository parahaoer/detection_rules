{"query": {"constant_score": {"filter": {"bool": {"should": [{"bool": {"must": [{"bool": {"should": [{"wildcard": {"process_path.keyword": "*\\\\bitsadmin.exe"}}]}}, {"bool": {"should": [{"wildcard": {"process_command_line.keyword": "* /transfer *"}}]}}]}}, {"bool": {"should": [{"wildcard": {"process_command_line.keyword": "*copy bitsadmin.exe*"}}]}}]}}}}}
tactic = "Persistence"
technique = "BITS Jobs"
procedure = "Download & Execute"
tech_code = "T1197"
