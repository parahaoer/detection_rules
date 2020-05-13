{"query": {"constant_score": {"filter": {"bool": {"must": [{"match_phrase": {"event_id": "12"}}, {"match_phrase": {"registry_key_path": "HKU\\*"}}, {"wildcard": {"registry_key_path.keyword": "*_Classes\\\\CLSID\\\\*"}}, {"wildcard": {"registry_key_path.keyword": "*\\\\TreatAs"}}]}}}}}
tactic = "Persistence"
technique = "Component Object Model Hijacking"
procedure = "Component Object Model Hijacking"
tech_code = "T1197"
