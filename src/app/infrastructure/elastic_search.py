import logging
from elasticsearch7 import Elasticsearch

def init_es_engine(es_uri=None):
    uri = "http://elasticsearch.armyost.com:24004/"
    logging.warn("!!! Check ElasticSearch engine !!!")
    es = Elasticsearch(uri, headers={"Content-Type": "application/json"})
    if es.indices.exists(index='dictionary'):
        logging.warn("!!! ElasticSearch Index Already Exist !!!")
        return es
    else:
        logging.warn("!!! No ElasticSearch Index Exist, So I will create new one !!!")
        response = es.indices.create(
            index='dictionary',
            body={
                "settings": {
                    "index": {
                        "analysis": {
                            "analyzer": {
                                "nori_token": {
                                    "type": "custom",
                                    "tokenizer": "nori_tokenizer"
                                }
                            }
                        }
                    }
                },
                "mappings": {
                    "properties": {
                        "id": {
                            "type": "integer",
                        },
                        "class_name": {
                            "type": "text",
                            "analyzer": "nori_token"
                        },
                        "price": {
                            "type": "integer",
                        },
                        "img_url": {
                            "type": "text",
                        },
                        "analyze": {
                            "type": "keyword"
                        }
                    }
                }
            }
        )
    return es