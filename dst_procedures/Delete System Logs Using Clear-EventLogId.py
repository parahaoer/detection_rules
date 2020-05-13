{"query": {"constant_score": {"filter": {"bool": {"must": [{"match_phrase": {"event_id": "104"}}, {"match_phrase": {"source_name": "Microsoft-Windows-Eventlog"}}]}}}}}
tactic = "Defense Evasion"
technique = "Indicator Removal on Host"
procedure = "Delete System Logs Using Clear-EventLogId"
tech_code = "T1070"
