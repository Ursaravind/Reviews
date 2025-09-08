from abc import ABC, abstractmethod

"""Interface for api"""

class Api(ABC):
    @abstractmethod
    def get_data(self):
        pass
