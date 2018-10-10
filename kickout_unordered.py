def kickout_unordered(a_list,kickout_ix):
    # Remove all items from a_list which are indexed by kickout_ix without moving parts of a_list around.
    # After this call, the last len(kickout_ix) elements of a_list are no longer valid.
    # The order of a_list is lost during this operation (high items are injected at low indexes).
    # This function exists for performance reasons therefore a_list is changed instead of returning a new, shorter list.
    # kickout_ix is invalid after the call.
    # Using this function makes sense only if there are few (~40%, in relation to total) elements to kick out
    n = len(a_list)
    s = n - len(kickout_ix)
    for i in range(len(kickout_ix)-1,-1,-1):
        if kickout_ix[i] < n:
            a_list[kickout_ix[i]] = a_list[n-1]
        else:
            a_list[kickout_ix[kickout_ix[i]-s]] = a_list[n-1]
            kickout_ix[i] = kickout_ix[kickout_ix[i]-s]
        n -= 1

mylist = list(range(0,10))
print("mylist looks like:",mylist)
kicked_outs = [0,3,1,9]
print("These are removed:",list(mylist[i] for i in kicked_outs ))
kickout_unordered(mylist,kicked_outs)
print("mylist looks now like: ",mylist)
print("valid part of mylist:",mylist[:-len(kicked_outs)])
