from domain.repositories import SearchRepositoryInterface
from infrastructure.repositories import BaseEsRepository
from domain.models import Search

class SearchRepository(BaseEsRepository, SearchRepositoryInterface):
    
    def selectWithKeyword(self, keyword):
        searchResults = []

        with self.es_connection as es_con:
            docs = es_con.search(index='dictionary',
                                    body={
                                        "query": {
                                            "match": {
                                                "class_name": keyword
                                            }
                                        }
                                    })
            for searchResult in docs['hits']['hits']:
                id = searchResult['_source']['id']
                price = searchResult['_source']['price']
                imgUrl = searchResult['_source']['img_url']
                className = searchResult['_source']['class_name']
                searchVo = Search(id, price, imgUrl, className)
                searchResults.append(searchVo)
            return searchResults