class User:
    def __init__(self,id_user,nom,prenom,mot_de_pass,telephone,role):
        self.id_user = id_user
        self.nom = nom
        self.prenom = prenom
        self.mot_de_pass = mot_de_pass
        self.telephone = telephone
        self.role = role
        
        
class Personnel(User):
    def __init__(self,id_user,nom,prenom,mot_de_pass,telephone):
        super()._init_(id_user,nom,prenom,mot_de_pass,telephone, "Personnel")

    def changer_status_commande(self, commande, new_status):
        commande.update_status(new_status)

