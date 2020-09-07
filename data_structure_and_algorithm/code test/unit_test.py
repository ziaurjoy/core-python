
def avarage(l):
    if not l:
        return None
    return sum(l)/len(l)

def test_avarage():
    assert 3 == avarage([1,2,3,4,5])


# def avarage(l):
#     if not l:
#         return None
#     return sum(l)/len(l)

# def test_avarage():
#     test_cases = [{
#         'name':'Simple case 1',
#         'input': [1,2,3],
#         'expected': 2.0
#     },
#    {
#         'name':'Simple case 2',
#         'input': [1,2,3,4,5],
#         'expected': 3.0
#     },
#     {
#         'name':'Single List',
#         'input': [100],
#         'expected': 100
#     },
#     {
#         'name':'Emty List',
#         'input': [],
#         'expected': None
#     }]

#     for test_case in test_cases:
#         assert avarage(test_case['input']) == test_case['expected'],test_case['name']

