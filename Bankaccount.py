class BankAccount:
    def __init__(self, account_number:str, balance = 0.0, daily_limit = 1000.0):
        first_digits = account_number[0:2]
        if first_digits in ("BE","NL"):
            self.account_number = account_number
            self.balance = float(balance)
            self.daily_limit = float(daily_limit)
            self.amount_withdrawn_today = 0.0
        else:
            assert first_digits in ("BE","NL"), "Account nummer is niet geldig"

    def deposit(self, amount):
        assert amount > 0.0, "Bedrag moet positief zijn"
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if 0 < amount < self.balance and amount <= self.daily_limit:
            self.balance = self.balance - amount
            self.amount_withdrawn_today = self.amount_withdrawn_today + amount
            return True
        else:
            print("De betaling kan niet doorgaan")
            return False

    def reset_daily_limit(self):
        self.amount_withdrawn_today = 0.0

    def __str__(self):
        status = self.account_number + ", " + str(self.balance) + ", " + str(self.daily_limit)
        return status

    def getAccountNumber(self):
        return self.account_number






#account1 = BankAccount("NL01BANK0123456789", 1000.00)
#print(account1)
