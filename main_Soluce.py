from abc import ABC, abstractmethod
from typing import Dict, Protocol



class Produit:   
    def __init__(self, nom: str, prix: float, type_produit: str):
        self.nom = nom
        self.prix = prix
        self.type_produit = type_produit


class Client:
    def __init__(self, nom: str, type_client: str):
        self.nom = nom
        self.type_client = type_client


# =============================================================================
# STRATEGY PATTERN - Interfaces abstraites
# =============================================================================

class StrategieRemise(Protocol):
    """Interface pour les stratégies de remise"""
    def calculer_remise(self, prix_base: float) -> float:
        """Calcule la remise à appliquer"""
        ...


class StrategiePointsFidelite(Protocol):
    """Interface pour les stratégies de points de fidélité"""
    def calculer_points(self, prix_base: float) -> int:
        """Calcule les points de fidélité à accorder"""
        ...


# =============================================================================
# STRATEGY PATTERN - Implémentations concrètes
# =============================================================================

class RemisePremium:
    """Stratégie de remise pour les clients premium (20%)"""
    def calculer_remise(self, prix_base: float) -> float:
        return prix_base * 0.20


class RemiseEntreprise:
    """Stratégie de remise pour les clients entreprise (15%)"""
    def calculer_remise(self, prix_base: float) -> float:
        return prix_base * 0.15


class RemiseStandard:
    """Stratégie de remise pour les clients standard (5%)"""
    def calculer_remise(self, prix_base: float) -> float:
        return prix_base * 0.05


class PointsPremium:
    """Stratégie de points pour les clients premium (1 point par 10$ dépensés)"""
    def calculer_points(self, prix_base: float) -> int:
        return int(prix_base // 10)


class PointsEntreprise:
    """Stratégie de points pour les clients entreprise (1 point par 20$ dépensés)"""
    def calculer_points(self, prix_base: float) -> int:
        return int(prix_base // 20)


class PointsStandard:
    """Stratégie de points pour les clients standard (1 point par 50$ dépensés)"""
    def calculer_points(self, prix_base: float) -> int:
        return int(prix_base // 50)


# =============================================================================
# ABSTRACT FACTORY PATTERN
# =============================================================================

class FabriqueStrategiesClient(ABC):
    """Interface abstraite pour la fabrique de stratégies par type de client"""
    
    @abstractmethod
    def creer_strategie_remise(self) -> StrategieRemise:
        """Crée une stratégie de remise appropriée pour ce type de client"""
        pass
    
    @abstractmethod
    def creer_strategie_points(self) -> StrategiePointsFidelite:
        """Crée une stratégie de points de fidélité appropriée pour ce type de client"""
        pass


class FabriqueStrategiesPremium(FabriqueStrategiesClient):
    """Fabrique concrète pour les clients premium"""
    
    def creer_strategie_remise(self) -> StrategieRemise:
        return RemisePremium()
    
    def creer_strategie_points(self) -> StrategiePointsFidelite:
        return PointsPremium()


class FabriqueStrategiesEntreprise(FabriqueStrategiesClient):
    """Fabrique concrète pour les clients entreprise"""
    
    def creer_strategie_remise(self) -> StrategieRemise:
        return RemiseEntreprise()
    
    def creer_strategie_points(self) -> StrategiePointsFidelite:
        return PointsEntreprise()


class FabriqueStrategiesStandard(FabriqueStrategiesClient):
    """Fabrique concrète pour les clients standard"""
    
    def creer_strategie_remise(self) -> StrategieRemise:
        return RemiseStandard()
    
    def creer_strategie_points(self) -> StrategiePointsFidelite:
        return PointsStandard()


# =============================================================================
# REGISTRE POUR L'EXTENSIBILITÉ
# =============================================================================

class RegistreFabriques:
    """Registre centralisé pour gérer les fabriques de stratégies par type de client"""
    
    def __init__(self):
        # Dictionnaire pour un accès O(1) au lieu de recherche linéaire
        self._fabriques: Dict[str, FabriqueStrategiesClient] = {
            "premium": FabriqueStrategiesPremium(),
            "entreprise": FabriqueStrategiesEntreprise(),
            "standard": FabriqueStrategiesStandard()
        }
    
    def obtenir_fabrique(self, type_client: str) -> FabriqueStrategiesClient:
        """Obtient la fabrique appropriée pour un type de client"""
        return self._fabriques.get(type_client, self._fabriques["standard"])
    
    def enregistrer_fabrique(self, type_client: str, fabrique: FabriqueStrategiesClient) -> None:
        """Permet d'ajouter de nouveaux types de clients sans modifier le code existant"""
        self._fabriques[type_client] = fabrique


# =============================================================================
# CLASSE PRINCIPALE REFACTORISÉE
# =============================================================================

class CalculateurPrix:
    """Calculateur de prix refactorisé utilisant les patrons de conception"""
    
    def __init__(self):
        # Structure de données optimisée : dictionnaire pour accès O(1)
        self.frais_livraison: Dict[str, float] = {
            "livre": 5.99,
            "electronique": 12.99,
            "vetement": 6.99
        }
        self.registre_fabriques = RegistreFabriques()
    
    def _obtenir_frais_livraison(self, type_produit: str) -> float:
        """Obtient les frais de livraison avec accès O(1)"""
        return self.frais_livraison.get(type_produit, 7.99)  # Valeur par défaut
    
    def _calculer_remise_et_points(self, prix_base: float, type_client: str) -> tuple[float, int]:
        """Calcule la remise et les points en utilisant les stratégies appropriées"""
        # Obtention de la fabrique appropriée
        fabrique = self.registre_fabriques.obtenir_fabrique(type_client)
        
        # Création des stratégies cohérentes
        strategie_remise = fabrique.creer_strategie_remise()
        strategie_points = fabrique.creer_strategie_points()
        
        # Calculs délégués aux stratégies
        remise = strategie_remise.calculer_remise(prix_base)
        points = strategie_points.calculer_points(prix_base)
        
        return remise, points
    
    def afficher_prix_final(self, produit: Produit, client: Client) -> None:
        """Affiche le calcul de prix final en utilisant les patrons de conception"""
        print(f"🧮 Calcul pour {produit.nom} - {client.nom} ({client.type_client})")
        
        prix_base = produit.prix
        print(f"   Prix de base: {prix_base:.2f}")
        
        # Calcul de la remise et des points via les stratégies
        remise, points_fidelite = self._calculer_remise_et_points(prix_base, client.type_client)
        
        # Application de la remise
        prix_apres_remise = prix_base - remise
        print(f"   Remise {client.type_client}: -{remise:.2f}")
        print(f"   Points fidélité gagnés: {points_fidelite}")
        
        # Application des frais de livraison
        frais_livraison = self._obtenir_frais_livraison(produit.type_produit)
        prix_final = prix_apres_remise + frais_livraison
        print(f"   Livraison: +{frais_livraison:.2f}")
        print(f"   💵 Prix final: {prix_final:.2f}")



def main():
    """Démonstration du calculateur refactorisé"""
    print("=" * 50)
    print(" DÉMONSTRATION CALCULATEUR REFACTORISÉ ")
    print("=" * 50)
    
    # Initialisation
    calculateur = CalculateurPrix()
    
    # Création de produits
    livre = Produit("Python Guide", 29.99, "livre")
    smartphone = Produit("Smartphone", 599.99, "electronique")
    tshirt = Produit("T-shirt", 19.99, "vetement")
    
    # Création de clients
    client_fr = Client("Jean Dupont", "premium")
    client_ca = Client("Marie Tremblay", "entreprise")
    client_us = Client("John Smith", "standard")
    
    # Tests de calculs
    print("📚 Test 1: Livre - Client premium")
    calculateur.afficher_prix_final(livre, client_fr)

    print("\n📱 Test 2: Smartphone - Client entreprise")
    calculateur.afficher_prix_final(smartphone, client_ca)

    print("\n👕 Test 3: T-shirt - Client standard")
    calculateur.afficher_prix_final(tshirt, client_us)
    
    print("\n" + "=" * 50)
    print(" DÉMONSTRATION EXTENSIBILITÉ ")
    print("=" * 50)
    
    # Démonstration de l'extensibilité : ajout d'un nouveau type de client
    class RemiseVIP:
        def calculer_remise(self, prix_base: float) -> float:
            return prix_base * 0.30  # 30% de remise
    
    class PointsVIP:
        def calculer_points(self, prix_base: float) -> int:
            return int(prix_base // 5)  # 1 point par 5$ dépensés
    
    class FabriqueStrategiesVIP(FabriqueStrategiesClient):
        def creer_strategie_remise(self) -> StrategieRemise:
            return RemiseVIP()
        
        def creer_strategie_points(self) -> StrategiePointsFidelite:
            return PointsVIP()
    
    # Enregistrement du nouveau type de client
    calculateur.registre_fabriques.enregistrer_fabrique("vip", FabriqueStrategiesVIP())
    
    # Test avec le nouveau type de client
    client_vip = Client("VIP Client", "vip")
    print("💎 Test 4: Smartphone - Client VIP (nouveau type)")
    calculateur.afficher_prix_final(smartphone, client_vip)


if __name__ == "__main__":
    main()
