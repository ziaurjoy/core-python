

# def avarage(l):
#     if not l:
#         return None
#     return sum(l)/len(l)
# a = [1,2,3,4,5]
# print(avarage(a))


def avarage(l):
    if not l:
        return None
    return sum(l)/len(l)

if __name__ == '__main__':
    l = [1,2,3,4,5]
    except_restult = 3
    restult = avarage(l)
    if except_restult == restult:
        print('Test Passed')
    else:
        print('Test Failed'+' received',restult,'Excepted Result ',except_restult)

