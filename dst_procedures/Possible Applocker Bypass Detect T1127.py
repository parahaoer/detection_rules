{"query": {"constant_score": {"filter": {"bool": {"should": [{"wildcard": {"process_command_line.keyword": "*\\\\msdt.exe*"}}, {"wildcard": {"process_command_line.keyword": "*\\\\installutil.exe*"}}, {"wildcard": {"process_command_line.keyword": "*\\\\regsvcs.exe*"}}, {"wildcard": {"process_command_line.keyword": "*\\\\regasm.exe*"}}, {"wildcard": {"process_command_line.keyword": "*\\\\msbuild.exe*"}}, {"wildcard": {"process_command_line.keyword": "*\\\\ieexec.exe*"}}]}}}}}
tactic = "Defense Evasion"
technique = "Trusted Developer Utilities"
procedure = "Possible Applocker Bypass Detect T1127"
tech_code =  "T1127"
