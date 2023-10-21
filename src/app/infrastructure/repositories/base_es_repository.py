class BaseEsRepository():

    def __init__(self, es_connection):
        self.es_connection = es_connection
