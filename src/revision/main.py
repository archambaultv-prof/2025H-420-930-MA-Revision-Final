from abc import ABC, abstractmethod
class Produit:   
    def __init__(self, nom: str, prix: float, type_produit: str):
        self.nom = nom
        self.prix = prix
        self.type_produit = type_produit


class Client:
    def __init__(self, nom: str, type_client: str):
        self.nom = nom
        self.type_client = type_client

# Strategy Pattern pour les remises
class RemiseStrategy(ABC):
    @abstractmethod
    def calculer_remise(self, prix_base: float) -> float:
        pass

class PremiumRemiseStrategy(RemiseStrategy):
    def calculer_remise(self, prix_base: float) -> float:
        return prix_base * 0.20
    
class EntrepriseRemiseStrategy(RemiseStrategy):
    def calculer_remise(self, prix_base: float) -> float:
        return prix_base * 0.15
    
class StandardRemiseStrategy(RemiseStrategy):
    def calculer_remise(self, prix_base: float) -> float:
        return prix_base * 0.05
    
class PointsFideliteStrategy(ABC):
    @abstractmethod
    def calculer_points_fidelite(self, prix_base: float) -> int:
        pass

# Strategy Pattern pour les points de fidélité
class PremiumPointsFideliteStrategy(PointsFideliteStrategy):
    def calculer_points_fidelite(self, prix_base: float) -> int:
        return int(prix_base // 10)
    
class EntreprisePointsFideliteStrategy(PointsFideliteStrategy):
    def calculer_points_fidelite(self, prix_base: float) -> int:
        return int(prix_base // 20)
    
class StandardPointsFideliteStrategy(PointsFideliteStrategy):
    def calculer_points_fidelite(self, prix_base: float) -> int:
        return int(prix_base // 50)

# Abstract Factory Pattern
class ClientFactory(ABC):
    @abstractmethod
    def creer_strategie_remise(self) -> RemiseStrategy:
        pass
    
    @abstractmethod
    def creer_strategie_points_fidelite(self) -> PointsFideliteStrategy:
        pass
class PremiumFactory(ClientFactory):
    def creer_strategie_remise(self) -> RemiseStrategy:
        return PremiumRemiseStrategy()
    
    def creer_strategie_points_fidelite(self) -> PointsFideliteStrategy:
        return PremiumPointsFideliteStrategy()
class EntrepriseFactory(ClientFactory):
    def creer_strategie_remise(self) -> RemiseStrategy:
        return EntrepriseRemiseStrategy()
    
    def creer_strategie_points_fidelite(self) -> PointsFideliteStrategy:
        return EntreprisePointsFideliteStrategy()
    
class StandardFactory(ClientFactory):
    def creer_strategie_remise(self) -> RemiseStrategy:
        return StandardRemiseStrategy()
    
    def creer_strategie_points_fidelite(self) -> PointsFideliteStrategy:
        return StandardPointsFideliteStrategy()
class CalculateurPrix:
    
    def __init__(self):
        # FIXME: Structures de données inefficaces
        # Utilisation d'un dictionnaire pour une recherche efficace
        self.frais_livraison = {
            "livre": 5.99,
            "electronique": 12.99,
            "vetement": 6.99
        }
        self.factories = {
            "premium": PremiumFactory(),
            "entreprise": EntrepriseFactory(),
            "standard": StandardFactory()
        }

    def _chercher_frais_livraison(self, type_produit: str) -> float:
        # FIXME: Recherche linéaire inefficace
        # Utilisation d'un dictionnaire pour une recherche efficace
        return self.frais_livraison.get(type_produit, 7.99)
    
    def afficher_prix_final(self, produit: Produit, client: Client) -> None:
        # FIXME: Méthode trop longue (fait : ajustements pays, produit, client, taxes, livraison, affichage)
        print(f"🧮 Calcul pour {produit.nom} - {client.nom} ({client.type_client})")
        
        prix_base = produit.prix
        print(f"   Prix de base: {prix_base:.2f}")
        
        ##############################################################
        # Modification du prix selon type de client
        ##############################################################
        # FIXME: Arbre if/elif -> code difficile à étendre
        # Utilisation d'un Abstract Factory Pattern pour une meilleure gestion des types de clients

        # Récupération de la factory appropriéee
        factory = self.factories[client.type_client]


        # Création des stratégies cohérentes via l'Abstract Factory
        strategie_remise = factory.creer_strategie_remise()
        strategie_points = factory.creer_strategie_points_fidelite()

        # Calcul des remises et points de fidélité via les stratégies
        remise = strategie_remise.calculer_remise(prix_base)
        points_fidelite = strategie_points.calculer_points_fidelite(prix_base)

        prix_base -= remise
        print(f"   Remise {client.type_client}: -{remise:.2f}")
        print(f"   Points fidélité gagnés: {points_fidelite}")
        
        ##############################################################
        # Application des taxes et frais de livraison
        ##############################################################
        # FIXME: _chercher_taux inefficace
        # Le corrigé _chercher_frais_livraison utilise un dictionnaire
        frais_livraison = self._chercher_frais_livraison(client.type_client)
        prix_final = prix_base + frais_livraison
        print(f"   Livraison: +{frais_livraison:.2f}")
        print(f"   💵 Prix final: {prix_final:.2f}")


def main():
    """Démonstration du calculateur avec ses défauts"""
    # FIXME: main mélange démonstration et test manuel (pas de tests automatisés fournis)
    print("=" * 50)
    print(" DÉMONSTRATION CALCULATEUR ")
    print("=" * 50)
    
    # Initialisation
    calculateur = CalculateurPrix()
    
    # Création de produits
    livre = Produit("Python Guide", 29.99, "livre")
    smartphone = Produit("Smartphone", 599.99, "electronique")
    
    # Création de clients
    client_fr = Client("Jean Dupont", "premium")
    client_ca = Client("Marie Tremblay", "entreprise")
    client_us = Client("John Smith", "standard")
    
    # Tests de calculs
    print("📚 Test 1: Livre - Client premium")
    calculateur.afficher_prix_final(livre, client_fr)

    print("\n📱 Test 2: Smartphone - Client entreprise")
    calculateur.afficher_prix_final(smartphone, client_ca)

    print("\n📱 Test 3: Smartphone - Client standard")
    calculateur.afficher_prix_final(smartphone, client_us)

if __name__ == "__main__":
    main()