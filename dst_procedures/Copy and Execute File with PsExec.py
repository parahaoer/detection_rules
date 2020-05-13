{"query": {"constant_score": {"filter": {"bool": {"must": [{"bool": {"must": [{"match_phrase": {"event_id": "5140"}}, {"match_phrase": {"share_name": "Admin$"}}]}}, {"bool": {"must_not": [{"bool": {"must": [{"wildcard": {"user_name.keyword": "*$"}}]}}]}}]}}}}}
tactic = "Lateral Movement"
technique = "Windows Admin Shares"
procedure = "Copy and Execute File with PsExec"
tech_code = "T1077"
