

def selection_sort(l):
    n = len(l)
    for i in range(0,n-1):
        index_min = i
        for j in range(i+1,n):
            if l[j] < l[index_min]:
                index_min = j
        if index_min != i:
            l[i],l[index_min] = l[index_min],l[i]

if __name__ == "__main__":
    l = [4,6,2,1,4,8,4]
    print('Before sort : ',l)
    selection_sort(l)
    print('After sort : ',l)