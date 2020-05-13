{"query": {"constant_score": {"filter": {"bool": {"must": [{"match_phrase": {"event_id": "13"}}, {"bool": {"should": [{"wildcard": {"registry_key_path.keyword": "*\\\\CurrentControlSet\\\\Control\\\\Terminal Server\\\\WinStations\\\\RDP-Tcp\\\\UserAuthentication"}}, {"wildcard": {"registry_key_path.keyword": "*\\\\CurrentControlSet\\\\Control\\\\Terminal Server\\\\fDenyTSConnections"}}]}}, {"match_phrase": {"registry_key_value": "DWORD (0x00000000)"}}]}}}}}
tactic = "Defense Evasion"
technique = "Modify Registry"
procedure = "RDP Registry Modification"
tech_code = "T1112"
