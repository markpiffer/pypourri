
def countmixix(ixlist,maxix):
    i = len(ixlist)-1
    while (i >= 0) and (ixlist[i] == maxix):
        i -= 1
    if i < 0:
        return False
    ixlist[i] += 1
    r = ixlist[i]
    for i in range(i+1,len(ixlist)):
        ixlist[i] = r
    return True
    
def mixin(alist,blist):
    """iterator which returns all possible mixes of the given lists preserving
    the relative order of the lists"""
    if len(alist) < len(blist):
        shortl,longl = alist,blist
    else:
        shortl,longl = blist,alist
    yield shortl+longl
    r = [None]*(len(alist)+len(blist))
    mixix = [0]*len(shortl)
    while countmixix(mixix,len(longl)):
        rx,lx,sx = 0,0,0
        mx = 0
        while rx < len(r):
            while (sx < len(mixix)) and (mx == mixix[sx]):
                r[rx] = shortl[sx]
                rx,sx = rx+1,sx+1
            if (sx < len(mixix)):
                di = mixix[sx] - mx
                mx = mixix[sx]
            else:
                di = len(r)-rx
            r[rx:rx+di] = longl[lx:lx+di]
            rx,lx = rx+di,lx+di
        yield r


a = [0,0,0]
while countmixix(a,3):
    print(a)
for i in mixin([1,2,3],['a','b']):
    print(i)
    
    
