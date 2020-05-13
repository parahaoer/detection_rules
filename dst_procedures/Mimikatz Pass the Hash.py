{"query": {"constant_score": {"filter": {"bool": {"must": [{"bool": {"must": [{"match_phrase": {"event_id": "4624"}}, {"bool": {"should": [{"bool": {"must": [{"match_phrase": {"SubjectUserSid": "S-1-0-0"}}, {"match_phrase": {"logon_type": "3"}}, {"match_phrase": {"logon_process_name": "NtLmSsp"}}, {"match_phrase": {"KeyLength": "0"}}]}}, {"bool": {"must": [{"match_phrase": {"logon_type": "9"}}, {"match_phrase": {"logon_process_name": "seclogo"}}]}}]}}]}}, {"bool": {"must_not": [{"bool": {"must": [{"match_phrase": {"user_name": "ANONYMOUS LOGON"}}]}}]}}]}}}}}
tactic = "Lateral Movement"
technique = "Pass the Hash"
procedure = "Mimikatz Pass the Hash"
tech_code = "T1075"
