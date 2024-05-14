

from base import data
from users import Users

class Client(Users):
    def __init__(self, id_client, id_users):
        from role import Role
        super().__init__(id_users=id_users, nom="", prenom="", mot_de_passe="", telephone="", role=Role.Client)
        self.id_client = id_client
        self.id_users = id_users


    def créer_un_compte(self, nom, prenom, mot_de_passe, telephone):
        # Logique pour créer un compte client
        pass

    def passer_commande(self):
        print("Voici la liste des produits disponibles:")
        for produit in data.produits:
            print(produit)


        #nom_produit = input("Entrez le nom du produit que vous souhaitez commander: ")
        #data.commandes.append(nom_produit)
        #print("Produit ajouté avec succès!")
        #for produit_commandés in data.commandes:
        #   print(produit_commandés)
        while True:  # Boucle infinie qui ne s'arrête que lorsque l'utilisateur saisit '0'
            nom_produit = input("Entrez le nom du produit que vous souhaitez commander, ou '0' pour arrêter: ")

            if nom_produit == '0':
                break  # Arrête la boucle si l'utilisateur a saisi '0'

            data.commandes.append(nom_produit)
            print("Produit ajouté avec succès!")

        print("Voici tous les produits que vous avez commandés:")
        for produit_commandés in data.commandes:
            print(produit_commandés)
        pass
        print("Votre commande est en attente, merci de patientez...")

    def modifier(self):
        # Logique pour modifier les informations du client
        pass

    def supprimer(self):
        # Logique pour supprimer un produit du panier du client
        pass

    def voir_produits(self):
        # Logique pour afficher les produits du client
        pass

    def FairePayement(self):
        # Logique pour effectuer un paiement
        pass
client = Client(id_client=1, id_users="client456")
client.nom = "KONATE"
client.prenom = "ADAMA"
client.passer_commande()