
class Produit:   
    def __init__(self, nom: str, prix: float, type_produit: str):
        self.nom = nom
        self.prix = prix
        self.type_produit = type_produit


class Client:
    def __init__(self, nom: str, type_client: str):
        self.nom = nom
        self.type_client = type_client


class CalculateurPrix:
    
    def __init__(self):
        # FIXME: Structures de données inefficaces
        self.frais_livraison = [
            ("livre", 5.99),
            ("electronique", 12.99),
            ("vetement", 6.99)
        ]

    def _chercher_frais_livraison(self, type_produit: str) -> float:
        # FIXME: Recherche linéaire inefficace
        for element in self.frais_livraison:
            if element[0] == type_produit:
                return element[1]
        return 7.99  # Défaut
    
    def afficher_prix_final(self, produit: Produit, client: Client) -> None:
        # FIXME: Méthode trop longue (fait : ajustements pays, produit, client, taxes, livraison, affichage)
        print(f"🧮 Calcul pour {produit.nom} - {client.nom} ({client.type_client})")
        
        prix_base = produit.prix
        print(f"   Prix de base: {prix_base:.2f}")
        
        ##############################################################
        # Modification du prix selon type de client
        ##############################################################
        # FIXME: Arbre if/elif -> code difficile à étendre
        if client.type_client == "premium":
            # FIXME:  Calcul dupliqué, devrait être dans une méthode dédiée
            remise_premium = prix_base * 0.20
            points_fidelite = int(prix_base // 10)

            prix_base -= remise_premium
            print(f"   Remise premium: -{remise_premium:.2f}")
            print(f"   Points fidélité gagnés: {points_fidelite}")
        elif client.type_client == "entreprise":
            # FIXME:  Calcul dupliqué, devrait être dans une méthode dédiée
            remise_entreprise = prix_base * 0.15
            points_fidelite = int(prix_base // 20)

            prix_base -= remise_entreprise
            print(f"   Remise entreprise: -{remise_entreprise:.2f}")
            print(f"   Points fidélité gagnés: {points_fidelite}")
        else:
            # FIXME:  Calcul dupliqué, devrait être dans une méthode dédiée
            remise_standard = prix_base * 0.05
            points_fidelite = int(prix_base // 50)

            prix_base -= remise_standard
            print(f"   Remise standard: -{remise_standard:.2f}")
            print(f"   Points fidélité gagnés: {points_fidelite}")
        
        ##############################################################
        # Application des taxes et frais de livraison
        ##############################################################
        # FIXME: _chercher_taux inefficace
        frais_livraison = self._chercher_frais_livraison(produit.type_produit)
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