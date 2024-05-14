from role import Role
class User:
    def __init__(self, id_user, nom, prenom, mot_de_pass, telephone, role):  
        self.id_user = id_user
        self.nom = nom
        self.prenom = prenom
        self.mot_de_pass = mot_de_pass
        self.telephone = telephone
        self.role = role  

    def __str__(self):
        return f"l'utilisateur est: {self.id_user} nom : {self.nom} prenom : {self.prenom} role est: {Role.Admin}"
