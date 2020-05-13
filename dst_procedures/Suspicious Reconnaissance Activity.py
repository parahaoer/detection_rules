{"query": {"constant_score": {"filter": {"bool": {"should": [{"match_phrase": {"param3": "net group \"domain admins\" /domain"}}, {"match_phrase": {"param3": "net localgroup administrators"}}]}}}}}
tactic = "Discovery"
technique = "Permission Groups Discovery"
procedure = "Suspicious Reconnaissance Activity"
tech_code = "T1069"
