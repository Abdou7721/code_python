from categorie import Categorie
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
    def creer_produit(self,id_produit,libelle,date,prix,catégorie: Categorie, quantiteProduit) -> Produit:
        cate_id = catégorie.id
        produit = Produit(id_produit,libelle,date,prix,cate_id, quantiteProduit)
        return produit
    
    def recupe_produit_par_id(self, id, listproduit) -> Produit|None:
        for i in range(len(listproduit)):
            if(listproduit[i].id_produit == id):
                return listproduit[i]
        return None
    
    
    # Cette methode prend en parametre un produit et un tableau dans lequel le produit sera ajouté.
    def ajouter_produit(self, produit: Produit, listproduit):
        itemIsIn = False
        for i in range(len(listproduit)):
            if(listproduit[i].id_produit == produit.id_produit):
                if(listproduit[i].libelle != produit.libelle):
                    print("Un produit avec l'id: ", produit.id_produit, "existe déjà.")
                    itemIsIn = True
                    break
                else:
                    listproduit[i].quantiteProduit += produit.quantiteProduit
                    print(f"Le produit {listproduit[i].libelle} incrementé")
                    itemIsIn = True
                    break
        if(itemIsIn == False):
            # produit_admin = Produit_Admin(produit, self.id_user)
            
            listproduit.append(produit)
            print(produit)
            print(f"Le produit {produit.libelle} a été ajouté avec succès")

    # Cette methode modifie un produit.
    def modifier_produit(self, produit: Produit, new_produit: Produit, listproduit):
        # print(f"Le produit avant modif: {produit}")
        index_produit_inList = listproduit.index(produit)
        produit.libelle = new_produit.libelle
        produit.date = new_produit.date
        produit.prix = new_produit.prix
        produit.catégorie_id = new_produit.catégorie_id
        produit.quantiteProduit = new_produit.quantiteProduit
        listproduit[index_produit_inList] = produit
        print(f"Le produit apres modif: {produit}")

    # Cette methode prend en parametre un produit et un tableau dont le produit sera retiré.
    def supprimer_produit(self, produit, listproduit):
        for i in range(len(listproduit)):
            if(listproduit[i].id_produit == produit.id_produit):
                listproduit.remove(listproduit[i])
                print(f"Produit {produit.libelle} supprimé avec success")
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
    
    def modifier_utilisateur(self, personnel: Personnel, new_personnel: Personnel, personnel_list):
        index_personnel_inList = personnel_list.index(personnel)
        personnel.nom = new_personnel.nom
        personnel.prenom = new_personnel.prenom
        personnel.telephone = new_personnel.telephone
        personnel.role = new_personnel.role
        personnel_list[index_personnel_inList] = personnel
        print(f"Le produit apres modif: {personnel}")

