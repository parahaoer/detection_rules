{"query": {"bool": {"must": [{"match": {"event_id": "10"}}, {"match": {"process_name": "wsmprovhost.exe"}}, {"wildcard": {"process_target_path.keyword": "*\\\\*.exe"}}]}}}
tactic = "Execution"
technique = "Windows Remote Management"
procedure = "WMIC Process Call Create"
tech_code = "T1028"
