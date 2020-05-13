{"query": {"constant_score": {"filter": {"bool": {"must": [{"bool": {"should": [{"wildcard": {"process_parent_path.keyword": "*\\\\wmiprvse.exe"}}]}}, {"bool": {"should": [{"wildcard": {"process_path.keyword": "*\\\\powershell.exe"}}]}}]}}}}}
tactic = "Execution"
technique = "Scripting"
procedure = "WMI Spawning Windows PowerShell"
tech_code = "T1064"
