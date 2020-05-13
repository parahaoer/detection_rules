{"query": {"constant_score": {"filter": {"bool": {"must": [{"match_phrase": {"event_id": "10"}}, {"match_phrase": {"process_target_path": "C:\\windows\\system32\\lsass.exe"}}, {"match_phrase": {"process_granted_access": "4112"}}, {"bool": {"must_not": [{"bool": {"must": [{"bool": {"should": [{"wildcard": {"process_path.keyword": "*\\\\wmiprvse.exe"}}, {"wildcard": {"process_path.keyword": "*\\\\taskmgr.exe"}}, {"wildcard": {"process_path.keyword": "*\\\\procexp64.exe"}}, {"wildcard": {"process_path.keyword": "*\\\\procexp.exe"}}, {"wildcard": {"process_path.keyword": "*\\\\lsm.exe"}}, {"wildcard": {"process_path.keyword": "*\\\\csrss.exe"}}, {"wildcard": {"process_path.keyword": "*\\\\wininit.exe"}}, {"wildcard": {"process_path.keyword": "*\\\\vmtoolsd.exe"}}]}}]}}]}}]}}}}}
tactic = "Credential Access"
technique = "Credential Dumping"
procedure = "Mimikatz Detection LSASS Access"
tech_code = "T1003"
