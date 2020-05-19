{"query": {"constant_score": {"filter": {"bool": {"must": [{"match_phrase": {"event_id": "13"}}, {"bool": {"should": [{"wildcard": {"registry_key_path.keyword": "*\\\\SOFTWARE\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\\\\AppCompatFlags\\\\Custom\\\\*"}}, {"wildcard": {"registry_key_path.keyword": "*\\\\SOFTWARE\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\\\\AppCompatFlags\\\\InstalledSDB\\\\*"}}]}}, {"match_phrase": {"event_type": "SetValue"}}]}}}}}
tactic = "Persistence"
technique = "Application Shimming"
procedure = "Registry key creation and/or modification events for SDB"
tech_code = "T1138"
