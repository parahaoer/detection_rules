{"query": {"constant_score": {"filter": {"bool": {"must": [{"bool": {"should": [{"match_phrase": {"event_id": "4103"}}, {"match_phrase": {"event_id": "400"}}]}}, {"match": {"powershell.host.name": "ServerRemoteHost"}}, {"match": {"powershell.host.application": "wsmprovhost.exe"}}]}}}}}
tactic = "Execution"
technique = "PowerShell"
procedure = "Remote PowerShell Session"
tech_code = "T1086"
