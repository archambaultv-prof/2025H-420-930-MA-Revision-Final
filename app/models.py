class Produit:   
    def __init__(self, nom: str, prix: float, type_produit: str):
        self.nom = nom
        self.prix = prix
        self.type_produit = type_produit


class Client:
    def __init__(self, nom: str, type_client: str):
        self.nom = nom
        self.type_client = type_client