class Fruits:
   def __init__(self,name,price,color):
       self.name=name
       self.price=price
       self.color=color
   def onyesha(self):
       print(f"my favourite fruits are {self.name}"
             f" and they cost ksh.{self.price}.They are {self.color} in color")

myobj=Fruits("apples",30,"red")
myobj.onyesha()


