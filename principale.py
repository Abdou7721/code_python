
from admin import Admin


list_produit = []
admin = Admin(1)
produit = admin.creer_produit(1,"ordi", "12/05/2024", 2300, 1)
produit1 = admin.creer_produit(1,"ordi", "12/05/2024", 2300, 1)
produit2 = admin.creer_produit(2,"tele", "12/05/2024", 2300, 1)
admin.ajouter_produit(produit, list_produit)
admin.ajouter_produit(produit1, list_produit)
admin.ajouter_produit(produit2, list_produit)
print("liste contient:", list_produit)
# admin.modifier_produit(produit, Produit(0,"Television", "12/05/2024", 2300, 1))
# admin.supprimer_produit(produit,list_produit)