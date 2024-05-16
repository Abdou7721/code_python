from datetime import datetime


class Produit:
    
    def __init__(self,id_produit,libelle,date,prix,catégorie_id, quantiteProduit):
        self.id_produit = id_produit
        self.libelle = libelle
        self.date = datetime.now()
        self.prix = prix
        self.catégorie_id= catégorie_id
        self.quantiteProduit= quantiteProduit
        
    quantiteToCart = 0

    def __str__(self):
        return f" id : {self.id_produit}, nom : {self.libelle} ,date d'ajout: {self.date},prix: {self.prix}, catégorie id: {self.catégorie_id}, quantité: {self.quantiteProduit}"


class Produit_Admin:
    def __init__(self, produit, id_admin):
        self.produit = produit
        self.id_admin = id_admin

    def toString(self):
        # return print(self.produit, self.id_admin)
        return f"{self.produit} par l'id de l'admin: {self.id_admin}"
    



