{"query": {"constant_score": {"filter": {"bool": {"should": [{"bool": {"must": [{"match_phrase": {"event_id": "13"}}, {"wildcard": {"registry_key_path.keyword": "HKU\\\\*\\\\mscfile\\\\shell\\\\open\\\\command\\\\*"}}]}}, {"bool": {"must": [{"bool": {"must": [{"match_phrase": {"event_id": "1"}}, {"wildcard": {"process_parent_path.keyword": "*\\\\eventvwr.exe"}}]}}, {"bool": {"must_not": [{"bool": {"must": [{"wildcard": {"process_path.keyword": "*\\\\mmc.exe"}}]}}]}}]}}]}}}}}
tactic = "Privilege Escalation"
technique = "Bypass User Account Control"
procedure = "Bypass UAC using Event Viewer"
tech_code = "T1088"
