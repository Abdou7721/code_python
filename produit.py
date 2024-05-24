from datetime import datetime


class Produit:
    
    def __init__(self,id_produit,libelle,date,prix,catégorie_id,quantiteProduit,id_admin):
        self.id_produit = id_produit
        self.libelle = libelle
        self.date = datetime.now()
        self.prix = prix
        self.id_admin=id_admin
        self.catégorie_id= catégorie_id
        self.quantiteProduit= quantiteProduit
    quantiteToCart = 0
    def __str__(self):
        return f" id : {self.id_produit}, nom : {self.libelle} ,date d'ajout: {self.date},prix: {self.prix}, catégorie id: {self.catégorie_id}, quantité: {self.quantiteProduit}"

    



