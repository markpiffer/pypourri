

def hop(alist,i):
    alist[i],alist[i+1] = alist[i+1],alist[i]

def hoptoend(alist,i):
    for j in range(i,len(alist)-1):
        hop(alist,j)
        yield True

def permutordered(alist,n=1):
    """iterator to create all permutations of alist (with partial ordering if n > 1). 
    The last n elements don't change their partial order within each returned permutation"""
    
    yield alist # return the trivial permutation
    
    # To generate all permutations we start with the 2nd-last element in the
    # sequence and add it to the previous permutation in all possible places:
    # this is behind the last element for the first step ("before the last element"
    # is a combination that was already satisfied with the trivial permutation).
    # We continue the same way with the 3rd last element, inserting it in all possible
    # places of all permutations of the elements right to it.
    # Formally: step from back to front through the list.
    # In each iteration [i], generate the complete set of permutations from step [i-1]
    # and insert element [i] in all possible places of these permutations.
    # If n is > 1, then start left from the n-th last element and don't create 
    # permutations for the elements from the nth to the end. This conserves the partial
    # ordering which these elements have - the elements to the left are mixed into
    # them in all possible permutations.
    for i in range(len(alist)-n-1,-1,-1):
        j = len(alist)-n
        stack = [alist]
        hopper = [iter([None])] # we need one initial iteration to start 
        while True:
            try:
                next(hopper[-1]) # move one element in the list on TOS
                if i == j:
                    yield stack[-1] # output only if we are at the level
                    # where we move the element from the outer iteration
                else:
                    # construct fresh permutation arrays on every level
                    # up from the one which is still running
                    for j in range(j-1,i-1,-1):
                        stack.append(stack[-1][:])
                        hopper.append(hoptoend(stack[-1],j))
            except StopIteration:
                stack.pop()
                hopper.pop()
                if len(hopper) == 1:
                    break
                else:
                    j += 1


a = [1,2,3,4]
for i,x in enumerate(permutordered(a,2)): print(i,x)
# Output: [1,2,3,4]  [1,3,2,4]  [1,3,4,2]  [2,1,3,4]
#         [2,3,1,4]  [2,3,4,1]  [3,1,2,4]  [3,2,1,4]
#         [3,2,4,1]  [3,1,4,2]  [3,4,1,2]  [3,4,2,1]
# Notice that the last two elements didn't change their relative positions

 
