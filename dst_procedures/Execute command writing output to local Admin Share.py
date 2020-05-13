{"query": {"constant_score": {"filter": {"bool": {"must": [{"bool": {"must": [{"match_phrase": {"event_id": "5140"}}, {"match_phrase": {"share_name": "Admin$"}}]}}, {"bool": {"must_not": [{"bool": {"must": [{"wildcard": {"user_name.keyword": "*$"}}]}}]}}]}}}}}
tactic = "Lateral Movement"
technique = "Windows Admin Shares"
procedure = "Execute command writing output to local Admin Share"
tech_code = "T1077"
