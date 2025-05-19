from bank_account import BankAccount, Setup_Account
account = BankAccount(123456, 50, 'ADMIN')
choice = input('''--------------------------
      Welcome admin!
      Would you like to withdraw/deposit money to/from your own account? (1)
      Or set up an account for a customer? (2)
               ''')
if choice == '1':
    Input = input("Withdraw or deposit? ").lower()
    amount = int(input("How much? "))
    if Input == 'withdraw' and amount <= account.bal:
        account.set_balance((account.bal-amount))
    elif Input == 'deposit':
        account.set_balance((account.bal+amount))
    else:
        print("Invalid input, this may be due to attempting to withdraw more than you have.")
elif choice == '2':
    acco_num = int(input("Account Number? "))
    bal = int(input("Initial deposit? "))
    owner = input("Onwer? ")
    Setup_Account(acco_num, bal, owner)
