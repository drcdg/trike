from abc import ABC, abstractmethod

class Sensor(ABC):
    def __init__(self, decimals: int = None):
        self.decimals = decimals

    @abstractmethod
    def read(self):
        pass

    def round(self, decimals: int):
        self.decimals = decimals

