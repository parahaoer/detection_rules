{"query": {"constant_score": {"filter": {"bool": {"should": [{"match_phrase": {"event_id": "517"}}, {"match_phrase": {"event_id": "1102"}}]}}}}}
tactic = "Defense Evasion"
technique = "Indicator Removal on Host"
procedure = "Delete Security Logs Using Clear-EventLogId"
tech_code = "T1070"
