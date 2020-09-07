def linear_search(l,x):
    n = len(l)
    i = 0
    while i < n:
        if l[i] == x:
            return i
        i += 1
    i = -1
    return i

def test():
    assert 2 == linear_search([1,2,3,4,5],3),'Not Accepted'