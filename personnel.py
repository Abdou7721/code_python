
from role import Role
from user import User

class Personnel(User):
    def __init__(self, id_personnel, nom, prenom, mot_de_pass, telephone, role):
        super().__init__(id_personnel, nom, prenom, mot_de_pass, telephone, role)  

    def changer_status_commande(self, commande, new_status):
        commande.update_status(new_status, self.id_user)
