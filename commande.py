from datetime import datetime
from enum import Enum

from status import Status


class Commande:

    def __init__(self, id_Panier, id_client, date, montant, status: Status, id_personnel=0):
        # self.id_commande = id_commande
        self.id_personnel = id_personnel
        self.id_Panier = id_Panier
        self.id_client = id_client
        self.date = date
        self.status = status
        self.montant = montant

    def __str__(self):
        return f"Commande {self.id_client}, {self.montant} ({self.status.value})"