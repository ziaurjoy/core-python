


# linear search

# def linear_search(li,x):
#     for i in range(len(li)): # time complexity = O(n)
#         if li[i] == x:
#             return 'yes this number is ',i # space complexity O(1) Becouse return ekbar e kaj kortese..
#     return 'Dose not match',-1

# print(linear_search([1,2,3,4,5,6,7,8,9,10],5))


# Binary Search

# def binary_search(List,element):
#     left, right = 0,len(List)-1
#     while left <= right:
#         mid = (left+right)//2
#         if List[mid] == element:
#             return mid
#         if List[mid] < element:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# print(binary_search([10,30,40,50],50))

# def binary_search(List,element):
#     left = 0
#     right = len(List)
#     for i in range(left,right):
#         mid = (i+right)//2
#         print(mid)
#         if List[mid] == element:
#             return mid
#         if List[mid] < element:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
# # print(binary_search([10,30,40,50],30))
# print(binary_search([1,2,4,9,11],9))



