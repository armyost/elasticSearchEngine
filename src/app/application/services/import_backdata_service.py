import json
import logging
import os

from flask import Response

class ImportBackdataService:
    def importSourceDatas2ES(es_con):
        jsonDataPath = os.path.dirname(__file__)
        filename = os.path.join(jsonDataPath, 'resources/es_backdata.json')
        logging.warn("!!! Import File "+filename+" !!!")
        with open(filename, 'r', encoding='utf-8') as file:
            datas = json.load(file)
            body = ""
            for i in datas['products']:
                body = body + json.dumps({"index": {"_index":"dictionary"}}) + '\n'
                body = body + json.dumps(i, ensure_ascii=False) + '\n'
            es_con.bulk(body)
        return "ImportBackdataService Finish!"