from domain.repositories import (BaseEsRepository, SearchRepositoryInterface)

class searchRepository(BaseEsRepository, SearchRepositoryInterface):

    def selectWithKeyword(self, keyword):
        with self.es_connection as es_con:
            docs = es_con.search(index='dictionary',
                                    doc_type='dictionary_datas',
                                    body={
                                        "query": {
                                            "match": {
                                                "query": keyword,
                                                "fields": "class_name"
                                            }
                                        }
                                    })
            searchDataList = docs['hits']
            ## Search 객체에 담는것도 생각해볼 필요 있음
            return searchDataList