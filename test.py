def is_greater(s,t):
    if s>t:
        print('The number is greater')
    elif s<t:
        print('The number is smaller')
    else:  
        print('Both the numbers are equal')
try:
    s = int(input("Enter your first number: "))
    t = int(input("Enter your first number: "))
    is_greater(s,t)
except:
    print("Number only asso")
