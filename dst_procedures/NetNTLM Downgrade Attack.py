{"query": {"constant_score": {"filter": {"bool": {"must": [{"match_phrase": {"event_id": "13"}}, {"bool": {"should": [{"wildcard": {"registry_key_path.keyword": "*System\\\\*ControlSet*\\\\Control\\\\Lsa\\\\LMCompatibilityLevel"}}, {"wildcard": {"registry_key_path.keyword": "*System\\\\*ControlSet*\\\\Control\\\\Lsa\\\\MSV1_0\\\\NtlmMinClientSec"}}, {"wildcard": {"registry_key_path.keyword": "*System\\\\*ControlSet*\\\\Control\\\\Lsa\\\\MSV1_0\\\\RestrictSendingNTLMTraffic"}}]}}]}}}}}
tactic = "Credential Access"
technique = "Exploitation for Credential Access"
procedure = "NetNTLM Downgrade Attack"
tech_code = "T1212"
