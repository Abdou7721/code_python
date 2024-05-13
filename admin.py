from produit import Produit, Produit_Admin


class Admin:
    def __init__(self, id):
        self.id = id

    # Cette methode crée et retourne un produit.
    def creer_produit(self, id_produit, libelle, date, prix, id_categorie) -> Produit:
        produit = Produit(id_produit, libelle, date, prix, id_categorie)
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
            produit_admin = Produit_Admin(produit, self.id)
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