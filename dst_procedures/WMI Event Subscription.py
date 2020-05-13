{"query": {"constant_score": {"filter": {"bool": {"should": [{"match_phrase": {"event_id": "19"}}, {"match_phrase": {"event_id": "20"}}, {"match_phrase": {"event_id": "21"}}]}}}}}
tactic = "Persistence"
technique = "Windows Management Instrumentation Event Subscription"
procedure = "WMI Event Subscription"
tech_code = "T1084"
