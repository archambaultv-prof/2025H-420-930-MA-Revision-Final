
from abc import ABC, abstractmethod

class Produit:
    def __init__(self, nom, prix, type_produit):
        self.nom = nom
        self.prix = prix
        self.type_produit = type_produit

class Client:
    def __init__(self, nom, type_client):
        self.nom = nom
        self.type_client = type_client

# ======================
# Strategies
# ======================
class RemiseStrategy(ABC):
    @abstractmethod
    def calculer(self, montant: float) -> float:
        ...

class PointsFideliteStrategy(ABC):
    @abstractmethod
    def calculer(self, montant: float) -> int:
        ...

# Implémentations concrètes
class RemisePourcentage(RemiseStrategy):
    def __init__(self, taux: float):
        self.taux = taux

    def calculer(self, montant: float) -> float:
        return montant * self.taux

class PointsParTranche(PointsFideliteStrategy):
    def __init__(self, tranche: float):
        self.tranche = tranche

    def calculer(self, montant: float) -> int:
        if self.tranche <= 0:
            return 0
        return int(montant // self.tranche)

# ======================
# Abstract Factory
# ======================
class ClientPricingFactory(ABC):
    @abstractmethod
    def create_remise_strategy(self) -> RemiseStrategy:
        ...
    
    @abstractmethod
    def create_points_strategy(self) -> PointsFideliteStrategy:
        ...

# Fabriques concrètes
class PremiumClientFactory(ClientPricingFactory):
    def create_remise_strategy(self) -> RemiseStrategy:
        return RemisePourcentage(0.20)
    def create_points_strategy(self) -> PointsFideliteStrategy:
        return PointsParTranche(10)

class EntrepriseClientFactory(ClientPricingFactory):
    def create_remise_strategy(self) -> RemiseStrategy:
        return RemisePourcentage(0.15)
    def create_points_strategy(self) -> PointsFideliteStrategy:
        return PointsParTranche(20)

class StandardClientFactory(ClientPricingFactory):
    def create_remise_strategy(self) -> RemiseStrategy:
        return RemisePourcentage(0.05)
    def create_points_strategy(self) -> PointsFideliteStrategy:
        return PointsParTranche(50)

# ======================
# Choix de la fabrique
# ======================
FACTORIES = {
    "premium": PremiumClientFactory(),
    "entreprise": EntrepriseClientFactory(),
    "standard": StandardClientFactory(),
}

def get_factory(type_client: str) -> ClientPricingFactory:
    return FACTORIES.get(type_client, StandardClientFactory())

# ======================
# Calculateur
# ======================
class CalculateurPrix:
    def __init__(self):
        self.frais_livraison = {
            "livre": 5.99,
            "electronique": 12.99,
            "vetement": 6.99,
        }
        self.frais_par_defaut = 7.99

    def _frais_livraison(self, type_produit):
        return self.frais_livraison.get(type_produit, self.frais_par_defaut)

    def calculer(self, produit: Produit, client: Client):
        factory = get_factory(client.type_client)
        remise_strategy = factory.create_remise_strategy()
        points_strategy = factory.create_points_strategy()

        prix_base = produit.prix
        remise = remise_strategy.calculer(prix_base)
        prix_apres_remise = prix_base - remise
        points = points_strategy.calculer(prix_base)
        livraison = self._frais_livraison(produit.type_produit)
        prix_final = prix_apres_remise + livraison

        return {
            "produit": produit.nom,
            "client": client.nom,
            "type_client": client.type_client,
            "prix_base": prix_base,
            "remise": remise,
            "prix_apres_remise": prix_apres_remise,
            "points": points,
            "livraison": livraison,
            "prix_final": prix_final,
        }

    def afficher(self, produit: Produit, client: Client):
        details = self.calculer(produit, client)
        print(f"🧮 Calcul pour {details['produit']} - {details['client']} ({details['type_client']})")
        print(f"   Prix de base: {details['prix_base']:.2f}")
        print(f"   Remise: -{details['remise']:.2f}")
        print(f"   Points fidélité gagnés: {details['points']}")
        print(f"   Livraison: +{details['livraison']:.2f}")
        print(f"   💵 Prix final: {details['prix_final']:.2f}")

# ======================
# Démo / simple test
# ======================

def demo():
    calculateur = CalculateurPrix()
    livre = Produit("Python Guide", 29.99, "livre")
    smartphone = Produit("Smartphone", 599.99, "electronique")

    client_premium = Client("Jean Dupont", "premium")
    client_entreprise = Client("Marie Tremblay", "entreprise")
    client_standard = Client("John Smith", "standard")

    print("=" * 50)
    print(" DÉMONSTRATION CALCULATEUR ")
    print("=" * 50)
    calculateur.afficher(livre, client_premium)
    print()
    calculateur.afficher(smartphone, client_entreprise)
    print()
    calculateur.afficher(smartphone, client_standard)

if __name__ == "__main__":  # pragma: no cover
    demo()
