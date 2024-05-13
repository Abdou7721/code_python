from User import User
       
class Personnel(User):
    def __init__(self,id_user,nom,prenom,mot_de_pass,telephone):
        super()._init_(id_user,nom,prenom,mot_de_pass,telephone, "Personnel")

    def changer_status_commande(self, commande, new_status):
        commande.update_status(new_status)

