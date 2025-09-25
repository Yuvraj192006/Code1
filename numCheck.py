a=int(input("enter a  number"))
if a%2==0:
    if a>0:
        print("This is a positive even number")
    elif a<0:
        print("This is a negative even number")
    else:
        print("This is zero, which is an even number")
else:
    if a>0:
        print("This is a positive odd number")
    elif a<0:
        print("This is a negative odd number")
        
