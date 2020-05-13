{"query": {"constant_score": {"filter": {"bool": {"must": [{"bool": {"should": [{"wildcard": {"process_path.keyword": "*\\\\wevtutil.exe"}}, {"match_phrase": {"file_name_original": "wevtutil.exe"}}]}}, {"bool": {"should": [{"wildcard": {"process_command_line.keyword": "* cl *"}}, {"wildcard": {"process_command_line.keyword": "* clear-log *"}}, {"wildcard": {"process_command_line.keyword": "* sl *"}}, {"wildcard": {"process_command_line.keyword": "* set-log *"}}]}}]}}}}}
tactic = "Defense Evasion"
technique = "Indicator Removal on Host"
procedure = "Clear Logs"
tech_code = "T1070"
