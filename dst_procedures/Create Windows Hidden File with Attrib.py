{"query": {"constant_score": {"filter": {"bool": {"must": [{"bool": {"must": [{"wildcard": {"process_path.keyword": "*\\\\attrib.exe"}}, {"wildcard": {"process_command_line.keyword": "* +h *"}}]}}, {"bool": {"must_not": [{"bool": {"should": [{"wildcard": {"process_command_line.keyword": "*\\\\desktop.ini *"}}, {"bool": {"must": [{"wildcard": {"process_parent_path.keyword": "*\\\\cmd.exe"}}, {"wildcard": {"process_command_line.keyword": "+R +H +S +A \\\\*.cui"}}, {"wildcard": {"process_parent_command_line.keyword": "C:\\\\WINDOWS\\\\system32\\\\*.bat"}}]}}]}}]}}]}}}}}
tactic = "Persistence"
technique = "Hidden Files and Directories"
procedure = "Create Windows Hidden File with Attrib"
tech_code = "T1158"
