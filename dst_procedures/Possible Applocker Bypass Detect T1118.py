{"query": {"constant_score": {"filter": {"bool": {"should": [{"wildcard": {"process_command_line.keyword": "*\\\\msdt.exe*"}}, {"wildcard": {"process_command_line.keyword": "*\\\\installutil.exe*"}}, {"wildcard": {"process_command_line.keyword": "*\\\\regsvcs.exe*"}}, {"wildcard": {"process_command_line.keyword": "*\\\\regasm.exe*"}}, {"wildcard": {"process_command_line.keyword": "*\\\\msbuild.exe*"}}, {"wildcard": {"process_command_line.keyword": "*\\\\ieexec.exe*"}}]}}}}}
tactic = "Defense Evasion"
technique = "InstallUtil"
procedure = "Possible Applocker Bypass"
tech_code = "T1118"
