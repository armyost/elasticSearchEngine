from flask import Response
from controller.exceptions import BadRequestException


def file_by_mimetype(request, mimetype):
    if 'file' not in request.files:
        raise BadRequestException({'file': 'mandatory'})
    file = request.files['file']
    if file.mimetype != mimetype:
        raise BadRequestException({'file': 'wrong file type'})

    return file

def filter_request_consistency(request, type):
    if 'id' not in request.json:
        raise BadRequestException({'id': 'mandatory'})
    paramId = request.json['id']
    if isinstance(paramId, type) is False:
        raise BadRequestException({'id': 'wrong data type'})
    return request.json

def filter_data_consistency(request, key):
    if key not in request.json:
        raise BadRequestException({key: 'mandatory'})
        # return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'search word param is missing'})
    return request.json
    