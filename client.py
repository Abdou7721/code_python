#Les clases importer
from datetime import datetime
from produit import Produit
from Commande import Commande;
from categorie import Categorie;
from enum import Enum

# La classe Role
class Role(Enum):
    Admin = 'Admin'
    Personnel = 'Personnel'
    Client = 'Client'
# La classe utilisateur
class User:
    def __init__(self, id_user, nom, prenom, mot_de_pass, telephone, role):
        self.id_user = id_user
        self.nom = nom
        self.prenom = prenom
        self.mot_de_pass = mot_de_pass
        self.telephone = telephone
        self.role = role

# Classe pour représenter les clients, héritant de Users
class Client(User):
    def __init__(self, id_client, id_user):
        super().__init__(id_user=id_user, nom='', prenom='', mot_de_pass='', telephone='', role=Role.Client)
        self.id_client = id_client
      
        
    
    # Méthode pour passer une commande
    def passer_commande(self, Commande):

        pass
    
    
    
    # Méthode pour afficher les informations d'un produit
    def voir_produit(self, Produit):
       pass

# l'nstanciation de la classe client
client1 = Client(id_client=1, id_user=1,)
print("passer votre commande en entrant vos information")
client1.nom = input("Entrez votre nom : ")
client1.prenom = input("Entrez votre prénom : ")
client1.mot_de_pass = input("Entrez votre mot de passe : ")
client1.telephone = input("Entrez votre numéro de téléphone : ")


# l'nstanciation de la classe commande
commande = Commande(id_commande=1, id_personnel=1, id_Panier=1, id_client=client1.id_user, date=datetime.now(), status="En cours")


# l'nstanciation de la classe catégorie
#categorie = Categorie(id_categorie=1, nom="Électronique")
# Instantiation d'une catégorie
categorie1 = Categorie(id_categorie=1,nom = input("Entrez la catégorie de votre produit: "))


# l'nstanciation de la classe produit
#produit = Produit(id_produit=1, id_admin=1, id_categorie=1, libelle="Smartphone", date=datetime.now(), stock=100, prix=499.99)
produit1 = Produit(id_produit=1, id_admin=1, libelle = input("Entrez le nom du produit : "), id_categorie=1, date=datetime.now(), stock=100, prix=499.99)



# Affichage des informations sur le produit
print("Informations sur le produit :")
print("ID :", produit1.id_produit)
print("Libellé :", produit1.libelle)
print("Prix :", produit1.prix)
print("Stock :", produit1.stock)
print("Catégorie :", produit1.id_categorie)

# Affichage des informations sur la commande
print("Commande de", client1.nom, client1.prenom)
print("Produit:", produit1.libelle)
print("Categorie:", categorie1.nom)


