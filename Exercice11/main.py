# Écrivez votre code ici !


class BankAccount():
    def __init__(self, account_holder: str, balance: float):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
        else:
            print("Erreur: Le montant du dépôt doit être positif.")

    def withdraw(self, amount: float):
        if amount > 0:
            if self.balance - amount < 0:
                print("Erreur: Solde insuffisant")
            else:
                self.balance -= amount
        else:
            print("Erreur: Le montant du retrait doit être positif.")

    def display_balance(self):
        print(f"Nom : {self.account_holder}"
              f"\nSolde : {self.balance}"
              )


print("\nTest de l'instanciation et affichage du solde")
test = BankAccount("Jean", 200)
test.display_balance()

print("\nTest de la méthode de dépôt (100) et affichage du solde")
test.deposit(100)
test.display_balance()

print("\nTest de la méthode de retrait (150) et affichage du solde")
test.withdraw(150)
test.display_balance()

print("\nTest de la méthode de dépôt négatif (-150) et affichage du solde")
test.deposit(-100)
test.display_balance()

print("\nTest de la méthode de retrait négatif (-100) et affichage du solde")
test.withdraw(-100)
test.display_balance()

print("\nTest de la méthode de retrait (1000) pour un "
      "solde négatif et affichage du solde")
test.withdraw(1000)
test.display_balance()
