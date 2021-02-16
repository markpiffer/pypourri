def print_leaf2leaf(root, path_down):
"""Emit all paths from one leaf to another in a tree.""" 
    for st in path_down:
        st.append(root)
    if all([x is None for x in root.children]):
        for st in path_down:
            for n in st: print(n.d,end=" ")
            print()
        path_up = [[root]]
    else:
        path_up = []
        for child in root.children:
            path_up += child is not None and [st+[root] for st in print_root2root(child, path_down + path_up)] or []
    for st in path_down:
        st.pop()
    return path_up

class node:
    def __init__(self,d,*children):
        self.d = d
        self.children = children
    
##               1
##            /     \
##          2         6
##        /   \      /
##       3     4     7
##      /          / | \
##     5          8  9  10

five = node(5)
three = node(3,five)
four = node(4)
two = node(2,three,four)
eight = node(8)
nine = node(9)
ten = node(10)
seven = node(7,eight,nine,ten)
six = node(6,None,seven)
one = node(1,two,six)

print_leaf2leaf(one,[])
