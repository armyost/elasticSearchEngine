from abc import (
    ABCMeta,
    abstractmethod
)

class SearchRepositoryInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def selectWithKeyword(self, keyword):
        pass
