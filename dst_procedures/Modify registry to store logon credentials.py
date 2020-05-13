{"query": {"constant_score": {"filter": {"bool": {"must": [{"match_phrase": {"event_id": "13"}}, {"match_phrase": {"event_type": "SetValue"}}, {"bool": {"should": [{"bool": {"should": [{"wildcard": {"registry_key_path.keyword": "*SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\UMe"}}, {"wildcard": {"registry_key_path.keyword": "*SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\UT"}}]}}, {"bool": {"must": [{"wildcard": {"registry_key_path.keyword": "*\\Control\\SecurityProviders\\WDigest\\UseLogonCredential"}}, {"match_phrase": {"registry_key_value": "DWORD (0x00000001)"}}]}}]}}]}}}}}
tactic = "Defense Evasion"
technique = "Modify Registry"
procedure = "Modify registry to store logon credentials"
tech_code = "T1112"
