class User: 
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name} Balance: ${self.account_balance}")

    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawal(amount)

kenneth = User("kenneth", "kenneth@kenneth.com")
jane = User("jane", "jane@jane.com")
jonathon = User("jonathon", "jonathon@jonathon.com")

kenneth.make_deposit(1000000000)
kenneth.make_deposit(200)
kenneth.make_deposit(150)
kenneth.make_withdrawal(50)
kenneth.display_user_balance()

jane.make_deposit(50)
jane.make_deposit(1000)
jane.make_withdrawal(500)
jane.make_withdrawal(100)
jane.display_user_balance()

jonathon.make_deposit(100)
jonathon.make_withdrawal(25)
jonathon.make_withdrawal(25)
jonathon.make_withdrawal(25)
jonathon.display_user_balance()

kenneth.transfer_money(jonathon,275000)
kenneth.display_user_balance()
jonathon.display_user_balance()
