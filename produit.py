class Produit:
    quantiteProduit = 0
    def __init__(self, id_produit, libelle, date, prix, id_categorie):
        self.id_produit = id_produit
        self.libelle = libelle
        self.date = date
        self.prix = prix
        self.id_categorie = id_categorie

    def set_libelle(self, libelle):
        self.libelle = libelle
        print("nouveau libelle:", libelle)

class Produit_Admin:
    def __init__(self, produit, id_admin):
        self.produit = produit
        self.id_admin = id_admin

    def toString(self):
        return print(self.produit, self.id_admin)