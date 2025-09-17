from abc import ABC, abstractmethod

class StrategiePointsFidelite(ABC):
    @abstractmethod
    def calculer(self, prix: float) -> int:
        pass

class PointsPremium(StrategiePointsFidelite):
    def calculer(self, prix: float) -> int:
        return int(prix // 10)

class PointsEntreprise(StrategiePointsFidelite):
    def calculer(self, prix: float) -> int:
        return int(prix // 20)

class PointsStandard(StrategiePointsFidelite):
    def calculer(self, prix: float) -> int:
        return int(prix // 50)

# L'ajout d'un nouveau type de client
class PointsZero(StrategiePointsFidelite):
    def calculer(self, prix: float) -> int:
        return int(prix // 5)