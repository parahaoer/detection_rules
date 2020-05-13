{"query": {"constant_score": {"filter": {"bool": {"should": [{"bool": {"must": [{"match_phrase": {"event_id": "5861"}}, {"bool": {"should": [{"wildcard": {"Message.keyword": "*ActiveScriptEventConsumer*"}}, {"wildcard": {"Message.keyword": "*CommandLineEventConsumer*"}}, {"wildcard": {"Message.keyword": "*CommandLineTemplate*"}}]}}]}}, {"match_phrase": {"event_id": "5859"}}]}}}}}
tactic = "Execution"
technique = "Windows Management Instrumentation"
procedure = "WMI Persistence"
tech_code = "T1047"
