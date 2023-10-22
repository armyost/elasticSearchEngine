import logging
import os

from flask import (Flask, g, jsonify, request)

from application.exceptions import WrongFileStructureException
from application.services import (ImportBackdataService, SearchEngineService)
from controller.exceptions import BadRequestException
from controller.utils import (filter_data_consistency)
from infrastructure.elastic_search import (init_es_engine, es_connect)
from infrastructure.repositories import (SearchRepository)

###################################### Configuration ########################################

app = Flask(__name__)

def get_es_connection(app):
    if 'es_con' not in g:
        es_engine = app.config.get('ES_ENGINE', None) or init_es_engine()
        g.es_con = es_connect(es_engine)
    return g.es_con

@app.errorhandler(BadRequestException)
@app.errorhandler(WrongFileStructureException)
def handle_bad_request(error):
    response = jsonify(error.to_dict())
    response.status_code = 400
    return response

###################################### View Area Start ########################################

@app.route("/ping", methods=['GET'])
def ping():
    return "pong"

@app.route("/importSourceData2Es", methods=['GET', 'POST'])
def importSourceData2Es():
    if request.method == 'POST':
        return jsonify({'status': 'alive!'})
    return ImportBackdataService.importSourceDatas2ES(get_es_connection(app))

@app.route("/searchByKeyword", methods=['GET', 'POST'])
def searchByKeyword():
    if request.method == 'GET':
        return jsonify({'status': 'alive!'})
    searchInfo = filter_data_consistency(request, "keyword")
    keyword = searchInfo['keyword']
    repository=SearchRepository(get_es_connection(app))
    return jsonify(SearchEngineService.searchByKeyword(repository, keyword))

###################################### View Area End ########################################

if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0', port=5001)
    # app.run(host=os.getenv('HOST'), port=os.getenv('PORT'))