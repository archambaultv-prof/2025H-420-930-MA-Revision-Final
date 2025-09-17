from revision.fabrique import FabriqueClient

class Client:
    def __init__(self, nom: str, type_client: FabriqueClient):
        self.nom = nom
        self.type_client = type_client