a=int(input("Enter first numbr :"))
b=int(input("Enter second numbr :"))
c=int(input("Enter third numbr :"))
if a>b:
    if a>c:
      print("Number 1 is the greatest")
    else:
      print("Number 3 is the greatest")
elif b>a:
    if b>c:
        print("Number 2 is the greatest")
    else:
        print("Number 3 is the greatest")
elif a==b==c:
    print("All three numbers are equal")

