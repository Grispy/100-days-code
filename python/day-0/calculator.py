n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
def add(x, y):
   return x + y
def sub(x, y):
   return x - y
def mul(x, y):
   return x * y
def div(x, y):
   return x / y
choice=1
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter choice: "))
    if choice==1:
        print(n1, "+", n2, "=", add(n1, n2))

    elif choice==2:
        print(n1, "-", n2, "=", sub(n1, n2))

    elif choice==3:
        print(n1, "*", n2, "=", mul(n1, n2))

    elif choice==4:
        print(n1, "/", n2, "=", div(n1, n2))
    elif choice==0:
        print("Exit")
    else:
        print("Enter valid choice")
