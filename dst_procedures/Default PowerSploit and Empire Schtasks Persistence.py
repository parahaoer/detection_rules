{"query": {"constant_score": {"filter": {"bool": {"must": [{"bool": {"should": [{"wildcard": {"process_parent_path.keyword": "*\\\\powershell.exe"}}]}}, {"bool": {"should": [{"wildcard": {"process_command_line.keyword": "*schtasks*/create*/sc *ONLOGON*/TN *Updater*/TR *powershell*"}}, {"wildcard": {"process_command_line.keyword": "*schtasks*/create*/sc *daily*/tn *updater*/tr *powershell*"}}, {"wildcard": {"process_command_line.keyword": "*schtasks*/Create*/SC *ONIDLE*/TN *Updater*/TR *powershell*"}}, {"wildcard": {"process_command_line.keyword": "*schtasks*/Create*/SC *Updater*/TN *Updater*/TR *powershell*"}}]}}]}}}}}
tactic = "Persistence"
technique = "Scheduled Task"
procedure = "Default PowerSploit and Empire Schtasks Persistence"
tech_code = "T1053"
