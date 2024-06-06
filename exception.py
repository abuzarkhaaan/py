x=input("enter 1 ")
y= input("enter 2 ")
try:
    z= int(x) /int(y)
except Exception as e:
    print("exp castched:,",e)
    z= None

print("div",z)