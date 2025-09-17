from revision.produit import Produit
from revision.client import Client
from revision.calculateurPrix import CalculateurPrix
from revision.fabrique import FabriquePremium, FabriqueEntreprise, FabriqueStandard, FabriqueZero

def main():
    print("=" * 50)
    print(" DÉMONSTRATION CALCULATEUR (REFACTORÉ) ")
    print("=" * 50)

    # Initialisation
    calculateur = CalculateurPrix()

    # Création de produits
    livre = Produit("Python Guide", 29.99, "livre")
    smartphone = Produit("Smartphone", 599.99, "electronique")
    toutou = Produit("Toutou", 9.99, "toutou")  # Test frais livraison defaut

    # Création de clients
    client_fr = Client("Jean Dupont", FabriquePremium())
    client_ca = Client("Marie Tremblay", FabriqueEntreprise())
    client_us = Client("John Smith", FabriqueStandard())
    client_ze = Client("Natacha Meyer", FabriqueZero())

    # Tests de calculs
    print("📚 Test 1: Livre - Client premium")
    calculateur.afficher_prix_final(livre, client_fr)

    print("\n📱 Test 2: Smartphone - Client entreprise")
    calculateur.afficher_prix_final(smartphone, client_ca)

    print("\n📱 Test 3: Smartphone - Client standard")
    calculateur.afficher_prix_final(smartphone, client_us)

    print("\n📱 Test 4: Toutou - Client 'zero' - un nouveau type de client")
    calculateur.afficher_prix_final(toutou, client_ze)

if __name__ == "__main__":
    main()
