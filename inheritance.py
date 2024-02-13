class Mpesa
    def __init__(self,account_balance,phone_number):
        self.account_balance =account_balance
        self.phone_number =phone_number
    def send_money(self,amount,receipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f'{amount} KES sent to {receipient}')
        else:
            print("insuficient amount to send money")

class PersonalMpesa(Mpesa):
     def __init__(self,account_balance,phone_number,idno):
         super().__init__(account_balance, phone_number)
         self.idno =idno
     def buyairtime(self,amount):
         self.account_balance-= amount
         print(f"{amount} KSH airtime bought successfully")

class businessMpesa (Mpesa):
    def __init__(self,account_balance,phone_number,business_name):
        super().__init__(account_balance, phone_number)
        self.business_name = business_name
    def receive_payment(self,amount):
        self.account_balance += amount
        print(f"{amount} KES received from customer")
 personal=PersonalMpesa(100,785758576,56746)
personal.send_money(300,948674633)
personal.buyairtime(150)
