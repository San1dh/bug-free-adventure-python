# basic calculator

def add(a, b):
  print("Sum = ", a+b)

def sub(a, b):
  print("Difference = ", a-b)

def multi(a, b):
  print("Product = ", a*b)

def div(a, b):
  print("Quotient = ", a/b)

rep = 'yes'

while(rep == 'yes'):
 a = int(input("Enter first number: "))
 b = int(input("Enter second number: "))

 print("1) Add \n2) Subtract \n3) Multiply \n4) Divide")
 ch = int(input("Enter your choice: "))
 while(ch!=1 and ch!=2 and ch!=3 and ch!= 4):
  ch = int(input("invalid input, enter again: "))
   
 if(ch == 1):
  add(a, b)
 elif(ch == 2):
  sub(a, b)
 elif(ch == 3):
  multi(a, b)
 if(ch == 4):
  div(a, b)

 rep = input("repeat menu (yes/no): ")
