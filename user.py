from enum import Enum
class role(Enum):
    Admin = 'Admin'
    Personnel = 'Personnel'
    Client = 'Client'

class User:
    def __init__(self,id_user,nom,prenom,mot_de_pass,telephone,role):
        self.id_user = id_user
        self.nom = nom
        self.prenom = prenom
        self.mot_de_pass = mot_de_pass
        self.telephone = telephone
        self.role = role
