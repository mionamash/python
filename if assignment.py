weight=input("Enter weight")
height=input("Enter your height")


ans=weight/height**2
if ans <=18.5:
    print("underweight")
elif ans >=18.5 and ans<25:
    print("normal weight")
elif ans >=25 and ans<30:
    print("overweight")
else:
    print("obese")