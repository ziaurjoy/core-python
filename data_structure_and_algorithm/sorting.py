
#   SELECTION SORT

# def selection_sort(l):
#     for i in range(len(l)):
#         index_min = i
#         for j in range(i+1,len(l)):
#             if l[j] < l[index_min]:
#                 index_min = j
#         if index_min != i:
#             l[i], l[index_min] = l[index_min],l[i]

# l = [6,1,4,9,2]            
# selection_sort(l)
# print('After ',l)
# # if __name__ == '__main__':
# #     l = [6,1,4,9,2]
# #     print('Before sort ',l)
# #     selection_sort(l)
# #     print('After ',l)
    


#   BUBBLE SORTING


# def bubble_sort(l):
#     n = len(l)
#     for i in range(0,n):
#         for j in range(0,n-i-1):
#             if l[j] < l[j+1]:
#                 l[j],l[j+1] = l[j+1],l[j]
# n= [6,1,4,9,2]
# print(bubble_sort(n))

def bubble_sort(l):
    n = len(l)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
l = [6,1,4,9,2]
bubble_sort(l)
print('After',l)

# if __name__ == '__main__':
#     l = [6,1,4,9,2]
#     print('Before',l)
#     bubble_sort(l)
#     print('After',l)