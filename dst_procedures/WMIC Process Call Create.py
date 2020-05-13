{"query": {"bool": {"must": [{"match": {"process_parent_name": "WmiPrvSE.exe"}}]}}}
tactic = "Execution"
technique = "Windows Remote Management"
procedure = "WMIC Process Call Create"
tech_code = "T1028"
