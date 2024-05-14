class Panier:
    def __init__(self):
        self.produits = []
    # la fonction ^pour ajouter les prduit au panier
    def ajouter_produit(self, nom_produit):
        self.produits.append({"nom": nom_produit})
    # fonction suppression
    def supprimer_produit(self, index):
        if self.verifie_panier():
            if index >= 0 and index < len(self.produits):
                del self.produits[index]
    # FOUNCTION MODIFICATION
    def modifier_produit(self, index, nom_produit):
        if self.verifie_panier():
            if index >= 0 and index < len(self.produits):
                self.produits[index] = {"nom": nom_produit,}

    def verifie_panier(self):
        if not self.produits:
            print("Le panier est vide")
            return False
        return True

# Exemple d'utilisation
panier = Panier()
print("ajouter un prduit au panier")
panier.ajouter_produit("Pc")
panier.ajouter_produit("Téléphone")
panier.ajouter_produit("SACK")

#enummuration des produit dans panier
print("Produits dans le panier :")
for i, produit in enumerate(panier.produits):
    print(f"{i+1}. {produit['nom']} ")

# Afficher total des produits
print(f"Total des produits : ")

panier.modifier_produit(1, "Souris")
print("\nProduits modifiés dans le panier :")
for i, produit in enumerate(panier.produits):
    print(f"{i+1}. {produit['nom']} ")

# Afficher total des produits après modification


panier.supprimer_produit(2)
print("\nProduits restants dans le panier :")
for i, produit in enumerate(panier.produits):
    print(f"{i+1}. {produit['nom']} ")

# Afficher total des produits  apres suppression
