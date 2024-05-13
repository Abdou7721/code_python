
# Classe pour représenter les clients, héritant de Users
class Client(Users):
    def __init__(self, id_client, id_user):
        super().__init__(id_user=id_user, nom='', prenom='', mot_de_passe='', telephone='', role=Role.Client)
        self.id_client = id_client
    def passe_commande(self):
        pass
    
    def créer_un_compte(self):
        pass
    