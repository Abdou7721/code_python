


class Categorie:

    # Classe représentant une catégorie de produit dans le système.

    def __init__(self, id, nom):

        self.id = id
        self.nom = nom
        self.produits = {}  

    def ajouter_produit(self, produit):

        self.produits[produit.nom] = produit

    def supprimer_produit(self, nom_produit):

        if nom_produit in self.produits:
            del self.produits[nom_produit]

def supprimer_cat(self):
        # Supprime la catégorie en supprimant tous les produits associés
        self.produits = {}
        

def modifier_cat(self, nouveau_nom):
        # Modifie le nom de la catégorie
        self.nom = nouveau_nom
        