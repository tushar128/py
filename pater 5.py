num=int(input("enter the number"))
row=0
while row < num:
    print("")
start =row+1

while start>0:
        print("*",end='')
        start=start-1
        row=row+1
        print()
