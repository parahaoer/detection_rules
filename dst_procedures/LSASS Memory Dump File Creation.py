{"query": {"constant_score": {"filter": {"bool": {"must": [{"match_phrase": {"event_id": "11"}}, {"wildcard": {"file_name.keyword": "*lsass*"}}, {"wildcard": {"file_name.keyword": "*dmp"}}]}}}}}
tactic = "Credential Access"
technique = "Credential Dumping"
procedure = "LSASS Memory Dump File Creation"
tech_code = "T1003"
