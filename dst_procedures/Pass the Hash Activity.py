{"query": {"constant_score": {"filter": {"bool": {"must": [{"bool": {"must": [{"match_phrase": {"logon_type": "3"}}, {"match_phrase": {"logon_process_name": "ntlmssp"}}, {"bool": {"should": [{"match_phrase": {"event_id": "4624"}}, {"match_phrase": {"event_id": "4625"}}]}}]}}]}}}}}
tactic = "Lateral Movement"
technique = "Pass the Hash"
procedure = "Pass the Hash Activity"
tech_code = "T1175"
