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
        # Utilisation d'un dictionnaire pour accès plus rapide
        self.frais_livraison = {
            "livre": 5.99,
            "electronique": 12.99,
            "vetement": 6.99
        }

    def _chercher_frais_livraison(self, type_produit: str) -> float:
        # Recherche efficace dans le dictionnaire
        return self.frais_livraison.get(type_produit, 7.99) 

    def _calculer_remise_et_points(self, prix_base: float, type_client: str):
        if type_client == "premium":
            remise = prix_base * 0.15
            points = int(prix_base // 10)
        elif type_client == "entreprise":
            remise = prix_base * 0.10
            points = int(prix_base // 20)
        else:
            remise = prix_base * 0.05
            points = int(prix_base // 50)
        return remise, points
    
    def afficher_prix_final(self, produit: Produit, client: Client) -> None:
        print(f"🧮 Calcul pour {produit.nom} - {client.nom} ({client.type_client})")
        prix_base = produit.prix
        print(f"   Prix de base: {prix_base:.2f}")
        
        ##############################################################
        # Modification du prix selon type de client
        ##############################################################
        remise, points_fidelite = self._calculer_remise_et_points(prix_base, client.type_client)
        prix_base -= remise
        if client.type_client == "premium":
            print(f"   Remise premium: -{remise:.2f}")
        elif client.type_client == "entreprise":
            print(f"   Remise entreprise: -{remise:.2f}")
        else:
            print(f"   Remise standard: -{remise:.2f}")
        print(f"   Points fidélité gagnés: {points_fidelite}")
        
        ##############################################################
        # Application des taxes et frais de livraison
        ##############################################################
        # utilise le type de produit pour les frais de livraison
        frais_livraison = self._chercher_frais_livraison(produit.type_produit)
        prix_final = prix_base + frais_livraison
        print(f"   Livraison: +{frais_livraison:.2f}")
        print(f"   💵 Prix final: {prix_final:.2f}")


def main():
    """Démonstration du calculateur avec ses défauts"""
   
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
