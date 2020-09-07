

def binary_search(l,x):
    left = 0
    right = len(l) - 1
    while left <= right: # [1,2,3,4,5,6,7,8,9,10]
        medile = (left + right)//2
        if l[medile] == x:
            return medile
        elif medile < x:
            left = medile + 1
        else:
            right = medile - 1
    return -1

# def test_binary():
#     assert 3 == binary_search([1,2,3,4,5,6,7,8],4),'Sorry Accepeted Ressult and Binary search result is not match'

if __name__ == '__main__':
    l = [1,2,3,4,5,6,7,8,9]
    for x in range(1,11):
        position = binary_search(l,x)
        if position == -1:
            if x in l:
                print(x,'is in l,but function returned')
            else:
                print(x,'not in list')
        else:
            if l[position] == x:
                print(x,'found in correct possition')
            else:
                print('Binary search retured',position,'for',x,'which in incurrect')
    print('program terminated')