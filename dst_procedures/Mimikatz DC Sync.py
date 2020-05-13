{"query": {"constant_score": {"filter": {"bool": {"must": [{"bool": {"must": [{"bool": {"must": [{"match_phrase": {"event_id": "4662"}}, {"bool": {"should": [{"wildcard": {"object_properties.keyword": "*Replicating Directory Changes All*"}}, {"wildcard": {"object_properties.keyword": "*1131f6ad-9c07-11d1-f79f-00c04fc2dcd2*"}}]}}]}}, {"bool": {"must_not": [{"bool": {"must": [{"match_phrase": {"SubjectDomainName": "Window Manager"}}]}}]}}]}}, {"bool": {"must_not": [{"bool": {"must": [{"bool": {"should": [{"wildcard": {"SubjectUserName.keyword": "NT AUTHORITY*"}}, {"wildcard": {"SubjectUserName.keyword": "*$"}}]}}]}}]}}]}}}}}
tactic = "Credential Access"
technique = "Credential Dumping"
procedure = "Mimikatz DC Sync"
tech_code = "T1003"
