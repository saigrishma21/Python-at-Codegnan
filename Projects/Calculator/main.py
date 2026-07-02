#import functions
from addition import add
import subtraction
import multiplication as MUL
from division import div as Division
from power import power_number
from square import sqrt_num
from compound import compound_interest
from simple import simple_interest

if __name__ == "__main__":
    print("welcome to the small calculator")
    while True:
        print("1.Addition \n 2.Subtraction \n 3.Multiplication \n 4. Division \n 5.power of a number \n 6.square root \n 7.compound interest \n 8.simple interest \n 9.Exit")
        choice=int(input("enter your choice:"))
        if choice==1:
            #call add function
            a,b,*c= map(int,input("enter numbers:").split())
            res =add(a,b,*c)
            print(res)
        elif choice==2:
            x,y=map(int,input("enter 2 numbers:").split())
            res=subtraction.sub(x,y)
            print(res)
        
        elif choice==3:
            #call mul func
            a,b=map(int,input("enter 2 numbers:").split())
            res=MUL.mul(a,b)
            print(res)
        
        elif choice==4:
            #call div fun
            x,y=map(int,input("enter 2 numbers:").split())
            res=Division(x,y)
            print(res)
        elif choice==5:
            #call power
            x,y = map(int, input("Enter base and exponent: ").split())
            res=power_number(x,y)
            print("Result:",res)

        elif choice==6:
            #call square
            num = int(input("Enter a number: "))
            print("Result:", sqrt_num(num))
        elif choice==7:
            #call compund
            p = float(input("Enter Principal Amount: "))
            r = float(input("Enter Rate of Interest (%): "))
            t = float(input("Enter Time (years): "))
            ci = compound_interest(p, r, t)
            print("Compound Interest =", round(ci, 2))
        elif choice==8:
            #call simple
            p = float(input("Enter Principal Amount: "))
            r = float(input("Enter Rate of Interest (%): "))
            t = float(input("Enter Time (years): "))
            si = simple_interest(p, r, t)
            print("Simple Interest =", si)
        elif choice==9:
            print("thanks for using small calculator")
            exit()
        else:
            print("Invalid choice,Select in between 1 to 5")