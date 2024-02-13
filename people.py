class People:
    def __init__(self,name,age,country):
        self.name =name
        self.age =age
        self.country =country

    def show(self):
     print(f" {self.name} who lives in {self.country} has proposed to me and he is {self.age} years old...This is so crazy!!")
myobj=People("Colon Brian",23,"France")
myobj.show()
myobj=People(" Brian",73,"Kenya")
myobj.show()
myobj=People("john",31,"Spain")
myobj.show()
myobj=People("Christian",20,"Uganda")
myobj.show()