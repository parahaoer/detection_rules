{"query": {"constant_score": {"filter": {"bool": {"must": [{"match_phrase": {"event_id": "13"}}, {"match_phrase": {"event_type": "SetValue"}}, {"bool": {"must": [{"wildcard": {"registry_key_path.keyword": "*\\\\Control\\\\SecurityProviders\\\\WDigest\\\\UseLogonCredential"}}, {"match_phrase": {"registry_key_value": "1"}}]}}]}}}}}
tactic = "Defense Evasion"
technique = "Modify Registry"
procedure = "Chafer Activity"
tech_code = "T1112"
