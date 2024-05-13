from datetime import datetime
from enum import Enum


class Commande:
    class Status(Enum):
        En_cours = 'En cours'
        Termine = 'Terminé'

    def __init__(self, id_commande, id_personnel, id_Panier, id_client, date, status):
        self.id_commande = id_commande
        self.id_personnel = id_personnel
        self.id_Panier = id_Panier
        self.id_client = id_client
        self.date = date
        self.status = status

    def __str__(self):
        return (f" Votre Commande est passée avec : id_commande={self.id_commande} , id_personnel={self.id_personnel}, id_Panier={self.id_Panier} "
                f"par le client: {self.id_client} au :{self.date.strftime('%Y-%m-%d')}, Le status de la commande est ={self.status.value}")
        pass


# Création d'un objet de la classe Commande
commande1 = Commande(
    id_commande=1,
    id_personnel=2,
    id_Panier=3,
    id_client=4,
    date=datetime.now(),
    status=Commande.Status.En_cours
)

print(commande1)