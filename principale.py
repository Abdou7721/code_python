
from datetime import date
from categorie import Categorie
from client import Client
from panier import Panier
from role import Role
from admin import Admin
from produit import Produit

# admin_role = Role("Admin", ["add_product", "update_product", "delete_product", "add_personnel", "update_personnel", "delete_personnel"])
# personnel_role = Role("Personnel", ["change_order_status"])
# client_role = Role("Client", ["place_order", "add_to_cart", "update_cart_item_quantity", "clear_cart"])

donnees_personnel = []
products = []
paniers = [
    Panier(1),
    Panier(2),
    Panier(3),
]
liste_commande = []
    


# produit1= Produit(1,"PC","",1000,"electronique", 20)
# produit2= Produit(2,"PC","",1000,"electronique", 20)
# produitThera= Produit(3,"MERCEDESS","",90,"Automobile",20)



# print(produit1)
categorie_electro = Categorie(1, "electro")
categorie_voiture = Categorie(2, "voiture")
categorie_lait = Categorie(3, "lait")
categorie_accessoire = Categorie(4,"Accessoire")

client1 = Client(1, "nom1", "prenom1", "mdp", "12345678", Role.Client, 1)
client2 = Client(1, "nom2", "prenom2", "mdp", "12345678", Role.Client, 2)
client3 = Client(1, "nom3", "prenom3", "mdp", "12345678", Role.Client, 3)


adminThera = Admin(2,"Thera", "Badra", "mot_de_pass", "12345678", Role.Admin)
adminHarouna = Admin(3,"Diallo","Harouna","mdp","3234356",Role.Admin)
produit1 = adminThera.creer_produit(1, "PC", "",1000, categorie_electro, 2)
produit4 = adminThera.creer_produit(1, "Telephone", "",1000, categorie_electro, 3)
produitHarouna = adminHarouna.creer_produit(6,"Lunette","",200,categorie_accessoire,4)
# categorie_lait = Categorie(3, "lait")
produit2 = adminThera.creer_produit(2,"Candia","",90, categorie_lait, 3)
produit3 = adminThera.creer_produit(4,"Abdala","",90, categorie_lait, 10)
# produit2 = adminThera.creer_produit(3,"MERCEDESS","",90, categorie_voiture, 20)
adminThera.ajouter_produit(produit1, products)
adminThera.ajouter_produit(produit2, products)
adminThera.ajouter_produit(produit3, products)
adminThera.ajouter_produit(produit4, products)
adminHarouna.ajouter_produit(produitHarouna,products)

client1.ajouter_produit_panier(produit1, 5, paniers)
client1.ajouter_produit_panier(produit1, 5, paniers)
client1.ajouter_produit_panier(produit3, 5, paniers)
client3.ajouter_produit_panier(produit3, 5, paniers)

# client1.supprimer_produit(produit1, paniers)

for h in range(len(paniers)):
   print(f"panier: id={paniers[h].id} cart={paniers[h].cart}")

varComande = client1.passer_commande(paniers)
client1.effectuer_paiement(10450, varComande, liste_commande)
print(liste_commande[0])
# p = adminThera.recupe_produit_par_id(1, products)
# h = adminHarouna.recupe_produit_par_id(6,products)
# h_new = adminHarouna.recupe_produit_par_id(6,products)
# p_new = adminThera.recupe_produit_par_id(1, products)
# c = adminHarouna.recupe_produit_par_id(2,products)
# c_new = adminThera.recupe_produit_par_id(2, products)
# p_new.catégorie_id = 2
# h_new.catégorie_id = 1
# print(f"Le produit avant modif: {p_new}")
# p_new.libelle = "p_new"
# h_new.libelle = "Nouveau Produit Diallo"
# if(h==None):
#     print("Id introuvable")
# else:
#     adminHarouna.modifier_produit(h, h_new, products)

# if(p==None):
#     print("Id introuvable")
# else:
#     adminThera.modifier_produit(p, p_new, products)
# print(products)

# adminHarouna.supprimer_produit(h_new, products)
# for h in range(len(products)):
#    print(f"{products[h]}")

# adminThera.supprimer_produit(p_new, products)
# for p in range(len(products)):
#    print(f"{products[p]}")

# adminThera.ajouter_produit(produit2, products)
# adminThera.ajouter_produit(produit3, products)
# adminThera.Ajouter_utilisateur(4,"Adama", "Konate", "mot_de_pass", "12345678", Role.Personnel, donnees_personnel)
# print(produit1)
# print(produit2)
# print(produit3)
# print("recupe:",adminThera.recupe_produit_par_id(4, products))
# print(products.index(produit1))

# admin = Admin(5,"JOE", "prenom", "mot_de_pass", "12345678", Role.Admin)
# admin.ajouter_produit(produit1, products)
# admin.ajouter_produit(produit2, products)
#adminThera.ajouter_produit(produitThera, products)
#adminThera.Ajouter_utilisateur(9,"Thera", "Badra", "mot_de_pass", "12345678", Role.Admin, donnees_personnel)
#for p in range(len(products)):
#    print(f"{products[p].toString()}")
#for p in range(len(donnees_personnel)):
 #   print(f"{donnees_personnel[p]}")    


# print(admin.Ajouter_utilisateur(id_personnel=3,nom="John", prenom="Doe", mot_de_passe="password", telephone="1234567890", role=Role.Personnel))
# clientMoh = Client(1, nom="Kone", prenom="Mohamed",mot_de_pass="eerty",telephone="1234",role="Client")
# client1 = Client(1, nom="A", prenom="z",mot_de_pass="eerty",telephone="1234",role="Client")

# client1.voir_produit(products)
# clientMoh.voir_produit(products)

# Exemple d'utilisation :
# client1 = Client(id_user=4, nom="John", prenom="Doe", mot_de_pass="azert", telephone="1234567890", role=Role.Client) 
# client1 = Client(id_user=4, nom="John", prenom="Doe", mot_de_pass="azert", telephone="1234567890", role=Role.Client)

# client1.ajouter_produit_panier(produit1)
#clientMoh.ajouter_produit_panier(produitThera)
# client1.ajouter_produit_panier(produit2)
# client1.supprimer_produit("PC")

# client1.passer_commande()
#clientMoh.passer_commande()
# client1.effectuer_paiement(id_payement=1, mode_payement="Carte bancaire", date_reglement=date.today(), montant_paye=1000)
# clientMoh.effectuer_paiement(id_payement=1, mode_payement="Carte bancaire", date_reglement=date.today(), montant_paye=100)


from datetime import date
from categorie import Categorie
from client import Client
from panier import Panier
from role import Role
from admin import Admin
from produit import Produit

# admin_role = Role("Admin", ["add_product", "update_product", "delete_product", "add_personnel", "update_personnel", "delete_personnel"])
# personnel_role = Role("Personnel", ["change_order_status"])
# client_role = Role("Client", ["place_order", "add_to_cart", "update_cart_item_quantity", "clear_cart"])

donnees_personnel = []
products = []
paniers = [
    Panier(1),
    Panier(2),
    Panier(3),
]
class data:
    liste_commande=[]


# produit1= Produit(1,"PC","",1000,"electronique", 20)
# produit2= Produit(2,"PC","",1000,"electronique", 20)
# produitThera= Produit(3,"MERCEDESS","",90,"Automobile",20)



# print(produit1)
categorie_electro = Categorie(1, "electro")
categorie_voiture = Categorie(2, "voiture")
categorie_lait = Categorie(3, "lait")
categorie_accessoire = Categorie(4,"Accessoire")

client1 = Client(1, "nom1", "prenom1", "mdp", "12345678", Role.Client, 1)
client2 = Client(1, "nom2", "prenom2", "mdp", "12345678", Role.Client, 2)
client3 = Client(1, "nom3", "prenom3", "mdp", "12345678", Role.Client, 3)


adminThera = Admin(2,"Thera", "Badra", "mot_de_pass", "12345678", Role.Admin)
adminHarouna = Admin(3,"Diallo","Harouna","mdp","3234356",Role.Admin)
produit1 = adminThera.creer_produit(1, "PC", "",1000, categorie_electro, 2)
produit4 = adminThera.creer_produit(1, "Telephone", "",1000, categorie_electro, 3)
produitHarouna = adminHarouna.creer_produit(6,"Lunette","",200,categorie_accessoire,4)
# categorie_lait = Categorie(3, "lait")
produit2 = adminThera.creer_produit(2,"Candia","",90, categorie_lait, 3)
produit3 = adminThera.creer_produit(4,"Abdala","",90, categorie_lait, 10)
# produit2 = adminThera.creer_produit(3,"MERCEDESS","",90, categorie_voiture, 20)
adminThera.ajouter_produit(produit1, products)
adminThera.ajouter_produit(produit2, products)
adminThera.ajouter_produit(produit3, products)
adminThera.ajouter_produit(produit4, products)
adminHarouna.ajouter_produit(produitHarouna,products)

client1.ajouter_produit_panier(produit1, 5, paniers)
client1.ajouter_produit_panier(produit1, 5, paniers)
client1.ajouter_produit_panier(produit3, 5, paniers)
client3.ajouter_produit_panier(produit3, 5, paniers)

for h in range(len(paniers)):
   print(f"panier: id={paniers[h].id} cart={paniers[h].cart}")

# p = adminThera.recupe_produit_par_id(1, products)
# h = adminHarouna.recupe_produit_par_id(6,products)
# h_new = adminHarouna.recupe_produit_par_id(6,products)
# p_new = adminThera.recupe_produit_par_id(1, products)
# c = adminHarouna.recupe_produit_par_id(2,products)
# c_new = adminThera.recupe_produit_par_id(2, products)
# p_new.catégorie_id = 2
# h_new.catégorie_id = 1
# print(f"Le produit avant modif: {p_new}")
# p_new.libelle = "p_new"
# h_new.libelle = "Nouveau Produit Diallo"
# if(h==None):
#     print("Id introuvable")
# else:
#     adminHarouna.modifier_produit(h, h_new, products)

# if(p==None):
#     print("Id introuvable")
# else:
#     adminThera.modifier_produit(p, p_new, products)
# print(products)

# adminHarouna.supprimer_produit(h_new, products)
# for h in range(len(products)):
#    print(f"{products[h]}")

# adminThera.supprimer_produit(p_new, products)
# for p in range(len(products)):
#    print(f"{products[p]}")

# adminThera.ajouter_produit(produit2, products)
# adminThera.ajouter_produit(produit3, products)
# adminThera.Ajouter_utilisateur(4,"Adama", "Konate", "mot_de_pass", "12345678", Role.Personnel, donnees_personnel)
# print(produit1)
# print(produit2)
# print(produit3)
# print("recupe:",adminThera.recupe_produit_par_id(4, products))
# print(products.index(produit1))

# admin = Admin(5,"JOE", "prenom", "mot_de_pass", "12345678", Role.Admin)
# admin.ajouter_produit(produit1, products)
# admin.ajouter_produit(produit2, products)
#adminThera.ajouter_produit(produitThera, products)
#adminThera.Ajouter_utilisateur(9,"Thera", "Badra", "mot_de_pass", "12345678", Role.Admin, donnees_personnel)
#for p in range(len(products)):
#    print(f"{products[p].toString()}")
#for p in range(len(donnees_personnel)):
 #   print(f"{donnees_personnel[p]}")    


# print(admin.Ajouter_utilisateur(id_personnel=3,nom="John", prenom="Doe", mot_de_passe="password", telephone="1234567890", role=Role.Personnel))
# clientMoh = Client(1, nom="Kone", prenom="Mohamed",mot_de_pass="eerty",telephone="1234",role="Client")
# client1 = Client(1, nom="A", prenom="z",mot_de_pass="eerty",telephone="1234",role="Client")

# client1.voir_produit(products)
# clientMoh.voir_produit(products)

# Exemple d'utilisation :
# client1 = Client(id_user=4, nom="John", prenom="Doe", mot_de_pass="azert", telephone="1234567890", role=Role.Client) 
# client1 = Client(id_user=4, nom="John", prenom="Doe", mot_de_pass="azert", telephone="1234567890", role=Role.Client)

# client1.ajouter_produit_panier(produit1)
#clientMoh.ajouter_produit_panier(produitThera)
# client1.ajouter_produit_panier(produit2)
# client1.supprimer_produit("PC")

# client1.passer_commande()
#clientMoh.passer_commande()
# client1.effectuer_paiement(id_payement=1, mode_payement="Carte bancaire", date_reglement=date.today(), montant_paye=1000)
# clientMoh.effectuer_paiement(id_payement=1, mode_payement="Carte bancaire", date_reglement=date.today(), montant_paye=100)

