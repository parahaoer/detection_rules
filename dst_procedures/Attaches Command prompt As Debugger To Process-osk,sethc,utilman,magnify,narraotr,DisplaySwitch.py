{"query": {"constant_score": {"filter": {"bool": {"should": [{"wildcard": {"process_command_line.keyword": "*\\\\currentversion\\\\image file execution options\\\\sethc.exe*"}}, {"wildcard": {"process_command_line.keyword": "*\\\\currentversion\\\\image file execution options\\\\utilman.exe*"}}, {"wildcard": {"process_command_line.keyword": "*\\\\currentversion\\\\image file execution options\\\\osk.exe*"}}, {"wildcard": {"process_command_line.keyword": "*\\\\currentversion\\\\image file execution options\\\\magnify.exe*"}}, {"wildcard": {"process_command_line.keyword": "*\\\\CurrentVersion\\\\Image File Execution Options\\\\narrator.exe*"}}, {"wildcard": {"process_command_line.keyword": "*\\\\currentversion\\\\image file execution options\\\\displayswitch.exe*"}}]}}}}}
tactic = "Persistence"
technique = "Accessibility Features"
procedure = "Attaches Command prompt As Debugger To Process-osk,sethc,utilman,magnify,narraotr,DisplaySwitch"
tech_code = "T1015"
