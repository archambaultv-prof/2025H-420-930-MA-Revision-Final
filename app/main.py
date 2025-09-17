from models import Produit, Client
from strategies import Premium, Entreprise, Standard


class CalculateurPrix:
    
    def __init__(self):
        # FIXME: Structures de données inefficaces FIXED

        # Le problème d'avant : Liste de tuples inefficace pour la recherche
        # La résolution : Dictionnaire pour recherche en O(1) au lieu de O(n)
        self.frais_livraison = {
            "livre": 5.99,
            "electronique": 12.99,
            "vetement": 6.99
        }

        #Ajout Registre des fabriques permettant l'ajout sans modification du code principal
        self.fabriques_clients = {
            "premium": Premium(),
            "entreprise": Entreprise(),
            "standard": Standard()
        }

    def _chercher_frais_livraison(self, type_produit: str) -> float:
    # Recherche directe dans un dictionnaire plutot que dans la liste lineaire
        return self.frais_livraison.get(type_produit, 7.99)
    
    def afficher_prix_final(self, produit: Produit, client: Client) -> None:
        # FIXME: Méthode trop longue (fait : ajustements pays, produit, client, taxes, livraison, affichage)
        print(f"🧮 Calcul pour {produit.nom} - {client.nom} ({client.type_client})")
        
        prix_base = produit.prix
        print(f"   Prix de base: {prix_base:.2f}")
        
        # FIXME: Arbre if/elif -> code difficile à étendre
        # on n'a plus besoin des chiffres codés en dur on apelle directement les abstractions
        fabrique = self.fabriques_clients.get(client.type_client, self.fabriques_clients["standard"])
        
        # Créer les stratégies via la fabrique
        strategie_remise = fabrique.remise()
        strategie_points = fabrique.points()
        
        # Calculs via les stratégies
        remise = strategie_remise.calculer(prix_base)
        points_fidelite = strategie_points.calculer(prix_base)
        
        prix_base -= remise
        
        # Affichage selon le type de client
        if client.type_client == "premium":
            print(f"   Remise premium: -{remise:.2f}")
            print(f"   Points fidélité gagnés: {points_fidelite}")
        elif client.type_client == "entreprise":
            print(f"   Remise entreprise: -{remise:.2f}")
            print(f"   Points fidélité gagnés: {points_fidelite}")
        else:
            print(f"   Remise standard: -{remise:.2f}")
            print(f"   Points fidélité gagnés: {points_fidelite}")
        
        ##############################################################
        # Application des taxes et frais de livraison
        ##############################################################
        # FIXME: _chercher_taux inefficace ----- HA oui ok, ici on appelle le type de client, mais on veut le type de livraison
        frais_livraison = self._chercher_frais_livraison(produit.type_produit) # <-
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