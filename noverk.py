
def noverk(k,n):
    perm = list(range(-1,k+1))
    perm[0] = 0
    perm[k+1] = n+1
   
    print(perm[1:k+1])
    
    for i in range(k,0,-1):
        while perm[i+1] > perm[i] + 1:
            perm[i] += 1
            print(perm[1:k+1])
    perm[k+1] -= 1    
        
    perm[2] -= 1
    for i in range(1,k+1):
        while perm[i-1] < perm[i] - 1:
            perm[i] -= 1
            print(perm[1:k+1])
    perm[0] += 1
    
    perm[k-1] += 1
    for i in range(k,0,-1):
        while perm[i+1] > perm[i] + 1:
            perm[i] += 1
            print(perm[1:k+1])
    perm[k+1] -= 1    
    
noverk(3,6)
