{"query": {"constant_score": {"filter": {"bool": {"should": [{"match_phrase": {"param3": "* -NoP -sta -NonI -W Hidden -Enc *"}}, {"match_phrase": {"param3": "* -noP -sta -w 1 -enc *"}}, {"match_phrase": {"param3": "* -NoP -NonI -W Hidden -enc *"}}]}}}}}
tactic = "Execution"
technique = "PowerShell"
procedure = "Detects suspicious powershell command line parameters used in Empire"
tech_code = "T1086"
