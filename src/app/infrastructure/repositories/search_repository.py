from domain.repositories import (BaseEsRepository, SearchRepositoryInterface)

class searchRepository(BaseEsRepository, SearchRepositoryInterface):

    def selectWithKeyword(self, keyword):
        with self.es_connection as es_con:
            docs = es_con.search(index='dictionary',
                                    doc_type='dictionary_datas',
                                    body={
                                        "query": {
                                            "multi_match": {
                                                "query": keyword,
                                                "fields": ["title", "content"]
                                            }
                                        }
                                    })
 
            searchDataList = docs['hits']
            return searchDataList