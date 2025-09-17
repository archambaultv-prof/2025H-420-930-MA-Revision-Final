from abc import ABC, abstractmethod

# I FIX YOU  avec PATRON STRATEGY
# Probleme : Calculs de remise dupliquée dans les if/elif
#  il a des clients (premium, entreprise et standard)

class StrategieRemise(ABC):
    @abstractmethod
    def calculer(self, prix_base: float) -> float:
        pass

class RemisePremium(StrategieRemise):
    def calculer(self, prix_base: float) -> float:
        return prix_base * 0.20

class RemiseEntreprise(StrategieRemise):
    def calculer(self, prix_base: float) -> float:
        return prix_base * 0.15

class RemiseStandard(StrategieRemise):
    def calculer(self, prix_base: float) -> float:
        return prix_base * 0.05


# Chaque groupe de clients a son propre calcul de points de fidélité. Je m'interroge sur le fait d'ajouter
# le calcul points_fidelite directement dans la remise ou non.
# Je vais choisir de respecter le principe de responsabilité unique et créer chacun dans leur classe également.

class Points(ABC):
    @abstractmethod
    def calculer(self, prix_base: float) -> int:
        pass

class PointsPremium(Points):
    def calculer(self, prix_base: float) -> int:
        return int(prix_base // 10)

class PointsEntreprise(Points):
    def calculer(self, prix_base: float) -> int:
        return int(prix_base // 20)

class PointsStandard(Points):
    def calculer(self, prix_base: float) -> int:
        return int(prix_base // 50)


# Chacun de nos clients appelle deux classes, donc le multiple choix se passe ici
# On va réellement implémenter l'abstract factory ici avec chaque type de client

class CreateurClient(ABC):
    @abstractmethod
    def remise(self) -> StrategieRemise:
        pass
    
    @abstractmethod
    def points(self) -> Points:
        pass

class Premium(CreateurClient):
    def remise(self) -> StrategieRemise:
        return RemisePremium()
    
    def points(self) -> Points:
        return PointsPremium()

class Entreprise(CreateurClient):
    def remise(self) -> StrategieRemise:
        return RemiseEntreprise()
    
    def points(self) -> Points:
        return PointsEntreprise()

class Standard(CreateurClient):
    def remise(self) -> StrategieRemise:
        return RemiseStandard()
    
    def points(self) -> Points:
        return PointsStandard()