def count_stair_ways(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return count_stair_ways(n-1) + count_stair_ways(n-2)
def count_k(n, k):
    if n == 0:
        return 1
    if n < 0:
        return 0
    total = 0
    for i in range(1,k+1):
        total += count_k(n-i,k)
    return total
def paths(m,n):
    if m == 1 and n == 1:
        return 1
    if m < 1 or n < 1:
        return 0
    return paths(m-1,n) + paths(m, n-1)
def max_product(s):
    if len(s) == 1:
        return s[0]
    return max(s[0]*max_product(s[2:]),max_product(s[1:]))
def flatten(s):
    ans = []
    for item in s:
        if type(item) == list:
            ans += flatten(item)
        else:
            ans += [item]
    return ans