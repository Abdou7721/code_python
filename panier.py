class Panier:
    def __init__(self):
        self.produits = []
        self.etat_produit= False
    # la fonction ^pour ajouter les prduit au panier
    def ajouter_produit(self, nom_produit, prix_produit):
        self.produits.append({"nom": nom_produit, "prix": prix_produit})
    # fonction suppression
    def supprimer_produit(self, index):
        if self.verifie_panier():
            if index >= 0 and index < len(self.produits):
                del self.produits[index]
    # FOUNCTION MODIFICATION
    def modifier_produit(self, index, nom_produit, prix_produit):
        if self.verifie_panier():
            if index >= 0 and index < len(self.produits):
                self.produits[index] = {"nom": nom_produit, "prix": prix_produit}

    #fonction total produits
    def total_produits(self):
        total = 0
        for produit in self.produits:
            total += produit["prix"]
        return total
    # Vérification d'état du panier
    def verifie_panier(self):
        if not self.produits:
            print("Le panier est vide")
            return False
        return True

# Exemple d'utilisation
panier = Panier()

while True:
    choix= input("Que voulez vous faire ? '(1. ajouter/ 2. Modifier/ 3. supprimer/ 4. Afficher/ 5. quiter)")
    if choix== "1":
        nom_produit=input("Nom du produit")
        prix_produit = float(input("Prix du prix"))
        panier.ajouter_produit(nom_produit,prix_produit)
        print(f"Le Produit {nom_produit}, Le prix : {prix_produit} a été ajouté au panier ")
    elif choix == '2':
        index_produit= int(input("Index du produit"))
        nom_produit= input("Nouveau nom du prosuit")
        prix_produit = float(input("Nouveau prix du produit"))
        panier.modifier_produit(index_produit,prix_produit,prix_produit)
        print(f"Le produit a l'index {index_produit}, a été modifier ")
    elif choix == "3":
        index_produit= int(input("index du produit à suppriner"))
        panier.supprimer_produit(index_produit)
        print(f"Le produit à l'index {index_produit} a été supprimer")

    elif choix == "4":
        print('Produit dans le panier')
        for i, produit in enumerate(panier.produits):
            print(f"{i + 1}. {produit['nom']} - {produit['prix']}")
        print(f"Total des produit : {panier.total_produits()}")

    elif choix == "5":
        break
    else:
        print('Choix invalide veuillez réessayer.')
