


# def avarage(l):
#     if not l:
#         return None
#     return sum(l)/len(l)
# if __name__ == '__main__':
#     print(avarage([1,2,3,4,5]))

# n = input('Enter your number : ')
# a = n.split()
# li = []
# for i in a:
#     li.append(int(i))
# def avarage(l):
#     if not l:
#         return None
#     return sum(l)/len(l)
# # print(avarage(li))
# if __name__ == '__main__':
#     l = li
#     print(avarage(l))

# def avarage(l):
#     if not l:
#         return None
#     return sum(l)/len(l)
# if __name__ == '__main__':
#     li = [1,2,3,4,5]
#     accept_result = 3.0
#     result = avarage(li)
#     if accept_result == result:
#         print('Test passed')
#     else:
#         print('Test failed','receved : ',result,'accepted : ',accept_result)




# def avarage(l):
#     if not l:
#         return None
#     return sum(l)/len(l)
# if __name__ == '__main__':
#     li = [1,2,3,4,5]
#     accept_result = 3
#     assert avarage(li) == accept_result,'Your Idea is rong'


#  pytest
# def avarage(l):
#     if not l:
#         return None
#     return sum(l)/len(l)

# def test_average():
#     assert 3 == avarage([1,2,3,4,5])

# def test_average():
#     test_cases = [
#         {
#             'name': 'Simple case 1',
#             'input': [1,2,3],
#             'expected': 2.0
#         },
#         {
#             'name': 'Simple case 2',
#             'input': [1,2,3,4],
#             'expected': 2.0
#         },
#         {
#             'name': 'List with one time',
#             'input': [100],
#             'expected': 100.0
#         },
#         {
#             'name': 'Emty list',
#             'input': [],
#             'expected': None
#         },
#     ]
#     for test_case in test_cases:
#         assert test_case['expected'] == test_average(test_case['input']),test_case['name']
        # print(test_case)


# unit test

# def avarage(l):
#     if not l:
#         return None
#     return sum(l)/len(l)
# if __name__ == '__main__':
#     print(avarage([1,2,3,4,5]))


