import operator

def binom_combi(n, k, delta=False, init_combi=None, init_dirs=None):
       """'n choose k': Generate binomial combinations like itertools.combinations, but in a order where
    two consecutive combinations will differ for each place in at most one position.
    I.e. for a 3-combination out of string "abcdef" you get "abc", "abd", "abe" etc. and no position
    in the 3-character string will jump more than +/-1 in the source set - you will get "abf", "acf"
    instead of the lexical sort order "abf", "acd" of itertools.combinations. n can be an integer, then
    all numeric combinations are generated, or an arbitrary list of elements, then the itertools.combinations
    interface is mimicked. init_combi if given is a list of integers of length exactly k and denotes a
    starting combination of indices, where all prior combinations will be skipped then.
    init_dirs (also length k) is the "direction" in which elements will count up (+1) or down (-1) in the
    next combination step - only such directions where "the way isn't blocked" by another adjacent element
    make sense. Elements at highest indices are moved first"""
    try:
        r = [None] + list(n) # try access as iterable
        n = len(r)-1
    except TypeError:        # oh, n must be an integer then
        r = [None] + list(range(n))
    if n >= k:
        if init_combi is None:
            perm = list(range(0,k+2))
            perm[0] = n+1
            perm[k+1] = n+1
        else:
            # convert 0-based user indices to 1-based algorithm indices
            perm = [n+1] + [x+1 for x in init_combi] + [n+1]
        if init_dirs is None:
            direc = [1] * (k+2)
        else:
            direc = [1] + init_dirs + [1]
        if not delta:
            yield operator.itemgetter(*perm[1:k+1])(r)
        while perm[1] != n+1-k:
            while perm[k] + direc[k] != perm[k+direc[k]]:
                perm[k] += direc[k]
                if delta:
                    yield ((k-1, direc[k]),)
                else:
                    yield operator.itemgetter(*perm[1:k+1])(r)
            i = k
            while (perm[i] + direc[i] == perm[i+direc[i]]) and (perm[i] == n-k+i or direc[i] == -1):
                direc[i] = -direc[i]
                i -= 1
            if direc[i] == 1:
                r_tmp = []
                while True:
                    perm[i] += 1
                    if delta:
                        r_tmp.append((i-1,1))
                    i += 1
                    if not ((perm[i] != n-k+i) and (perm[i-1] == perm[i])): break
            else:
                perm[i] -= 1
                if delta:
                    r_tmp = [(i-1,-1)]
                i += 1
                while (i <= k) and (perm[i-1] == perm[i] - 2):
                    perm[i] -= 1
                    if delta:
                        r_tmp.append((i-1,-1))
                    direc[i] = 1
                    i += 1
            if delta:
                yield tuple(r_tmp)
            else:
                yield operator.itemgetter(*perm[1:k+1])(r)
    return

print(list(binom_combi(4,2)))
print(list(binom_combi("abcd",2)))
print(list(binom_combi(4,2,delta=True)))
print(list(binom_combi("abcd",2,delta=True)))
print(list(binom_combi(4,2,init_combi=[2,3])))
print(list(binom_combi("abcd",2,init_combi=[1,2])))

n = 18
k = 9
r = binom_combi(n,k)
pold = list(range(k))
for p in r:
    for i in range(k):
        if (pold[i] - p[i] > 1) or (pold[i] - p[i] < -1):
            print("Error, consecutive coefficient sets differing more than +-1:", p, pold)
            break
    pold = p

n = "abcdefghijklmnop"
k = 8
r = binom_combi(n,k)
test_dict = {}
cnt = 0
for p in r:
    cnt += 1
    test_dict[p] = True
print(cnt)
cnt = 0
import itertools
for p in itertools.combinations(n,k):
    test_dict.pop(p)
    cnt += 1
print(cnt)
if len(test_dict) != 0:
    print("Error: elements remaining: ",test_dict)

