#check wheather the given number is positive or negative
"""num=int(input())
if num>-1:
    print("positive number")
else:
    print("negative number")"""


#check wheather the person is eligible for vote or not
'''age=int(input())
if age>=18:
    print("eligible")
else:
    print("not eligible")'''

#find wheather the number is even or odd

'''num=int(input())
if num%2==0:
    print("even number")
else:
    print("odd number")'''

#or

'''num=int(input())
if num%2:
    print("odd number")
else:
    print("even number")'''

#find wheather given number is divisible by 3 or not

'''num=int(input())
if  num%3==0:
    print("divisible by 3")
else:
    print("not divisible by 3")'''

#or

'''num=int(input())
if  num%3:
    print("not divisible by 3")
else:
    print("divisible by 3")'''

#check wheather the number is divisible by 3 and 5

'''num=int(input())
if num%3==0 and num%5==0:
    print("fizz buzz")
else:
    print("buzz")'''
#or
'''
num=int(input())
if num%3 and num%5:
    print("buzz")
else:
    print("fizz buzz")'''

#or

'''num=int(input())
if num%3 or num%5:
    print("buzz")
else:
    print("fizz buzz")'''

#check wheather number is zero or +ve or -ve
#using if only
'''num=int(input())
if num==0:
    print("zero")
if num >0:
    print("+ve")
if num<0:
    print("-ve")'''

#using if elif else

'''num=int(input())
if num>0:
    print("+ve")
elif num<0:
    print("-ve")
else:
    print("zero")'''


#if number divisible with 3 - fizz 5- buzz both 3 and 5 fizz buzz other wise invalid

'''n=int(input())
if n%3==0 and n%5==0:
    print("fizz buzz")
elif n%5==0:
    print("buzz")
elif n%3==0:
    print("fizz")b
else:
    print("invalid")'''


#check number is +ve even,+ve odd.-ve even,-odd

'''n=int(input())
if n>0 and n%2==0:
    print("+ve even")
elif n>0 and n%2==1:
    print("+ve odd")
elif n<0 and n%2==0:
    print("-ve even")
else:
    print("-ve odd")'''

#using nested if
n=int(input())
if n>=0:
    if n%2==0:
        print("+ve even")
    else:
        print("+ve odd")
else:
    if n%2==0:
        print("-ve even")
    else:
        print("-ve odd")
