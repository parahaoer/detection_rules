{"query": {"constant_score": {"filter": {"bool": {"must": [{"match_phrase": {"event_id": "4624"}}, {"match_phrase": {"logon_type": "9"}}, {"match_phrase": {"logon_process_name": "seclogo"}}, {"match_phrase": {"logon_authentication_package_name": "Negotiate"}}]}}}}}
tactic = "Lateral Movement"
technique = "Pass the Hash"
procedure = "Successful Overpass the Hash Attempt"
tech_code = "T1075"
