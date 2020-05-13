{"query": {"constant_score": {"filter": {"bool": {"must": [{"wildcard": {"process_parent_path.keyword": "*\\\\mshta.exe"}}, {"bool": {"should": [{"wildcard": {"process_path.keyword": "*\\\\cmd.exe"}}, {"wildcard": {"process_path.keyword": "*\\\\powershell.exe"}}, {"wildcard": {"process_path.keyword": "*\\\\wscript.exe"}}, {"wildcard": {"process_path.keyword": "*\\\\cscript.exe"}}, {"wildcard": {"process_path.keyword": "*\\\\sh.exe"}}, {"wildcard": {"process_path.keyword": "*\\\\bash.exe"}}, {"wildcard": {"process_path.keyword": "*\\\\reg.exe"}}, {"wildcard": {"process_path.keyword": "*\\\\regsvr32.exe"}}, {"wildcard": {"process_path.keyword": "*\\\\BITSADMIN*"}}]}}]}}}}}
tactic = "Execution"
technique = "Mshta"
procedure = "Mshta executes VBScript to execute malicious command"
tech_code = "T1170"
