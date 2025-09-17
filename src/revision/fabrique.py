from abc import ABC, abstractmethod
from revision.strategiePointsFidelite import StrategiePointsFidelite, PointsPremium, PointsEntreprise, PointsStandard
from revision.strategieRemise import StrategieRemise, RemisePremium, RemiseEntreprise, RemiseStandard

from revision.strategiePointsFidelite import PointsZero
from revision.strategieRemise import RemiseZero

class FabriqueClient(ABC):
    @abstractmethod
    def creer_strategie_remise(self) -> StrategieRemise:
        pass

    @abstractmethod
    def creer_strategie_points(self) -> StrategiePointsFidelite:
        pass


class FabriquePremium(FabriqueClient):
    def __str__(self):
        return "premium"

    def creer_strategie_remise(self) -> StrategieRemise:
        return RemisePremium()

    def creer_strategie_points(self) -> StrategiePointsFidelite:
        return PointsPremium()


class FabriqueEntreprise(FabriqueClient):
    def __str__(self):
        return "entreprise"
    
    def creer_strategie_remise(self) -> StrategieRemise:
        return RemiseEntreprise()

    def creer_strategie_points(self) -> StrategiePointsFidelite:
        return PointsEntreprise()


class FabriqueStandard(FabriqueClient):
    def __str__(self):
        return "standard"
    
    def creer_strategie_remise(self) -> StrategieRemise:
        return RemiseStandard()

    def creer_strategie_points(self) -> StrategiePointsFidelite:
        return PointsStandard()

# L'ajout d'un nouveau type de client
class FabriqueZero(FabriqueClient):
    def __str__(self):
        return "zero"
    
    def creer_strategie_remise(self) -> StrategieRemise:
        return RemiseZero()

    def creer_strategie_points(self) -> StrategiePointsFidelite:
        return PointsZero()