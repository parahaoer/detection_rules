{"query": {"bool": {"must": [{"bool": {"should": [{"wildcard": {"process_parent_path.keyword": "*\\explorer.exe"}}, {"wildcard": {"process_parent_path.keyword": "*\\services.exe"}}, {"wildcard": {"process_parent_path.keyword": "*\\wmiprvse.exe"}}, {"wildcard": {"process_parent_path.keyword": "*\\mmc.exe"}}]}}, {"wildcard": {"process_command_line.keyword": {"value": "*\\cmd.exe* /c*"}}}]}}}
tactic = "Lateral Movement"
technique = "Component Object Model and Distributed COM"
procedure = "Impacket Lateralization Detection"
tech_code = "T1175"
