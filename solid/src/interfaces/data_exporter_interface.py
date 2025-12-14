from abc import ABC, abstractmethod

"""Interface for data parsing """
class DataParser(ABC):
    @abstractmethod
    def data_exporter(self):
        pass
