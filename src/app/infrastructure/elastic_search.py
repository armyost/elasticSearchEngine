import logging
import os
from elasticsearch7 import Elasticsearch

def init_es_engine(es_uri=None):
    uri = "http://elasticsearch.armyost.com:24004/"
    # uri = es_uri or os.getenv('ES_URI')
    es_engine = Elasticsearch(uri, headers={"Content-Type": "application/json"})
    logging.warn("!!! Check ElasticSearch engine !!!")
    __create_index_if_not_exists(es_engine)
    return es_engine

def es_connect(es_engine):
    return es_engine

def close_es_connection(es_connection):
    try:
        es_connection.transport.close()
    except:
        pass

def __create_index_if_not_exists(es_engine):
        if es_engine.indices.exists(index='dictionary'):
            logging.warn("!!! ElasticSearch Index Already Exist !!!")
        else:
            logging.warn("!!! No ElasticSearch Index Exist, So I will create new one !!!")
            response = es_engine.indices.create(
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
