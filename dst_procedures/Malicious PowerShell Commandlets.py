{"query": {"constant_score": {"filter": {"bool": {"should": [{"match": {"powershell.command.name": "Invoke-PsExec"}}, {"match": {"param3": "*Invoke-DllInjection*"}}]}}}}}
tactic = "Execution"
technique = "PowerShell"
procedure = "Malicious PowerShell Commandlets"
tech_code = "T1086"
