{"query": {"bool": {"must": [{"match": {"event_id": "13"}}, {"wildcard": {"registry_key_path.keyword": "*\\\\ms-settings\\\\shell\\\\open\\\\command\\\\*"}}]}}}
tactic = "Privilege Escalation"
technique = "Bypass User Account Control"
procedure = "Bypass UAC using ComputerDefaults - PowerShell"
tech_code = "T1088"
