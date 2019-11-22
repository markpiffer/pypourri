def noverk(k,n):
    perm = list(range(-1,k+1))
    perm[0] = 0
    perm[k+1] = n+1
    direc = [1] * (k+2)
    cnt = 9
    try:
        while cnt > 0:
            cnt -= 1
            i = k
            while perm[i] + direc[i] != perm[i+direc[i]]:
                perm[i] += direc[i]
                print(perm)
                print(direc,"\n")
            direc[i] = -direc[i]
            if direc[i] == 1 and perm[i] + 1 != perm[i+1]:
                perm[i] += direc[i]
            i -= 1
            while perm[i] + direc[i] == perm[i+direc[i]]:
                direc[i] = -direc[i]
                i -= 1
            perm[i] += direc[i]
            print(perm)
            print(direc,"\n")
    except:
        print("Bumm")

def noverk_(k,n):
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
