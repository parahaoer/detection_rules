{"query": {"constant_score": {"filter": {"bool": {"should": [{"match_phrase": {"process_command_line": "vssadmin.exe Delete Shadows"}}, {"match_phrase": {"process_command_line": "vssadmin.exe create shadow /for=C:"}}, {"wildcard": {"process_command_line.keyword": "copy \\\\\\\\?\\\\GLOBALROOT\\\\Device\\\\*\\\\windows\\\\ntds\\\\ntds.dit"}}, {"wildcard": {"process_command_line.keyword": "copy \\\\\\\\?\\\\GLOBALROOT\\\\Device\\\\*\\\\config\\\\SAM"}}, {"match_phrase": {"process_command_line": "vssadmin delete shadows /for=C:"}}, {"match_phrase": {"process_command_line": "reg SAVE HKLM\\SYSTEM "}}, {"wildcard": {"process_command_line.keyword": "esentutl.exe /y /vss *\\\\ntds.dit*"}}]}}}}}
tactic = "Credential Access"
technique = "Credential Dumping"
procedure = "Registry dump of SAM, creds, and secrets"
tech_code = "T1003"
