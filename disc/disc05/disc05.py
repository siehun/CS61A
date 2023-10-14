from math import gcd
def make_rat(num, den):
    gcd_fraction = gcd(num,den)
    return [num//gcd_fraction,den//gcd_fraction]

def numer(rat):
    return rat[0]

def denom(rat):
    return rat[1]


def lt_rat(x, y):
    return numer(x)*denom(y) < numer(y) < denom(x)



def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_leaf(tree):
    """Returns True if the tree's list of branches is empty, and False otherwise."""
    return not branches(tree)

def height(t):
    if is_leaf(t):
        return 0
    return max([height(b) for b in branches(t)])+1
        
def find_path(t, x):
    if label(t) == x:
        return [label(t)]
    for branch in branches(t):
        path = find_path(branch,x)
        if path:
            return [label(t)] + path
        
# leaves is a list
def sprout_leaves(t, leaves):
    if is_leaf(t):
        return tree(label(t,[tree(leaf) for leaf in leaves]))
    return tree(label(t),[sprout_leaves(s, leaves) for s in branches(t)])

def sum_tree(t):
    total = 0
    for b in branches(t):
        total += sum_tree(b)
    return label(t) + total

def balanced(t):
    for b in branches(t):
        if sum_tree(branches(t)[0]) != sum_tree(b) or not balanced(b):
            return False
        return True