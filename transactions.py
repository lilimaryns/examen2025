from BankAccount import BankAccount



def transfer_funds(source_account:BankAccount, target_account:BankAccount, amount, accounts_list):
    accounts_list_numbers = []
    for i in accounts_list:
        accounts_list_numbers.append(i.getAccountNumber())


    if source_account.getAccountNumber() in accounts_list_numbers and target_account.getAccountNumber() in accounts_list_numbers:
        if amount > 0:
            source_account.withdraw(amount)
            if source_account.withdraw(amount):
                target_account.deposit(amount)
                print("Overboeking geslaagd")
                return accounts_list
            else:

                return "Onvoldoende saldo"

        else:
            assert amount > 0, "Bedrag moet groter zijn dan 0."

    else:
        assert source_account.getAccountNumber() in accounts_list_numbers and target_account.getAccountNumber() in accounts_list_numbers, "Accounts zijn niet in lijst opgeslagen"

def new_day(accounts_list):
    for i in accounts_list:
        i.reset_daily_limit()
    return accounts_list

def main():
    account1 = BankAccount("NL01BANK0123456789", 1000.00)
    account2 = BankAccount("BE68BANK12345678", 500.00)
    account3 = BankAccount("NL03BANK1357924680", 1200.50)
    accounts_list = [account1,account2,account3]
    #accounts_list_str = [account1.__str__(), account2.__str__(), account3.__str__()]
    #TEST1
    source_account1 = BankAccount("NL01BANK0123456789", 1000.00)
    target_account1 = BankAccount("BE68BANK12345678", 500.00)
    trans1 = transfer_funds(source_account1, target_account1, 100, accounts_list)
    print(trans1)
    #TEST2
    source_account2 = BankAccount("BE01BANK0123486789", 1000.00)
    target_account2 = BankAccount("NL01BANK0123456789", 1000.00)
    trans2 = transfer_funds(source_account2, target_account2, 100, accounts_list)
    print(trans2)
    #TEST3 (ik gebruik dezelfde accounts als in test 1)
    amount3 = 1200
    trans3 = transfer_funds(source_account2, target_account2, amount3, accounts_list)
    print(trans3)
    #TEST4
    newday = new_day(accounts_list)
    print(newday)





    #trans = transfer_funds(account1, account2, 200, accounts_list)
    #newday = new_day(accounts_list)

main()
