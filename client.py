
from datetime import datetime
from payement import Payement
from user import User
from produit import Produit


class Client(User):
    def __init__(self, id_user, nom, prenom, mot_de_pass, telephone, role, id_panier):
        super().__init__(id_user, nom, prenom, mot_de_pass, telephone, role)
        self.id_panier = id_panier
    
     # Méthode pour afficher les produits
    def voir_produit(self, listproduit):
       for i in range(len(listproduit)):
         print(listproduit[i])
 

    def ajouter_produit_panier(self, produit: Produit, list_panier):
        for i in range(len(list_panier)):
            if(list_panier[i].id == self.id_panier):
                list_panier[i].cart.append(produit)

        # self.panier.append(produit)
        print(f"Le produit '{produit.libelle}' a été ajouté à votre panier.")


    def supprimer_produit(self, nom_produit):
        produits_supprimes = []
        for produit in self.panier:
            if produit.libelle == nom_produit:
                self.panier.remove(produit)
                produits_supprimes.append(produit)
        if produits_supprimes:
            print(f"Les produits avec le nom '{nom_produit}' ont été supprimés du panier.")
        else:
            print(f"Aucun produit avec le nom '{nom_produit}' n'a été trouvé dans le panier.")

    def passer_commande(self):
        # Implémentez ici la logique pour passer une commande, par exemple, enregistrer la commande dans une base de données.
        montant_total = sum(produit.prix for produit in self.panier)
        date_commande = datetime.now()
        # Réinitialisez le panier après avoir passé la commande.
        self.panier = []
        print(f"Commande passée avec succès le {date_commande}. Montant total : {montant_total} FCFA.")

    def effectuer_paiement(self, id_payement, mode_payement, date_reglement, montant_paye):
        # Instancier un objet Payement
        paiement = Payement(id_payement, mode_payement, date_reglement, montant_paye)
        # Appeler la méthode pour effectuer le paiement
        paiement.effectuer_paiement()
   