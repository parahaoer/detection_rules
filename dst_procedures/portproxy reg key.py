{"query": {"constant_score": {"filter": {"bool": {"must": [{"match": {"process_command_line": " interface portproxy add v4tov4 *"}}, {"match": {"process_name": "netsh.exe"}}]}}}}}
tactic = "Defense Evasion"
technique = "Connection Proxy"
procedure = "portproxy reg key"
tech_code = "T1090"
