{"query": {"constant_score": {"filter": {"bool": {"must": [{"bool": {"must": [{"wildcard": {"process_path.keyword": "*\\\\csc.exe"}}, {"bool": {"should": [{"wildcard": {"process_command_line.keyword": "*\\\\AppData\\\\*"}}, {"wildcard": {"process_command_line.keyword": "*\\\\windows\\\\temp\\\\*"}}]}}]}}, {"bool": {"must_not": [{"bool": {"must": [{"bool": {"should": [{"wildcard": {"process_parent_path.keyword": "C:\\\\Program Files*"}}, {"wildcard": {"process_parent_path.keyword": "*\\\\sdiagnhost.exe"}}, {"wildcard": {"process_parent_path.keyword": "*\\\\w3wp.exe"}}]}}]}}]}}]}}}}}
tactic = "Defense Evasion"
technique = "Compile After Delivery"
procedure = "Compile After Delivery using csc.exe"
tech_code = "T1500"
