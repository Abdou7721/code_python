from datetime import date

class Payement:
    def __init__(self, id_payement, mode_payement, date_reglement, montant_paye):
        self.id_payement = id_payement
        self.mode_payement = mode_payement
        self.date_reglement = date_reglement
        self.montant_paye = montant_paye

    def effectuer_paiement(self):
        if self.montant_paye > 0:
            notification = Notification(id_notification=1, message=f"La commande a ete payee avec un montant de {self.montant_paye} FCFA.")
            notification.envoyerMessage()

class Notification(Payement):
    def __init__(self, id_notification, message):
        self.id_notification = id_notification
        self.message = message
    
    def envoyerMessage(self):
        print("Message :", self.message)

# Exemple de test
def test_notification_paiement():
    paiement = Payement(id_payement=1, mode_payement="Orange money", date_reglement=date.today(), montant_paye=5000)
    paiement.effectuer_paiement()

# Appel du test
test_notification_paiement()
