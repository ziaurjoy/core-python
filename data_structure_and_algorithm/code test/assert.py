
def avarage(l):
    if not l:
        return None
    return sum(l)/len(l)

if __name__ == '__main__':
    l = [1,2,3,4,5]
    excepted_restult = 3
    assert excepted_restult == avarage(l),'Sorry Excepted Result is not True'