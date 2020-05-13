from elasticsearch import Elasticsearch
from helk_info import HELK_IP
es = Elasticsearch(HELK_IP + ':9200')

mappings = {
            "mappings": {
                    "properties": {
                        "EventCount": {
                            "type": "long",
                        },
                        "Tactic": {
                            "type": "keyword"
                        },
                        "Technique": {
                            "type": "keyword"
                        },
                        "Procedure": {
                            "type": "keyword"
                        },
                        "Tech_code": {
                            "type": "keyword"
                        }
                    }
                }
            }

res = es.indices.create(index = 'represent_1',body =mappings)
