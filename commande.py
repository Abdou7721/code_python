from datetime import datetime
from enum import Enum

from status import Status


class Commande:

    def __init__(self, id_Panier, id_client, date, montant, status: Status, id_personnel=0):
<<<<<<< HEAD
        # self.id_commande = id_commande
=======
>>>>>>> bd851f214da99333d707a6988427614a6c388c6d
        self.id_personnel = id_personnel
        self.id_Panier = id_Panier
        self.id_client = id_client
        self.date = date
        self.status = status
        self.montant = montant
<<<<<<< HEAD
=======
        self.historique = []  # Ajout d'un attribut pour l'historique des changements de statut

    def update_status(self, new_status, id_personnel):
        self.status = new_status
        self.historique.append((datetime.now(), id_personnel, new_status))
    
    def voir_commande(self, listCommande):
        for i in range(len(listCommande)):
            print(listCommande[i])
>>>>>>> bd851f214da99333d707a6988427614a6c388c6d

    def __str__(self):
        return f"Commande {self.id_client}, {self.montant} ({self.status.value})"