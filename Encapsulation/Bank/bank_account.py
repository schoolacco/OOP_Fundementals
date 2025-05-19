class BankAccount:
    def __init__(self, account_number, balance, owner_name):
        self.num = account_number
        self.bal = balance
        self.owner = owner_name
    def getaccount(self):
        print(self.num)
    def getbalance(self):
        print(self.bal)
    def getowner(self):
        print(self.owner)
    def set_number(self, account_number):
     if isinstance(account_number, int) and len(account_number) <= 6:
         self.num = account_number
     else:
         raise ValueError("Account Number must be an integer and at most 6 characters.")
    def set_balance(self, balance):
        if isinstance(balance, int):
            self.bal = balance
        else:
            raise ValueError("Balance must be an integer")
    def set_owner(self, owner):
        if isinstance(owner, str):
            self.owner = owner
        else:
            raise ValueError("Name must be a string.")
def Setup_Account(account_number, balance, owner_name):
    account = BankAccount(account_number,balance, owner_name)
    account.getaccount()
    account.getbalance()
    account.getowner()
