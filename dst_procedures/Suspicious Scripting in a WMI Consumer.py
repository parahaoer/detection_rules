{"query": {"constant_score": {"filter": {"bool": {"must": [{"match_phrase": {"event_id": "20"}}, {"bool": {"should": [{"wildcard": {"wmi_consumer_destination.keyword": "* -Nop *"}}]}}]}}}}}
tactic = "Execution"
technique = "PowerShell"
procedure = "Suspicious Scripting in a WMI Consumer"
tech_code = "T1086"
