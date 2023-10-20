import logging
from domain.models import Search

class SearchEngineService:

    def searchByKeyword(repository, keyword):
        searchResultDataList = repository.selectWithKeyword(keyword)
        return searchResultDataList
        