class Panier:
    def __init__(self):
        self.produits = []
        self.etat_produit= False
    # la fonction ^pour ajouter les prduit au panier
    def ajouter_produit(self, nom_produit, prix_produit):
        self.produits.append({"nom": nom_produit, "prix": prix_produit})
    # fonction suppression
    def supprimer_produit(self, index):
        if index >= 0 and index < len(self.produits):
            del self.produits[index]
    # FOUNCTION MODIFICATION
    def modifier_produit(self, index, nom_produit, prix_produit):
        if index >= 0 and index < len(self.produits):
            self.produits[index] = {"nom": nom_produit, "prix": prix_produit}

    #fonction total produits
    def total_produits(self):
        total = 0
        for produit in self.produits:
            total += produit["prix"]
        return total

# Exemple d'utilisation
panier = Panier()
print("ajouter un prduit au panier")
panier.ajouter_produit("Pc", 1000.08)
panier.ajouter_produit("Téléphone", 13000.100)
panier.ajouter_produit("SACK", 1000)

#enummuration des produit dans panier
print("Produits dans le panier :")
for i, produit in enumerate(panier.produits):
    print(f"{i+1}. {produit['nom']} - {produit['prix']}")

# Afficher total des produits
print(f"Total des produits : {panier.total_produits()} FCFA ")

panier.modifier_produit(1, "Souris", 2000)
print("\nProduits modifiés dans le panier :")
for i, produit in enumerate(panier.produits):
    print(f"{i+1}. {produit['nom']} - {produit['prix']} FCFA ")

# Afficher total des produits après modification
print(f"Total des produits après modification : {panier.total_produits()} FCFA")

panier.supprimer_produit(2)
print("\nProduits restants dans le panier :")
for i, produit in enumerate(panier.produits):
    print(f"{i+1}. {produit['nom']} - {produit['prix']} FCFA")

# Afficher total des produits  apres suppression
print(f"Total des produits après suppression : {panier.total_produits()} FCFA")