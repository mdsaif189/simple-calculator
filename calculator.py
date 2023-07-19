def add(a,b):
  return(a+b)
  
def subtract(a,b):
  return(a-b)

def multiply(a,b):
    return(a*b)

def divide(a,b):
    return (a/b)

print(""" Enter your choice :\n
1.+
2.-
3.*
4./\n""")

select=int(input("Choose  from 1,2,3,4:"))

n1=float(input("\nenter first number:"))
n2=float(input("\nenter second number:"))

if select==1:
  print(n1,"+",n2,"=",add(n1,n2))

if select==2:
  print(n1,"-",n2,'=',subtract(n1,n2))
  
if select==3:
  print(n1,"*",n2,"=",multiply(n1,n2))

if select==4:
  print(n1,"/",n2,"=",divide(n1,n2))


print(" **This is your answer**")
