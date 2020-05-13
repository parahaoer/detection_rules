{"query": {"constant_score": {"filter": {"bool": {"must": [{"match_phrase": {"event_id": "10"}}, {"match_phrase": {"process_target_path": "C:\\windows\\system32\\lsass.exe"}}, {"match_phrase": {"process_granted_access": "2097151"}}, {"bool": {"should": [{"wildcard": {"process_call_trace.keyword": "*dbghelp.DLL*"}}, {"wildcard": {"process_call_trace.keyword": "*dbgcore.DLL*"}}]}}]}}}}}
tactic = "Credential Access"
technique = "Credential Dumping"
procedure = "LSASS Memory Dump"
tech_code = "T1003"
