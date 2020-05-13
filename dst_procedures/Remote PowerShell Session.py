{"query": {"constant_score": {"filter": {"bool": {"must": [{"match_phrase": {"event_id": "5156"}}, {"bool": {"should": [{"match_phrase": {"dst_port": "5985"}}, {"match_phrase": {"dst_port": "5986"}}]}}, {"match_phrase": {"network_layer_id": "44"}}]}}}}}
tactic = "Execution"
technique = "PowerShell"
procedure = "Remote PowerShell Session"
tech_code = "T1086"
