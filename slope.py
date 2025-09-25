x1=int(input("Enter number :"))
x2=int(input("Enter number :"))
y1=int(input("Enter number :"))
y2=int(input("Enter number :"))
if x1==x2:
    print("vertical Line")
else:
    m = (y2 - y1) / (x2 - x1)
    if m>0:
       print("positive slope")
    elif m<0:
       print("negative slope")
    elif m==0:
       print("horizontal line")
    

