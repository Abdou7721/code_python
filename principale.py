
from datetime import date
from client import Client
from role import Role
from admin import Admin
from produit import Produit

# admin_role = Role("Admin", ["add_product", "update_product", "delete_product", "add_personnel", "update_personnel", "delete_personnel"])
# personnel_role = Role("Personnel", ["change_order_status"])
# client_role = Role("Client", ["place_order", "add_to_cart", "update_cart_item_quantity", "clear_cart"])

donnees_personnel = []
products = []
class data:
    liste_commande=[]


produit1= Produit(1,"PC","",1000,"electronique", 20)
produit2= Produit(2,"PC","",1000,"electronique", 20)
produitThera= Produit(3,"MERCEDESS","",90,"Automobile",20)



# print(produit1.toString())


adminThera = Admin(2,"Thera", "Badra", "mot_de_pass", "12345678", Role.Admin)
adminThera.Ajouter_utilisateur(4,"Adama", "Konate", "mot_de_pass", "12345678", Role.Personnel, donnees_personnel)

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
clientMoh = Client(1, nom="Kone", prenom="Mohamed",mot_de_pass="eerty",telephone="1234",role="Client")
# client1 = Client(1, nom="A", prenom="z",mot_de_pass="eerty",telephone="1234",role="Client")

# client1.voir_produit(products)
clientMoh.voir_produit(products)

# Exemple d'utilisation :
# client1 = Client(id_user=4, nom="John", prenom="Doe", mot_de_pass="azert", telephone="1234567890", role=Role.Client) 
client1 = Client(id_user=4, nom="John", prenom="Doe", mot_de_pass="azert", telephone="1234567890", role=Role.Client)

# client1.ajouter_produit_panier(produit1)
#clientMoh.ajouter_produit_panier(produitThera)
# client1.ajouter_produit_panier(produit2)
# client1.supprimer_produit("PC")

# client1.passer_commande()
#clientMoh.passer_commande()
# client1.effectuer_paiement(id_payement=1, mode_payement="Carte bancaire", date_reglement=date.today(), montant_paye=1000)
clientMoh.effectuer_paiement(id_payement=1, mode_payement="Carte bancaire", date_reglement=date.today(), montant_paye=100)

