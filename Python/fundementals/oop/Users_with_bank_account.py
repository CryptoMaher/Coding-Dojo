class User:
    def _init_(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)


def make_deposit(self, amount):
    self.account.deposit(amount)
    return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self 

    def display_user_balance(self):
        print(self.name)
        self.account.display_account_info()
        return self






class BankAccount:
    accounts = []
    def _init_(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

        def deposit(self, amount):
            self.balance += amount
            return self

    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficent Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yeild_intrest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
            return self


    @classmethod
    def print_all_accounts(cls):
        for account in cls.account:
            account.display_account_info()

user1 = User("Aziz", "aziz.com")
user1.make_deposit(100).make_deposit(250).display_user_balance()

user2 = User("Badyss","badyss.com")
user2.make_deposit(1000). display_user_balance().withdraw(450).display_user_balance
