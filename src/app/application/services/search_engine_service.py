import logging
from domain.models import Search

class SearchEngineService:

    def searchByKeyword(repository, keyword):
        searchResults = repository.selectWithKeyword(keyword)
        return [search.as_dict() for search in searchResults]