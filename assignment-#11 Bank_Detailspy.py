class BankAccount:
    def __init__(self, account_number, date_of_opening, customer_name, balance):
        self.account_number = account_number
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
        self.balance = balance




    def deposit(self):
        DEPOSIT = int(input("How much do you want to deposit: "))
        print("This amount has been deposited: ",DEPOSIT)
       

    def withdraw(self):
        WITHDRAW = int(input("How much do you want to withdaw: "))
        if WITHDRAW > self.balance:
                print("Balance is not enough. Try again ")   
                WITHDRAW = int(input("How much do you want to withdaw: "))
        else:
                balance_left_withdrawn = self.balance - WITHDRAW
                print("This amount has been withdrawn: ",WITHDRAW)

    def customer_details(self):
        print("Account number: ",self.account_number)
        print("Date of opening : ",self.date_of_opening)
        print("Customer name: ",self.customer_name)
        print("Account balance ",self.balance)
        
                
    def check_balance(self,withdrawn_money,money_deposited):
        balance_left = self.balance - withdrawn_money + money_deposited
        print("This is the current balance: ", balance_left)

details = BankAccount(231, "26 Feb 2023","Carol", 400000)
details.deposit(DEPOSIT)
details.withdraw()
details.customer_details()
details.check_balance(20000,5000)


