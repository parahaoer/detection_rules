{"query": {"constant_score": {"filter": {"bool": {"must": [{"match_phrase": {"event_id": "4661"}}, {"bool": {"should": [{"match_phrase": {"object_type": "SAM_USER"}}, {"match_phrase": {"object_type": "SAM_GROUP"}}]}}, {"bool": {"should": [{"wildcard": {"object_name.keyword": "*-512"}}, {"wildcard": {"object_name.keyword": "*-502"}}, {"wildcard": {"object_name.keyword": "*-500"}}, {"wildcard": {"object_name.keyword": "*-505"}}, {"wildcard": {"object_name.keyword": "*-519"}}, {"wildcard": {"object_name.keyword": "*-520"}}, {"wildcard": {"object_name.keyword": "*-544"}}, {"wildcard": {"object_name.keyword": "*-551"}}, {"wildcard": {"object_name.keyword": "*-555"}}, {"wildcard": {"object_name.keyword": "*admin*"}}]}}]}}}}}
tactic = "Discovery"
technique = "Permission Groups Discovery"
procedure = "AD Privileged Users or Groups Reconnaissance"
tech_code = "T1069"
