from personnel import Personnel
from role import Role
from produit import Produit, Produit_Admin
from user import User

# donnees_personnel = []

class Admin(User):
    def __init__(self, id_user, nom, prenom, mot_de_pass, telephone, role):
        super().__init__(id_user, nom, prenom, mot_de_pass, telephone, role=Role.Admin)
        # self.id_user = id_user
        # self.nom = nom
        # self.prenom = prenom
        # self.mot_de_pass = mot_de_pass
        # self.telephone = telephone
        # self.role = role 


    # Cette methode crée et retourne un produit.
    def creer_produit(self,id_produit,libelle,date,prix,catégorie,quantiteProduit) -> Produit:
        produit = Produit(id_produit,libelle,date,prix,catégorie,quantiteProduit)
        return produit
    
    # Cette methode prend en parametre un produit et un tableau dans lequel le produit sera ajouté.
    def ajouter_produit(self, produit, listproduit):
        itemIsIn = False
        for i in range(len(listproduit)):
            if(listproduit[i].produit.id_produit == produit.id_produit):
                listproduit[i].produit.quantiteProduit += 1
                print(f"Le produit {listproduit[i].produit.libelle} incrementé")
                itemIsIn = True
                break
        if(itemIsIn == False):
            produit_admin = Produit_Admin(produit, self.id_user)
            listproduit.append(produit_admin)
            produit_admin.toString()
            print(f"Le produit {produit.libelle} a été ajouté avec succès")

    # Cette methode modifie un produit.
    def modifier_produit(self, produit, new_produit: Produit):
        print(f"Le produit avant modif: {produit.libelle}")
        produit.libelle = new_produit.libelle
        produit.date = new_produit.date
        produit.prix = new_produit.prix
        produit.id_categorie = new_produit.id_categorie
        print(f"Le produit apres modif: {produit.libelle}")

    # Cette methode prend en parametre un produit et un tableau dont le produit sera retiré.
    def supprimer_produit(self, produit, listproduit):
        for i in range(len(listproduit)):
            if(listproduit[i].produit.id_produit == produit.id_produit):
                listproduit.remove(listproduit[i])
                print(len(listproduit))
                break 

    def Ajouter_utilisateur(self, id_personnel, nom, prenom, mot_de_passe, telephone, role, listpersonnel):
        personnel = Personnel(id_personnel, nom, prenom, mot_de_passe, telephone, role)
        listpersonnel.append(personnel)
        for personnel in listpersonnel:
            print(personnel)
        return f"Utilisateur avec id_personnel {id_personnel} a été ajouté avec success."
    def Supprimer_utilisateur(self, id_personnel, listpersonnel):
        for personnel in listpersonnel:
            if personnel.id_user == id_personnel:
                listpersonnel.remove(personnel)
                return f"Utilisateur avec id_personnel {id_personnel} à été supprimé avec succès."
        return "Aucun utilisateur trouvé avec cet id_personnel."
       

