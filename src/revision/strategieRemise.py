from abc import ABC, abstractmethod

class StrategieRemise(ABC):
    @abstractmethod
    def calculer(self, prix: float) -> float:
        pass

class RemisePremium(StrategieRemise):
    def calculer(self, prix: float) -> float:
        return prix * 0.20

class RemiseEntreprise(StrategieRemise):
    def calculer(self, prix: float) -> float:
        return prix * 0.15

class RemiseStandard(StrategieRemise):
    def calculer(self, prix: float) -> float:
        return prix * 0.05

# L'ajout d'un nouveau type de client
class RemiseZero(StrategieRemise):
    def calculer(self, prix: float) -> float:
        return prix * 0.50