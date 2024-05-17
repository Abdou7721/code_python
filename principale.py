
from datetime import date
from categorie import Categorie
from client import Client
from code_python.personnel import Personnel
from panier import Panier
from role import Role
from admin import Admin
from produit import Produit

# admin_role = Role("Admin", ["add_product", "update_product", "delete_product", "add_personnel", "update_personnel", "delete_personnel"])
# personnel_role = Role("Personnel", ["change_order_status"])
# client_role = Role("Client", ["place_order", "add_to_cart", "update_cart_item_quantity", "clear_cart"])

donnees_personnel = []
liste_admin=[]
#products = []
#paniers = [
 #   Panier(1),
 #   Panier(2),
  #  Panier(3),
#]
#class data:
    #liste_commande=[]


# produit1= Produit(1,"PC","",1000,"electronique", 20)
# produit2= Produit(2,"PC","",1000,"electronique", 20)
# produitThera= Produit(3,"MERCEDESS","",90,"Automobile",20)



# print(produit1)
#categorie_electro = Categorie(1, "electro")
#categorie_voiture = Categorie(2, "voiture")
#categorie_lait = Categorie(3, "lait")
#categorie_accessoire = Categorie(4,"Accessoire")

#client1 = Client(1, "nom1", "prenom1", "mdp", "12345678", Role.Client, 1)
#client2 = Client(1, "nom2", "prenom2", "mdp", "12345678", Role.Client, 2)
#client3 = Client(1, "nom3", "prenom3", "mdp", "12345678", Role.Client, 3)


#adminThera = Admin(2,"Thera", "Badra", "mot_de_pass", "12345678", Role.Admin)
#adminHarouna = Admin(3,"Diallo","Harouna","mdp","3234356",Role.Admin)
#produit1 = adminThera.creer_produit(1, "PC", "",1000, categorie_electro, 2)
#produit4 = adminThera.creer_produit(1, "Telephone", "",1000, categorie_electro, 3)
#produitHarouna = adminHarouna.creer_produit(6,"Lunette","",200,categorie_accessoire,4)
# categorie_lait = Categorie(3, "lait")
#produit2 = adminThera.creer_produit(2,"Candia","",90, categorie_lait, 3)
#produit3 = adminThera.creer_produit(4,"Abdala","",90, categorie_lait, 10)
# produit2 = adminThera.creer_produit(3,"MERCEDESS","",90, categorie_voiture, 20)
#adminThera.ajouter_produit(produit1, products)
#adminThera.ajouter_produit(produit2, products)
#adminThera.ajouter_produit(produit3, products)
#adminThera.ajouter_produit(produit4, products)
#adminHarouna.ajouter_produit(produitHarouna,products)

#client1.ajouter_produit_panier(produit1, 5, paniers)
#client1.ajouter_produit_panier(produit1, 5, paniers)
#client1.ajouter_produit_panier(produit3, 5, paniers)
#client3.ajouter_produit_panier(produit3, 5, paniers)

#for h in range(len(paniers)):
#   print(f"panier: id={paniers[h].id} cart={paniers[h].cart}")

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


# Création de listes pour stocker les objets Personnel et Admin
liste_personnel = []
liste_admin = []
liste_client = []

print("A : admin")
print("B : personnel")
print("C : client")

role_utilisateur = input("Quel est le rôle de l'utilisateur ?:")


if role_utilisateur == "A":
    # Instanciation d'un objet Admin
    print("1 : Créer un autre admin")
    print("2 : Se connecter à partir d'un identifiant")
    ad=input("l'option:")
    if ad=="1":
        id_user = input("Entrez l'ID de l'Admin : ")
        nom_admin = input("Entrez le nom de l'Admin : ")
        prenom_admin = input("Entrez le prénom de l'Admin : ")
        mot_de_pass_admin = input("Entrez le mot de passe de l'Admin : ")
        telephone_admin = input("Entrez le téléphone de l'Admin : ")
        admin = Admin(id_user, nom_admin, prenom_admin, mot_de_pass_admin, telephone_admin, Role.Admin)
        liste_admin.append(admin)
        print("l'admin créer avec success !!!")
        print("Veuillez vous connecter avec votre nouvel ID d'Admin.")
        while True:
            id_user = input("Entrez l'ID de l'Admin : ")
            # Parcourir la liste_admin pour vérifier si l'id saisi est dedans
            for admin in liste_admin:
                if admin.id_user == id_user:
                    print("L'admin connecté !")
                    break
            else:
                continue
            break


    elif ad == "2":
        while True:
            id_user = input("Entrez l'ID de l'Admin : ")
            # Parcourir la liste_admin pour vérifier si l'id saisi est dedans
            for admin in liste_admin:
                if admin.id_user == id_user:
                    print("l'admin connecté !")
                    break
            else:
                continue
            break
        print("Ajouter un personnel")
        print("Ajouter un produit")
        print("Supprimer un personnel")
        print("Supprimer un personnel")

elif role_utilisateur == "B":

        while True:
            id_user = input(" Se connecter à partir de votre identifiant")
            # Parcourir la liste_admin pour vérifier si l'id saisi est dedans
            for personnel in liste_personnel:
                if personnel.id_personnel == id_user:
                    print("l'admin connecté !")
                    break
            else:
                continue
            break



elif role_utilisateur == "C":
    # Instanciation d'un objet Client
    id_client = input("Entrez l'ID du Client : ")
    nom_client = input("Entrez le nom du Client : ")
    prenom_client = input("Entrez le prénom du Client : ")
    mot_de_pass_client = input("Entrez le mot de passe du Client : ")
    telephone_client = input("Entrez le téléphone du Client : ")
    client = Client(id_client, nom_client, prenom_client, mot_de_pass_client, telephone_client, Role.Client)
    liste_client.append(client)


