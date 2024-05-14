from datetime import datetime


class Produit:
    
    def __init__(self,id_produit,libelle,date,prix,catégorie,quantiteProduit):
        self.id_produit = id_produit
        self.libelle = libelle
        self.date = datetime.now()
        self.prix = prix
        self.catégorie= catégorie
        self.quantiteProduit= quantiteProduit

    def __str__(self):
        return f" id : {self.id_produit}, nom : {self.libelle} ,date d'ajout: {self.date},prix: {self.prix}, catégorie: {self.catégorie}, quantité: {self.quantiteProduit}"


class Produit_Admin:
    def __init__(self, produit, id_admin):
        self.produit = produit
        self.id_admin = id_admin

    def toString(self):
        # return print(self.produit, self.id_admin)
        return f"{self.produit} par l'id de l'admin: {self.id_admin}"
    



