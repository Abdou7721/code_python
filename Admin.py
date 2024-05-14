from Personnel import Personnel
from base import data
from role import Role
from users import Users

class data:
    produits=["ordinateur", "téléphone", "réfrigérateur", "voiture", "moto"]
    commandes=[]
    donnees_personnel=[]
    
class Administrateur(Users):
    def __init__(self, Id_admin, id_users):
        super().__init__(id_users=id_users, nom="", prenom="", mot_de_passe="", telephone="", role=Role.Admin)
        self.Id_admin = Id_admin
        self.id_users = id_users

    def __str__(self):
        return f"{self.Id_admin} et {self.id_users}"
    def ajouterProduit(self):
        # Logique pour ajouter un produit à la base de données
        pass

    def modifierProduit(self):
        # Logique pour modifier les informations d'un produit
        pass

    def supprimerProduit(self):
        # Logique pour supprimer un produit de la base de données
        pass

    def voir_produits(self):
        # Logique pour afficher tous les produits
        pass

    def Ajouter_utilisateur(self, id_personnel, id_users,  nom, prenom, mot_de_passe, telephone):
        personnel = Personnel(id_personnel, id_users,  nom, prenom, mot_de_passe, telephone)
        data.donnees_personnel.append(personnel)
        for personnel in data.donnees_personnel:
            print(personnel)
        return f"Utilisateur avec id_personnel {id_personnel} et id_users {id_users} ajouté avec success."
    def Supprimer_utilisateur(self, id_personnel=None):
        for personnel in data.donnees_personnel:
            if personnel.id_personnel == id_personnel:
                data.donnees_personnel.remove(personnel)
                return f"Utilisateur avec id_personnel {id_personnel} supprimé avec succès."
        return "Aucun utilisateur trouvé avec cet id_personnel."
        pass


admin1 = Administrateur(Id_admin=1, id_users=1)
print(admin1.Ajouter_utilisateur(id_personnel=3, id_users=3, nom="John", prenom="Doe", mot_de_passe="password", telephone="1234567890"))

