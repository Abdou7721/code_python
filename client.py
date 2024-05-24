
from datetime import datetime
from commande import Commande
from payement import Payement
from status import Status
from user import User
from produit import Produit
from panier import Panier


class Client(User):
    def __init__(self, id_user, nom, prenom, mot_de_pass, telephone, role, id_panier):
        super().__init__(id_user, nom, prenom, mot_de_pass, telephone, role)
        self.id_panier = id_panier
       
    
     # Méthode pour afficher les produits
    def voir_produit(self, listproduit):
       for i in range(len(listproduit)):
         print(listproduit[i])
 

    def ajouter_produit_panier(self, produit: Produit, nbr, list_panier):
        for i in range(len(list_panier)):
            if(list_panier[i].id == self.id_panier):
                cart = list_panier[i].cart
                if(len(cart)==0):
                    cartItem = produit
                    cartItem.quantiteToCart += nbr
                    cart.append(cartItem)
                    print("produit:", cartItem.libelle, "ajouté")
                    break
                else:
                    for k in range(len(cart)):
                        if(cart[k].id_produit == produit.id_produit):
                            cart[k].quantiteToCart += nbr
                            print("produit:", cart[k].libelle, "existait déjà dans le panier. Nbr incrementé a:", cart[k].quantiteToCart)
                            break
                        else:
<<<<<<< HEAD
                            cart.append(produit)
                            print("produit supplementaire:", produit.libelle, "ajouté")
                            break


    def supprimer_produit(self, produit, list_panier):
=======
                            produit.quantiteToCart += nbr 
                            cart.append(produit)
                            print("produit supplementaire:", produit.libelle, "ajouté")
                            break
        print(f"Le produit '{produit.libelle}' a été ajouté à votre panier.")



    def supprimer_produit(self, produit, list_panier, listProduit):
        qte = 0
>>>>>>> bd851f214da99333d707a6988427614a6c388c6d
        for i in range(len(list_panier)):
            if(list_panier[i].id == self.id_panier):
                cart = list_panier[i].cart
                for k in range(len(cart)):
                        if(cart[k].id_produit == produit.id_produit):
                            cart.remove(produit)
<<<<<<< HEAD
                            print(f"Le produit avec le nom '{produit.libelle}' a été supprimé du panier. Nbr: {produit.quantiteToCart}")
                            break

    def passer_commande(self, list_panier) -> Commande:
=======
                            qte = produit.quantiteToCart
                            print(f"Le produit avec le nom '{produit.libelle}' a été supprimé du panier. Nbr: {produit.quantiteToCart}")
                            break
        for k in range(len(listProduit)):
                        if(listProduit[k].id_produit == produit.id_produit):
                            listProduit[k].quantiteProduit += qte
                            break
    
    def passer_commande(self, list_panier) -> Commande | None:
>>>>>>> bd851f214da99333d707a6988427614a6c388c6d
        # Implémentez ici la logique pour passer une commande, par exemple, enregistrer la commande dans une base de données.
        montant_total = 0
        indexPanier = -1
        for i in range(len(list_panier)):
            if(list_panier[i].id == self.id_panier):
                cart = list_panier[i].cart
                indexPanier = i
                for k in range(len(cart)):
                    produit = cart[k]
                    montant_total+= produit.quantiteToCart * produit.prix
        
<<<<<<< HEAD
        print(f"Votre commande contient {len(list_panier[indexPanier].cart)} produit(s). Le montant total fait: {montant_total} FCFA.")
        # list_panier[indexPanier] = []
        return Commande(self.id_panier, self.id_user, datetime.now, montant_total, status=Status.En_cours)
=======
        if montant_total > 0:
          print(f"Votre commande contient {len(list_panier[indexPanier].cart)} produit(s). Le montant total fait: {montant_total} FCFA.")        
          return Commande(self.id_panier, self.id_user, datetime.now, montant_total, status=Status.En_cours)
        
        return None
>>>>>>> bd851f214da99333d707a6988427614a6c388c6d

    def passer_commande_direct(self, produit: Produit, nbr) -> Commande:
        montant_total = produit.prix * nbr
        return Commande(self.id_panier, self.id_user, datetime.now, montant_total, status=Status.En_cours)
    
    def effectuer_paiement(self, solde, commande: Commande, listCommande):
        if(solde < commande.montant):
            print("Votre solde est insuffisant !")
<<<<<<< HEAD
        else:
            listCommande.append(commande)
            print(f"La commande a ete payee avec un montant de {commande.montant} FCFA.")
   
=======
            return False
        else:
            listCommande.append(commande)
            print(f"La commande a ete payee avec un montant de {commande.montant} FCFA.")
            return True
>>>>>>> bd851f214da99333d707a6988427614a6c388c6d
