num=int(input("enter the row"))

i=0

while i<4:
    
    j=num-i-1
    
    while j>0:
        print(end=" ")
        j=j-1
        
        k=i+1
        while k>0:
            print("*",end="")
            k=k-1
            
            print("")
            
            i=i+1
            print("")
                
