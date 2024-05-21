#Les classes importées
from datetime import date, datetime
import getpass
from categorie import Categorie
from personnel import Personnel
from role import Role
from produit import Produit
from admin import Admin
from panier import Panier
from client import Client
from status import Status

# Variables globales
donnees_personnel = [
    Personnel(1, "Daou", "Mariame", "mdp", "telephone", Role.Personnel)
]
products = [
    Produit(1,"PC","",1000, 1, 20, 1),
    Produit(2,"Mercedes","",30000, 2, 20, 1),
    Produit(3,"TELEPHONE","",1000, 1, 20, 1),
    Produit(4,"Candia","",600, 3, 40, 1),
    Produit(5,"Montre","",1000, 4, 20, 1),
    Produit(6,"Tecno","",1000, 1, 20, 1)
]

Listeclient = [
    Client(1, "Daou", "Mariame", "mdp1", "76435353", Role.Client, 1),
    Client(2, "Konate", "Adama", "mdp2", "76435353", Role.Client, 2),
    Client(3, "Client3", "prenom", "mdp3", "76435353", Role.Client, 3),
    Client(4, "Client4", "prenom", "mdp4", "76435353", Role.Client, 4),
    Client(5, "Client5", "prenom", "mdp5", "76435353", Role.Client, 5),
    Client(6, "Client6", "prenom", "mdp6", "76435353", Role.Client, 6),
]

list_panier = [
    Panier(1),
    Panier(2),
    Panier(3),
    Panier(4),
    Panier(5),
    Panier(6),
]

liste_commande = []

categories = [
    Categorie(1, "Electronique"),
    Categorie(2, "Voiture"),
    Categorie(3, "Lait"),
    Categorie(4, "Accessoire")
]

liste_admin = [
    Admin(1, "Thera", "Badra", "mdp", "12345678"),
    Admin(2, "Diallo", "Harouna", "mdp", "3234356"),
    Admin(3, "Sissoko", "Adama", "mdp", "3234356")
]

# Fonction pour afficher le menu (tableau de bord de l'admin)
def afficher_menu():
    print("\n***Options***\n:")
    print("1. Ajouter un produit")
    print("2. Modifier un produit")
    print("3. Supprimer un produit")
    print("4. Voir la liste des produits")
    print("5. Ajouter un personnel")
    print("6. Modifier un personnel")
    print("7. Supprimer un personnel")
    print("8. Voir la liste des personnel")
    print("9. Quitter")
    print("10. Changer d'utilisateur")
    # print("10. Ajouter un produit au panier")

# Fonction pour choisir une catégorie
def choisir_categorie():
    print("\nChoisissez la catégorie du produit")
    for i, categorie in enumerate(categories, 1):
        print(f"{i}. {categorie.nom}")
    choix_categorie = int(input("Votre choix (1-4): "))
    if 1 <= choix_categorie <= len(categories):
        return categories[choix_categorie - 1]
    else:
        print("Catégorie invalide.")
        return None

# Fonction pour gerer la connexion des admins
def verifier_presence_admin():
    print("\n ***Connexion*** \n")
    nom_admin = input("veillez saisir votre nom: ")
    mdp_admin = getpass.getpass("veillez saisir votre mot de passe: ")
    admin_operant = next((a for a in liste_admin if a.nom == nom_admin and a.mot_de_pass == mdp_admin), None)
    if admin_operant:
        print("\n ***Bienvenu(e) Administrateur ", admin_operant.prenom, "!*** \n")
        main(admin_operant)
    else:
        print("Le nom ou le mot de passe incorrect, veuillez vous rassurer que vous avez bien saisi les caracteres.")
        print("\n***Options***\n:")
        print("1. Réessayer")
        print("Autre. Quitter")
        choix = input("Entrez votre choix: ")
        if choix == '1':
            verifier_presence_admin()

# Fonction pour gerer la connexion des personnel
def verifier_presence_personnel():
    print("\n ***Connexion*** \n")
    nom_personnel = input("veillez saisir votre nom: ")
    mdp_personnel = getpass.getpass("veillez saisir votre mot de passe: ")
    personnel_operant = next((a for a in donnees_personnel if a.nom == nom_personnel and a.mot_de_pass == mdp_personnel), None)
    if personnel_operant:
        print("\n ***Bienvenu(e) Personnel", personnel_operant.prenom, "!*** \n")
        main_personnel(personnel_operant)
    else:
        print("Le nom ou le mot de passe incorrect, veuillez vous rassurer que vous avez bien saisi les caracteres.")
        print("\n***Options***\n:")
        print("1. Réessayer")
        print("Autre. Quitter")
        choix = input("Entrez votre choix: ")
        if choix == '1':
            verifier_presence_personnel()

# Fonction pour gerer la connexion des client
def verifier_presence_client() -> Client:
    print("\n***Connexion***\n")
    nom_client = input("veillez saisir votre nom: ")
    mdp_client = getpass.getpass("veillez saisir votre mot de passe: ")
    client_operant = next((a for a in Listeclient if a.nom == nom_client and a.mot_de_pass == mdp_client), None)
    if client_operant:
        print(f"\n*** Bienvenu(e)  {client_operant.prenom}, ravi de vous revoir! ***\n")
        return client_operant
        # main_client()
    else:
        print("Le nom ou le mot de passe incorrect, veuillez vous rassurer que vous avez bien saisi les caracteres.")
        print("\n ***Options*** \n:")
        print("1. Réessayer")
        print("Autre. Quitter")
        choix = input("Entrez votre choix: ")
        if choix == '1':
            verifier_presence_client()

# Fonction principale (tableau de bord de l'admin)
def main(admin_operant: Admin):
    while True:
        afficher_menu()
        choix = input("Choisissez une option entre 1-10 : ").strip()
# Ajouter un produit
        if choix == '1':
            try:
                admin = admin_operant
                
                libelle = input("Entrez le nom du produit: ")
                prix = float(input("Entrez le prix du produit: "))
                categorie = choisir_categorie()
                if categorie:
                    quantiteProduit = int(input("Entrez la quantité disponible du produit: "))
                    
                    id_produit = len(products) + 1
                    id_admin = admin.id_user
                    produit = admin.creer_produit(id_produit, id_admin, libelle, date.today(), prix, categorie, quantiteProduit)
                    admin.ajouter_produit(produit, products)
            except ValueError:
                print("Entrée invalide. Veuillez entrer des valeurs correctes.")
#Modifier un produit
        elif choix == '2':
            try:
                print("\n** Modification d'un produit\n**")
                id_produit = int(input("Entrez l'ID du produit à modifier: "))
                produit = next((p for p in products if p.id_produit == id_produit), None)
                if produit:
                    libelle = input("Entrez le nouveau nom du produit: ")
                    prix = float(input("Entrez le nouveau prix du produit: "))
                    categorie = choisir_categorie()
                    if categorie:
                        quantiteProduit = int(input("Entrez la nouvelle quantité disponible du produit: "))
                        new_produit = Produit(produit.id_produit, libelle, date.today(), prix, categorie.id, quantiteProduit, produit.id_admin)
                       
                        admin_operant.modifier_produit(produit, new_produit, products)
                else:
                    print("Produit non trouvé.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer des valeurs correctes.")
#Supprimer un produit      
        elif choix == '3':
            try:
                id_produit = int(input("Entrez l'ID du produit à supprimer: "))
                produit = next((p for p in products if p.id_produit == id_produit), None)
                if produit:
                   
                    admin_operant.supprimer_produit(produit, products)
                else:
                    print("Produit non trouvé.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer des valeurs correctes.")
#Supprimer un produit      
            
#Voir la liste des produits      
        elif choix == '4':
            try:
                print("\nListe des produits:")
                for p in products:
                    print(f"ID: {p.id_produit}, Nom: {p.libelle}, Date: {p.date}, Prix: {p.prix}, Quantité: {p.quantiteProduit}, ID Admin: {p.id_admin}")
            except ValueError:
                print("Entrée invalide. Veuillez entrer des valeurs correctes.")
        #Ajouter un personnel
              
        elif choix == '5':
            try: 
               
                admin = admin_operant
           

                id_personnel = len(donnees_personnel) + 1
                nom = input("Entrez le nom de l'utilisateur: ")
                prenom = input("Entrez le prénom de l'utilisateur: ")
                mot_de_passe = input("Entrez le mot de passe de l'utilisateur: ")
                telephone = input("Entrez le téléphone de l'utilisateur: ")
                role = Role.Personnel
                admin.Ajouter_utilisateur(id_personnel, nom, prenom, mot_de_passe, telephone, role, donnees_personnel)
            except ValueError:
                print("Entrée invalide. Veuillez entrer des valeurs correctes.")

#Modifier un prsonnel     
        elif choix == '6':
            try:
                id_personnel = int(input("Entrez l'ID de l'utilisateur à modifier: "))
                personnel = next((p for p in donnees_personnel if p.id_user == id_personnel), None)
                if personnel:
                    nom = input("Entrez le nouveau nom de l'utilisateur: ")
                    prenom = input("Entrez le nouveau prénom de l'utilisateur: ")
                    mot_de_passe = input("Entrez le nouveau mot de passe de l'utilisateur: ")
                    telephone = input("Entrez le nouveau téléphone de l'utilisateur: ")
                    role = Role.Personnel
                    new_personnel = Personnel(id_personnel, nom, prenom, mot_de_passe, telephone, role)
                    # admin = next((a for a in [adminThera, adminHarouna] if a.id_user == personnel.id_user), None)
                    admin = admin_operant
                    if admin:
                        admin.modifier_utilisateur(personnel, new_personnel, donnees_personnel)
                else:
                    print("Utilisateur non trouvé.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer des valeurs correctes.")
#Supprimer un produit      
    #Supprimer un prsonnel       
        elif choix == '7':
            try:
                id_personnel = int(input("Entrez l'ID de l'utilisateur à supprimer: "))
                personnel = next((p for p in donnees_personnel if p.id_user == id_personnel), None)
                if personnel:
                    # admin = next((a for a in [adminThera, adminHarouna] if a.id_user == personnel.id_user), None)
                    admin = admin_operant
                    if admin:
                        admin.Supprimer_utilisateur(id_personnel, donnees_personnel)
                        print('Personnel supprimer avec succés')
                else:
                    print("Utilisateur non trouvé.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer des valeurs correctes.")
#Supprimer un produit      
#Voir la liste des personnel       
        elif choix == '8':
            try:
                print("\n**Liste des utilisateurs**\n")
                if not donnees_personnel:
                    print("Liste vide !")
                for p in donnees_personnel:
                    print(f"ID: {p.id_user},  {p.id_user} nom : {p.nom} prenom : {p.prenom} role est: {p.role_str()}")
            except ValueError:
                print("Entrée invalide. Veuillez entrer des valeurs correctes.")
#Supprimer un produit      
    #Pour quitter
        elif choix == '9':
            print("Au revoir!")
            break
#Changer le role 
        elif choix=='10':
            role = input("Entrez votre rôle (admin/personnel:client): ").lower()
            if role == 'admin':
                verifier_presence_admin()
            elif role == 'client':
                main_client(None)
            elif role == 'personnel':
                # main_personnel()
                verifier_presence_personnel()
            else:
                print("Rôle invalide.")

        else:
            print("Option invalide, veuillez réessayer.")


# Fonction pour obtenir les informations du client
def obtenir_informations_client(id_client):
    nom = input("Entrez votre nom : ")
    prenom = input("Entrez votre prénom : ")
    telephone = input("Entrez votre numéro de téléphone : ")
    return Client(id_client, nom, prenom, telephone)

# Fonction pour afficher le menu du client
def afficher_menu_client():
    print("\nOptions:")
    print("1. Ajouter un produit au panier")
    print("2. VOIR PRODUIT")
    print("3. VOIR PANIER")
    print("4. SUPPRIMER PANIER")
    print("5. Passée commande avec le panier")
    print("6. Passée commande en direct")
    print("7. Quitter")
    print("8. CHARGER UTILISATEUR")

# Fonction principale pour le client (tableau de bord du client).
def main_client(client_operant: Client | None):
    client = client_operant
    while True:
        afficher_menu_client()
        choix = input("Choisissez une option: ").strip()
#Ajouter un produit au panier
        if choix == '1':
            try:
                if not client:
                    print("\n*** Seuls les clients ayant un compte possedent un panier. ***")
                    print("\n ***Options*** \n:")
                    print("1. Se connecter")
                    print("2. S'inscrire")
                    print("3. Quitter")
                

                    option = input("Choisissez une option (1-4): ").strip()
                    if option == '1':
                        client = verifier_presence_client()
                        pass
                    elif option == '2':
                        client = saisir_nouveau_client()
                        print('Inscription reussi avec succés')
                        pass
                    elif option == '3':
                        print("A bientôt !")
                        break
                    else:
                        main_client(None)

                libelle = input("Entrez le nom du produit à ajouter au panier: ")
                # produit = next((p for p in products if p.libelle == libelle), None)
                produit= None
                for p in products:
                    if p.libelle.lower() == libelle.lower():
                        produit = p
                if produit:
                    nbr = int(input("Entrez la quantité à ajouter au panier: "))
                    if nbr <= 0:
                        print("Refléchit un peu !")
                    elif nbr <= produit.quantiteProduit:
                        # print(nbr)
                        client.ajouter_produit_panier(produit, nbr,list_panier)
                        produit.quantiteProduit -= nbr
                        print("Produit ajouté au panier avec succès.")
                    else:
                        print("Quantité insuffisante en stock.")
                else:
                    print("Produit non trouvé.")
                    main_client(client)
            except ValueError:
                print("Entrée invalide. Veuillez entrer des valeurs correctes.")
#La liste des produits
        elif choix == '2':
            print("\nListe des produits:")
            for p in products:
                print(f"ID: {p.id_produit}, Nom: {p.libelle}, Date: {p.date}, Prix: {p.prix}, Quantité: {p.quantiteProduit}, ID Admin: {p.id_admin}")
        elif choix == '3':
            
            print(client)
            if not client:
                print("\n*** Seuls les clients ayant un compte possedent un panier. ***")
                print("\n ***Options*** \n:")
                print("1. Se connecter")
                print("2. S'inscrire")
                print("3. Quitter")
               

                option = input("Choisissez une option (1-4): ").strip()
                if option == '1':
                    client = verifier_presence_client()
                    pass
                elif option == '2':
                    client = saisir_nouveau_client()
                    pass
                elif option == '3':
                    print("A bientôt !")
                    break
                else:
                    main_client(None)
#Ajouter au panier               
            print("\n** PANIER **\n")
            for p in range(len(list_panier)):
               if(client.id_panier == list_panier[p].id):
                   cart = list_panier[p]

                   if not cart.cart:
                       print("Le panier ne contient aucun produit.")
                       main_client(client)
                       
                   for i in range(len(cart.cart)):
                       print(f"nom: {cart.cart[i].libelle} prix: {cart.cart[i].prix} quantite: {cart.cart[i].quantiteToCart}")
                       main_client(client)

        elif choix == '4':
            
            if not client:
                print("\n*** Seuls les clients ayant un compte possedent un panier. ***")
                print("\n ***Options*** \n:")
                print("1. Se connecter")
                print("2. S'inscrire")
                print("3. Quitter")
                print("autre. Retour")

                option = input("Choisissez une option: ").strip()
                if option == '1':
                    client = verifier_presence_client()
                    pass
                elif option == '2':
                    client = saisir_nouveau_client()
                    pass
                elif option == '3':
                    print("A bientôt !")
                    break
                else:
                    main_client(None)

            nom_produit = input("Entrez le nom du produit à supprimer du panier: ")
            produit = None
            for p in products:
                if p.libelle == nom_produit:
                    produit = p
            if produit:
                client.supprimer_produit(produit, list_panier, products)
                main_client(client)
            else:
                print("Aucun produit à supprimer !")
                main_client(client)
        elif choix == '5':
            try:
                commande = None    
                
                if not client:
                    print("\n*** Seuls les clients ayant un compte possedent un panier. ***")
                    print("\n ***Options*** \n:")
                    print("1. Se connecter")
                    print("2. S'inscrire")
                    print("3. Quitter")
                    print("autre. Retour")

                    option = input("Choisissez une option (1-4): ").strip()
                    if option == '1':
                        client = verifier_presence_client()                                       
                    elif option == '2':
                        client = saisir_nouveau_client()
                    elif option == '3':
                        print("A bientôt !")
                        break
                    else:
                        main_client(None)
    #Passer une commande avec le panier
                commande = client.passer_commande(list_panier)
                if commande:
                    reponses=input("\n**Prosseder au payement ?**\nSaisir: oui ou non: ").lower()
                    while True:
                        if(reponses=='oui'):
                            vider_panier = client.effectuer_paiement(int(input("votre solde ?")), commande, liste_commande)
                            if vider_panier:
                                for i in range(len(list_panier)):
                                    if(list_panier[i].id == client.id_panier):
                                        list_panier[i].cart = []

                            main_client(client)
                            break
                        elif(reponses == 'non'):
                            print("Merci! Nous esperons vous revoir bientôt.")
                            main_client(client)
                            break
                        reponses=input("Saisir: oui ou non pour confirmer votre choix ").lower()
                else:
                    print("\n**Panier vide**\n")
                main_client(client)         
            except ValueError:
                print("Entrée invalide. Veuillez entrer des valeurs correctes.")
#Supprimer un produit      
        elif choix == '6':
            try:
                if not client:
                    print("\n*** Seuls les clients ayant un compte peuvent effecuer cette opperation. ***")
                    print("\n ***Options*** \n:")
                    print("1. Se connecter")
                    print("2. S'inscrire")
                    print("3. Quitter")
                

                    option = input("Choisissez une option: ").strip()
                    if option == '1':
                        client = verifier_presence_client()                                       
                    elif option == '2':
                        client = saisir_nouveau_client()
                    elif option == '3':
                        print("A bientôt !")
                        break
                    else:
                        main_client(None)

                # Passer une commande directement
                libelle = input("Entrez le nom du produit à commander: ")
                produit = next((p for p in products if p.libelle == libelle), None)
                if produit:
                    nbr = int(input("Entrez la quantité à commander: "))
                    # commande = client.passer_commande_direct(produit,datetime.now, quantite)
                    if nbr <= produit.quantiteProduit:
                        commande = client.passer_commande_direct(produit, nbr)
                        produit.quantiteProduit -= nbr
                        if commande:
                            reponses=input("\n**Prosseder au payement ?**\nSaisir: oui ou non: ").lower()
                            while True:
                                if(reponses=='oui'):
                                    client.effectuer_paiement(int(input("votre solde ? ")), commande, liste_commande)
                                    main_client(client)
                                    break
                                elif(reponses == 'non'):
                                    print("Merci! Nous esperons vous revoir bientôt.")
                                    main_client(client)
                                    break
                                reponses=input("Saisir: oui ou non pour confirmer votre choix ").lower()
                    else:
                        print("Quantité insuffisante en stock.")
                    
                else:
                    print("Produit non trouvé.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer des valeurs correctes.")
#Supprimer un produit      
        elif choix == '7':
            print("Au revoir!")
            break
        elif choix=='8':
            role = input("Entrez votre rôle (admin/personnel/client): ").lower()
            if role == 'admin':
                verifier_presence_admin()
            elif role == 'client':
                main_client(client_operant)
            elif role == 'personnel':
                verifier_presence_personnel()
        
        else:
            print("Option invalide, veuillez réessayer.")

# Fonction pour saisir les informations d'un nouveau client
def saisir_nouveau_client():
    id_client = len(Listeclient) + 1
    nom = input("Entrez votre nom : ")
    prenom = input("Entrez votre prénom : ")
    mot_de_pass = input("Entrez votre mot_de_passe : ")
    telephone = input("Entrez votre numéro de téléphone : ")
    role = Role.Client
    if(len(Listeclient) > 5):
        id_panier = len(list_panier) + 1  # Nouvel identifiant de panier unique
    else:
        id_panier = 1    
    return Client(id_client, nom, prenom,mot_de_pass, telephone, role, id_panier)

def afficher_menuPERSONNEL():
    print("\n** Options **")
    print("1. Charger les statuts de la commande")
    print("2. Voir les commandes")
    print("3. Quitter")
    print("4. CHANGER")

# (tableau de bord du personnel)
def main_personnel(personnel_operant: Personnel|None):
    personnel = personnel_operant
    while True:
        afficher_menuPERSONNEL()
        choix = input("Choisissez une option: ").strip()

        if choix == '1':
            if not liste_commande:
                print("\n**Aucune commande**\n")
                continue  # Retourne au menu principal

            while True:
                try:
                    id_commande = int(input("Choisissez le numéro: ").strip())
                    if 1 <= id_commande <= len(liste_commande):
                        break
                    else:
                        print("Veuillez choisir un numéro de commande valide.")
                except ValueError:
                    print("Veuillez entrer un nombre valide.")

            commande_occurante = liste_commande[id_commande - 1]
            if commande_occurante:
                # Demander le nouveau statut
                print("Choisir le nouveau statut de la commande: ")
                print("1 : En cours")
                print("2 : Terminé")
                Choice = input("Choisissez une option: ").strip()
                if Choice == "1":
                    commande_occurante.update_status(commande_occurante, Status.En_cours)
                    print("Statut modifié !")
                    print(commande_occurante)
                elif Choice == "2":
                    personnel.changer_status_commande(commande_occurante, Status.Termine)
                    print("Statut modifié !")
                    print(commande_occurante)

        elif choix == '2':
            if not liste_commande:
                print("\n**Aucune commande**\n")
            else:
                for c in range(len(liste_commande)):
                    print(f"Commande n°{c + 1}, panier_id: {liste_commande[c].id_Panier}, ID Client: {liste_commande[c].id_client}, Montant: {liste_commande[c].montant}, Statut: {liste_commande[c].status.value}")
        elif choix == '3':
            print("*** Fin de programme ***")
            break
        elif choix == '4':
            role = input("Entrez votre rôle (admin/personnel/client): ").lower()
            if role == 'admin':
                verifier_presence_admin()
            elif role == 'client':
                main_client()
            elif role == 'personnel':
                verifier_presence_personnel()
        else:
            print("Identifiant invalide. Veuillez réessayer.")



if __name__ == "__main__":
    print('***Bienvenue dans notre système de gestion de commerce en ligne***')
    role = input("Veuillez indiquer votre rôle (admin/personneL/client): ").lower()
    if role == 'admin':
        # main()
        verifier_presence_admin()
    elif role == 'client':
        main_client(None)
    elif role == 'personnel':
        verifier_presence_personnel()
    else:
        print("Rôle invalide.")
        