{"query": {"constant_score": {"filter": {"bool": {"must": [{"bool": {"must": [{"match_phrase": {"event_id": "7"}}, {"bool": {"should": [{"wildcard": {"process_path.keyword": "*\\\\svchost.exe"}}]}}, {"bool": {"should": [{"wildcard": {"module_loaded.keyword": "*\\\\tsmsisrv.dll"}}, {"wildcard": {"module_loaded.keyword": "*\\\\tsvipsrv.dll"}}, {"wildcard": {"module_loaded.keyword": "*\\\\wlbsctrl.dll"}}, {"wildcard": {"module_loaded.keyword": "*\\\\amsi.dll"}}]}}]}}, {"bool": {"must_not": [{"bool": {"must": [{"match_phrase": {"event_id": "7"}}, {"bool": {"should": [{"wildcard": {"process_path.keyword": "*\\\\svchost.exe"}}]}}, {"bool": {"should": [{"match_phrase": {"module_loaded": "C:\\Windows\\WinSxS\\*"}}]}}]}}]}}]}}}}}
tactic = "Persistence"
technique = "DLL Search Order Hijacking"
procedure = "DLL Search Order Hijacking-amsi.dll"
tech_code = "T1038"
