{"query": {"constant_score": {"filter": {"bool": {"should": [{"bool": {"should": [{"wildcard": {"param3.keyword": "*DumpCreds*"}}, {"wildcard": {"param3.keyword": "*invoke-mimikatz*"}}]}}, {"bool": {"must": [{"bool": {"should": [{"wildcard": {"param3.keyword": "*rpc*"}}, {"wildcard": {"param3.keyword": "*token*"}}, {"wildcard": {"param3.keyword": "*crypto*"}}, {"wildcard": {"param3.keyword": "*dpapi*"}}, {"wildcard": {"param3.keyword": "*sekurlsa*"}}, {"wildcard": {"param3.keyword": "*kerberos*"}}, {"wildcard": {"param3.keyword": "*lsadump*"}}, {"wildcard": {"param3.keyword": "*privilege*"}}, {"wildcard": {"param3.keyword": "*process*"}}]}}, {"bool": {"should": [{"wildcard": {"param3.keyword": "*::*"}}]}}]}}]}}}}}
tactic = "Credential Access"
technique = "Credential Dumping"
procedure = "Mimikatz Command Line"
tech_code = "T1003"
