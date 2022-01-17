class User:

    def __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.account_balance = 0

    def greeting(self):
        print(f"Welcome back, {self.first_name}")

    def make_deposit(self, amount):
        self.account_balance += amount

# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
    def make_withdrawal(self, amount):
        self.account_balance -= amount

# display_user_balance(self) - have this method print the user's name and account balance to the terminal
    def display_user_balance(self):
        print(f"User: {self.first_name} {self.last_name}, Balance: {self.account_balance}")

# BONUS: transfer_money(self, other_user, amount)
# have this method decrease the user's balance by the amount and add that amount to other other_user's balance
    def transfer_money(self, amount, other_user):
        self.account_balance -= amount
        other_user.account_balance += amount
        self.display_user_balance()
        other_user.display_user_balance()


James = User("James", "Holden", "jamesholden@expanse.com")
Naomi = User("Naomi", "Nagata", "naominagata@expanse.com")
Camina = User("Camina", "Drummer", "caminadrummer@expanse.com")

James.make_deposit(500)
James.make_deposit(32)
James.make_deposit(290)
James.make_withdrawal(100)
James.display_user_balance()

Naomi.make_deposit(1000)
Naomi.make_deposit(312)
Naomi.make_withdrawal(200)
Naomi.make_withdrawal(25)
Naomi.display_user_balance()

Camina.make_deposit(3000)
Camina.make_withdrawal(200)
Camina.make_withdrawal(20)
Camina.make_withdrawal(150)
Camina.display_user_balance()

James.transfer_money(200, Camina)