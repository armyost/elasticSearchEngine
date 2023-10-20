class BaseEsRepository():

    def __init__(self, es_connection):
        self.db_connection = es_connection
