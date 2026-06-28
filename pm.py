def multi(n):
    for i in range(n,3):
        
        for j in range(0,11):
            if j%2==0:
                print("")
            else:
            
                print(f"{i}+{j}={i+j}")

multi(2)
