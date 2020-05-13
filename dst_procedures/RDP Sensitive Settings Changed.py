{"query": {"constant_score": {"filter": {"bool": {"must": [{"match_phrase": {"event_id": "13"}}, {"bool": {"should": [{"wildcard": {"registry_key_path.keyword": "*\\\\services\\\\TermService\\\\Parameters\\\\ServiceDll*"}}, {"wildcard": {"registry_key_path.keyword": "*\\\\Control\\\\Terminal Server\\\\fSingleSessionPerUser*"}}, {"wildcard": {"registry_key_path.keyword": "*\\\\Control\\\\Terminal Server\\\\fDenyTSConnections*"}}]}}]}}}}}
tactic = "Defense Evasion"
technique = "Modify Registry"
procedure = "RDP Sensitive Settings Changed"
tech_code = "T1112"
