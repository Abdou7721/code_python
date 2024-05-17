from datetime import datetime
from enum import Enum
from base import data


class Commande:
    class Status(Enum):
        En_cours = 'En cours'
        Termine = 'Terminé'
    
    def __init__(self, id_commande, status=Status.En_cours):
        self.id_commande = id_commande
        self.status = status
    
    def update_status(self, new_status):
        if new_status in Commande.Status:
            self.status = new_status
        else:
            raise ValueError(f"{new_status} n'est pas un status valide")
    
    def __str__(self):
        return f"Commande ID: {self.id_commande}, Status: {self.status.value}"


    def __init__(self, id_commande, id_personnel, id_Panier, id_client, date, status):
        self.id_commande = id_commande
        self.id_personnel = id_personnel
        self.id_Panier = id_Panier
        self.id_client = id_client
        self.date = date
        self.status = status

    #def __str__(self):
       # return (f" Votre Commande est passée avec : id_commande={self.id_commande} , id_personnel={self.id_personnel}, id_Panier={self.id_Panier} "
           #     f"par le client: {self.id_client} au :{self.date.strftime('%Y-%m-%d')}, Le status de la commande est ={self.status.value}")
        

    def __str__(self):
        return f"Commande {self.id_commande} ({self.status.value})"

# Création d'un objet de la classe Commande
commande1 = Commande(
    id_commande=1,
    id_personnel=2,
    id_Panier=3,
    id_client=4,
    date=datetime.now(),
    status=Commande.Status.En_cours
)
data.liste_commande.append(commande1)
print("voici la liste des commandes:")
for commandes in data.liste_commande:
    print(commandes)
