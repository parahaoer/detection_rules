{"query": {"constant_score": {"filter": {"bool": {"must": [{"match_phrase": {"event_id": "11"}}, {"bool": {"should": [{"bool": {"must": [{"wildcard": {"file_name.keyword": "*\\\\inetpub\\\\wwwroot\\\\*"}}, {"bool": {"should": [{"wildcard": {"file_name.keyword": "*.asp*"}}, {"wildcard": {"file_name.keyword": "*.ashx*"}}, {"wildcard": {"file_name.keyword": "*.ph*"}}]}}]}}, {"bool": {"must": [{"bool": {"should": [{"wildcard": {"file_name.keyword": "*\\\\www\\\\*"}}, {"wildcard": {"file_name.keyword": "*\\\\htdocs\\\\*"}}, {"wildcard": {"file_name.keyword": "*\\\\html\\\\*"}}]}}, {"wildcard": {"file_name.keyword": "*.ph*"}}]}}, {"bool": {"must": [{"wildcard": {"file_name.keyword": "*\\\\*"}}, {"wildcard": {"file_name.keyword": "*.jsp*"}}]}}, {"bool": {"must": [{"wildcard": {"file_name.keyword": "*\\\\cgi-bin\\\\*"}}, {"wildcard": {"file_name.keyword": "*.pl*"}}]}}]}}]}}}}}
tactic = "Persistence"
technique = "Web Shell"
procedure = "Web Shell Written to Disk"
tech_code = "T1100"
