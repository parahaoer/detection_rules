{"query": {"constant_score": {"filter": {"bool": {"should": [{"bool": {"should": [{"bool": {"should": [{"bool": {"must": [{"match_phrase": {"event_id": "4738"}}]}}, {"bool": {"must": [{"match_phrase": {"event_id": "5136"}}, {"match_phrase": {"dsobject_attribute_name": "msDS-AllowedToDelegateTo"}}]}}]}}, {"bool": {"must": [{"match_phrase": {"event_id": "5136"}}, {"match_phrase": {"dsobject_class": "user"}}, {"match_phrase": {"dsobject_attribute_name": "servicePrincipalName"}}]}}]}}, {"bool": {"must": [{"match_phrase": {"event_id": "5136"}}, {"match_phrase": {"dsobject_attribute_name": "msDS-AllowedToActOnBehalfOfOtherIdentity"}}]}}]}}}}}
tactic = "Credential Access"
technique = "Account Manipulation"
procedure = "Admin Account Manipulate"
tech_code = "T1098"
