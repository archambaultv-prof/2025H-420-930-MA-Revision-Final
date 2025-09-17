from revision.produit import Produit
from revision.client import Client

class CalculateurPrix:
    def __init__(self):
        self.frais_livraison = {
            "livre": 5.99,
            "electronique": 12.99,
            "vetement": 6.99
        }

    def _chercher_frais_livraison(self, type_produit: str) -> float:
        return self.frais_livraison.get(type_produit, 7.99)

    def afficher_prix_final(self, produit: Produit, client: Client) -> None:
        print(f"🧮 Calcul pour {produit.nom} - {client.nom} ({client.type_client})")
        prix_base = produit.prix
        print(f"   Prix de base: {prix_base:.2f}$")

        fabrique = client.type_client
        if not fabrique:
            raise ValueError(f"Type de client inconnu: {client.type_client}")

        strategie_remise = fabrique.creer_strategie_remise()
        strategie_points = fabrique.creer_strategie_points()

        remise = strategie_remise.calculer(prix_base)
        points = strategie_points.calculer(prix_base)

        prix_apres_remise = prix_base - remise
        print(f"   Remise {client.type_client}: -{remise:.2f}$")
        print(f"   Points fidélité gagnés: {points}")

        frais_livraison = self._chercher_frais_livraison(produit.type_produit)
        prix_final = prix_apres_remise + frais_livraison
        print(f"   Livraison: +{frais_livraison:.2f}$")
        print(f"   💵 Prix final: {prix_final:.2f}$")
