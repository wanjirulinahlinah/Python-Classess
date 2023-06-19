# # Add these attributes and behaviours to the class Account

# # Add attributes deposits and withdrawals in the init method 
# # which are empty lists by default and another attribute loan_balance which is zero by default.
# class Account:
#     def __init__(self):
#         self.deposit=[]
#         self.withdrawal=[]
#         self.loan_balance=0


# # Add a method check_balance which returns the account’s balance
# def check_balance(self):
#     total_deposits=sum(transaction['amount']for transaction in self.deposits)
#     total_withdrawals=sum(transaction['amount']for transaction in self.withdrawals)
#     return total_deposits-total_withdrawals

# # Update the deposit method to append each withdrawal transaction to the deposits list. Each transaction should be in form of a dictionary like this  
# # {
# #    "amount": amount,
# #    "narration": “deposit”
# # }

# def deposit(self,amount):
#     transaction={
#     'amount':amount,
#     'narration':'deposit'
#   }
#     self.deposits.append(transaction)
    
    
# # Update the withdrawal method to append each withdrawal transaction to the 
# # withdrawals list. Each transaction should be in form of a dictionary like like this 
# # {
# #    "amount": amount,
# #    "narration": “withdrawal”
# # }
# def withdrawal(self,amount):
#     if self.check_balance()>=amount:
#         transaction={
#             'amount':amount,
#             'narration':'withdrawal'
#         }

#     self.withdrawals.append(transaction)
    
# #     Add a new method  print_statement which combines both deposits and
# # withdrawals into one list and, using a for loop, prints each transaction in a new line like this
# # deposit - 1000
# # withdrawal - 500

# def print_statement(self):
#     transaction=self.deposits+self.withdrawals
#     for transaction in transaction:
#         print(f"{transaction['narration']}-{transaction['amount']}")
        
        
# #         Add a borrow_loan method which allows a customer to borrow if they meet these conditions:
# # Account has no outstanding loan
# # Loan amount requested is more than 100
# # Customer has made at least 10 deposits.
# # Amount requested is less than or equal to 1/3 of their total sum of all deposits.
# # A successful loan increases the loan_balance by requested amount

# def borrow_loan(self,amount):
#     if self.loan_balance == 0 and amount> 100 and len(self.deposits)>= 10:
#         self.loan_balance += amount


# #     Add a repay_loan method with this functionality
# # A customer can repay a loan to reduce the current loan_balance
# # Overpayment of a loan increases the accounts current balance

# def  repay_loan(self,amount):
#      if amount>self.loan_balance:
#          extra_amount = amount-self.loan-check_balance
#          self.loan_balance=0
#          self.deposit(extra_amount)
#      else:
#          self.loan_balance-=amount  
         
#         #  Add a transfer method which accepts two attributes 
#         #  (amount and instance of another account). If the amount is less 
#         #  than the current instances balance, the method transfers the 
#         #      requested amount from the current account to the passed account. 
#         #      The transfer is accomplished by reducing the current account balance 
#         #      and depositing
#         #  the requested amount to the passed account.  
# def transfer(self,amount,destination_account):
#         if amount <= self.check_balance():
#             self.withdrawal(amount)
#             destination_account.deposit(amount)





class BankAccount:
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        transaction = {
            "amount": amount,
            "narration": "deposit"
        }
        self.deposits.append(transaction)

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            transaction = {
                "amount": amount,
                "narration": "withdrawal"
            }
            self.withdrawals.append(transaction)
        else:
            print("Insufficient balance!")

    def print_statement(self):
        transactions = self.deposits + self.withdrawals
        for transaction in transactions:
            print(transaction["narration"], "-", transaction["amount"])

    def borrow_loan(self, amount):
        if self.loan_balance == 0 and amount > 100 and len(self.deposits) >= 10:
            total_deposits = sum(transaction["amount"] for transaction in self.deposits)
            if amount <= total_deposits / 3:
                self.loan_balance += amount
                print("Loan approved!")
            else:
                print("Loan amount exceeds 1/3 of total deposits!")
        else:
            print("Loan not approved!")

    def repay_loan(self, amount):
        if amount <= self.loan_balance:
            self.loan_balance -= amount
            self.balance += amount
            print("Loan repayment successful!")
        else:
            print("Invalid loan repayment amount!")

    def transfer(self, amount, target_account):
        if amount <= self.balance:
            self.balance -= amount
            target_account.deposit(amount)
            print("Transfer successful!")
        else:
            print("Insufficient balance for transfer!")