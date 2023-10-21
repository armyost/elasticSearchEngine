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



# @app.route("/userAdd", methods=['GET', 'POST'])
# def userAdd():
#     if request.method == 'GET':
#         return jsonify({'status': 'alive!'})
#     userInfo = filter_request_consistency(request, int)
#     # logging.warn(userInfo)
#     repository=UserRepository(get_db_connection(app))
#     return jsonify(UserService.addUser(userInfo['id'], userInfo['description'], userInfo['userName'], userInfo['deptId'], repository))

# @app.route("/deptAdd", methods=['GET', 'POST'])
# def deptAdd():
#     if request.method == 'GET':
#         return jsonify({'status': 'alive!'})
#     deptInfo = filter_request_consistency(request, int)
#     repository=DepartmentRepository(get_db_connection(app))
#     # logging.warn(deptInfo)
#     return jsonify(DepartmentService.addDepartment(deptInfo['id'], deptInfo['description'], deptInfo['deptName'], repository))

# @app.route("/userInfoDetail/<userId>", methods=['GET', 'POST'])
# def userInfoDetail(userId):
#     if request.method == 'POST':
#         return jsonify({'status': 'not accept POST method'})
#     # userInfo = filter_request_consistency(request, int)
#     repository=UserRepository(get_db_connection(app))
#     return jsonify(UserService.detailUser(userId, repository))

# @app.route('/acquire/pdf', methods=['GET', 'POST'])
# def acquire_pdf():
#     if request.method == 'GET':
#         return jsonify({'status': 'alive!'})

#     file = file_by_mimetype(request, 'application/pdf')
#     plain_text = AcquirePdfFile().do(
#         file_content=file.stream.read()
#     )

#     return jsonify({'plain_text': plain_text})


# @app.route('/anonymize/txt', methods=['GET', 'POST'])
# def anonymize_txt():
#     if request.method == 'GET':
#         return jsonify({'status': 'alive!'})

#     file = file_by_mimetype(request, 'text/plain')
#     anonymized_data = AnonymizeTxtFile().do(
#         file_content=file.stream.read().decode("utf-8"),
#         repository=ReportRepository(get_db_connection(app))
#     )

#     return jsonify(anonymized_data)

###################################### View Area End ########################################

if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0', port=5001)
    # app.run(host=os.getenv('HOST'), port=os.getenv('PORT'))