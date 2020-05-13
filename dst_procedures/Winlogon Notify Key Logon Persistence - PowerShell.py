{"query": {"constant_score": {"filter": {"bool": {"must": [{"match_phrase": {"event_id": "4104"}}, {"bool": {"should": [{"multi_match": {"query": "*Set-ItemProperty*", "fields": [], "type": "phrase"}}, {"multi_match": {"query": "*New-Item*", "fields": [], "type": "phrase"}}]}}, {"multi_match": {"query": "*CurrentVersion\\Winlogon*", "fields": [], "type": "phrase"}}]}}}}}
tactic = "Persistence"
technique = "Winlogon Helper DLL"
procedure = "Winlogon Notify Key Logon Persistence - PowerShell"
tech_code = "T1004"
