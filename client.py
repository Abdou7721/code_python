from datetime import date
from categorie import Categorie
from personnel import Personnel
from role import Role
from user import User
from produit import Produit
from admin import Admin

# Variables globales
donnees_personnel = []
products = []
categories = [
    Categorie(1, "Electronique"),
    Categorie(2, "Voiture"),
    Categorie(3, "Lait"),
    Categorie(4, "Accessoire")
]

# Création des admins
adminThera = Admin(1, "Thera", "Badra", "mot_de_passe", "12345678")
adminHarouna = Admin(2, "Diallo", "Harouna", "mdp", "3234356")

# Fonction pour afficher le menu
def afficher_menu():
    print("\nOptions:")
    print("les option de l'administrateur")
    print("1. Ajouter un produit")
    print("2. Modifier un produit")
    print("3. Supprimer un produit")
    print("4. Voir la liste des produits")
    print("5. Ajouter un personnel")
    print("6. Modifier un personnel")
    print("7. Supprimer un personnel")
    print("8. Voir la liste des personnel")
    print("9. Quitter")
    print("10. Ajouter prduit au panier")
    


# Fonction pour choisir une catégorie
def choisir_categorie():
    print("Choisissez la catégorie du produit:")
    for i, categorie in enumerate(categories, 1):
        print(f"{i}. {categorie.nom}")
    choix_categorie = int(input("Votre choix (1-4): "))
    if 1 <= choix_categorie <= len(categories):
        return categories[choix_categorie - 1]
    else:
        print("Catégorie invalide.")
        return None

# Fonction principale
def main():
    while True:
        afficher_menu()
        choix = input("Choisissez une option (1-10): ").strip()

        if choix == '1':
            admin_id = input("Entrez votre identifiant d'administrateur: ")
            admin = None
            if admin_id == str(adminThera.id_user):
                admin = adminThera
            elif admin_id == str(adminHarouna.id_user):
                admin = adminHarouna
            else:
                print("Identifiant d'administrateur invalide.")
                continue
            
            libelle = input("Entrez le nom du produit: ")
            prix = float(input("Entrez le prix du produit: "))
            quantite_produit = int(input("Entrez la quantité disponible du produit: "))
            categorie = choisir_categorie()
            if categorie:
                id_produit = len(products) + 1
                produit = admin.creer_produit(id_produit, libelle, date.today(), prix, categorie, quantite_produit, admin.id_user)
                admin.ajouter_produit(produit, products)
        
        elif choix == '2':
            id_produit = int(input("Entrez l'ID du produit à modifier: "))
            produit = next((p for p in products if p.id_produit == id_produit), None)
            if produit:
                libelle = input("Entrez le nouveau nom du produit: ")
                prix = float(input("Entrez le nouveau prix du produit: "))
                quantite_produit = int(input("Entrez la nouvelle quantité disponible du produit: "))
                categorie = choisir_categorie()
                if categorie:
                    new_produit = Produit(produit.id_produit, libelle, date.today(), prix, categorie.id, quantite_produit, produit.id_admin)
                    admin = next((a for a in [adminThera, adminHarouna] if a.id_user == produit.id_admin), None)
                    if admin:
                        admin.modifier_produit(produit, new_produit, products)
            else:
                print("Produit non trouvé.")
        
        elif choix == '3':
            id_produit = int(input("Entrez l'ID du produit à supprimer: "))
            produit = next((p for p in products if p.id_produit == id_produit), None)
            if produit:
                admin = next((a for a in [adminThera, adminHarouna] if a.id_user == produit.id_admin), None)
                if admin:
                    admin.supprimer_produit(produit, products)
            else:
                print("Produit non trouvé.")
        
        elif choix == '4':
            print("\nListe des produits:")
            for p in products:
                print(f"ID: {p.id_produit}, Nom: {p.libelle}, Date: {p.date}, Prix: {p.prix}, Quantité: {p.quantiteProduit}, ID Admin: {p.id_admin}")
        
        elif choix == '5':
            admin_id = input("Entrez votre identifiant d'administrateur: ")
            admin = None
            if admin_id == str(adminThera.id_user):
                admin = adminThera
            elif admin_id == str(adminHarouna.id_user):
                admin = adminHarouna
            else:
                print("Identifiant d'administrateur invalide.")
                continue

            id_personnel = len(donnees_personnel) + 1
            nom = input("Entrez le nom de l'utilisateur: ")
            prenom = input("Entrez le prénom de l'utilisateur: ")
            mot_de_passe = input("Entrez le mot de passe de l'utilisateur: ")
            telephone = input("Entrez le téléphone de l'utilisateur: ")
            role = Role.Personnel
            admin.Ajouter_utilisateur(id_personnel, nom, prenom, mot_de_passe, telephone, role, donnees_personnel)

        
        elif choix == '6':
            id_personnel = int(input("Entrez l'ID de l'utilisateur à modifier: "))
            personnel = next((p for p in donnees_personnel if p.id_user == id_personnel), None)
            if personnel:
                nom = input("Entrez le nouveau nom de l'utilisateur: ")
                prenom = input("Entrez le nouveau prénom de l'utilisateur: ")
                mot_de_passe = input("Entrez le nouveau mot de passe de l'utilisateur: ")
                telephone = input("Entrez le nouveau téléphone de l'utilisateur: ")
                role = Role.Personnel
                new_personnel = Personnel(id_personnel, nom, prenom, mot_de_passe, telephone, role)
                admin = next((a for a in [adminThera, adminHarouna] if a.id_user == personnel.id_user), None)
                if admin:
                    admin.modifier_utilisateur(personnel, new_personnel, donnees_personnel)
            else:
                print("Utilisateur non trouvé.")
        
        elif choix == '7':
            id_personnel = int(input("Entrez l'ID de l'utilisateur à supprimer: "))
            personnel = next((p for p in donnees_personnel if p.id_user == id_personnel), None)
            if personnel:
                admin = next((a for a in [adminThera, adminHarouna] if a.id_user == personnel.id_user), None)
                if admin:
                    admin.supprimer_utilisateur(id_personnel, donnees_personnel)
            else:
                print("Utilisateur non trouvé.")
        
        elif choix == '8':
            print("\nListe des utilisateurs:")
            for p in donnees_personnel:
                # print(f"ID: {p.id_user}, Nom: {p.nom}, Prénom: {p.prenom}, Téléphone: {p.telephone}, Role: {p.role}")
                print(f"ID: {p.id_user},  {p.id_user} nom : {p.nom} prenom : {p.prenom} role est: {p.role_str()}")
        
        elif choix == '9':
            print("Au revoir!")
            break
        elif choix == '10':
            # Ajouter produit au panier
            libelle = str(input("Entrez le nom du produit à ajouter au panier: "))
            produit = next((p for p in products if p.libelle == libelle), None)
            if produit:
                quantite = int(input("Entrez la quantité à ajouter au panier: "))
                if quantite <= produit.quantiteProduit:
                    user_id = input("Entrez votre identifiant d'utilisateur: ")
                    user = None
                   
                    if user:
                        user.ajouter_au_panier(produit, quantite)
                        produit.quantiteProduit -= quantite
                    else:
                        print("Utilisateur non trouvé.")
                else:
                    print("Quantité insuffisante en stock.")
            else:
                print("Produit non trouvé.")
        
        else:
            print("Option invalide, veuillez réessayer.")
       

        
if __name__ == "__main__":
    main()
