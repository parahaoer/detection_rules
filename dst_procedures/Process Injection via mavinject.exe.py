{"query": {"constant_score": {"filter": {"match": {"process_command_line": "* /INJECTRUNNING *"}}}}}
tactic = "Privilege Escalation"
technique = "Process Injection"
procedure = "Process Injection via mavinject.exe"
tech_code = "T1055"
