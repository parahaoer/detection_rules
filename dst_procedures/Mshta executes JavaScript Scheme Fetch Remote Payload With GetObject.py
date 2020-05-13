{"query": {"bool": {"should": [{"bool": {"must": [{"match": {"process_name": "mshta.exe"}}, {"wildcard": {"process_command_line.keyword": "*javascript*"}}]}}, {"bool": {"must": [{"match": {"process_name": "mshta.exe"}}, {"match": {"event_id": "3"}}]}}]}}}
tactic = "Execution"
technique = "Mshta"
procedure = "Mshta executes JavaScript Scheme Fetch Remote Payload With GetObject"
tech_code = "T1170"
