{"query": {"constant_score": {"filter": {"wildcard": {"process_command_line.keyword": "*ntdsutil*"}}}}}
tactic = "Credential Access"
technique = "Credential Dumping"
procedure = "Dump Active Directory Database with NTDSUtil"
tech_code = "T1003"
