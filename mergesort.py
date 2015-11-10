from heapq import merge

def merge_sort(m):
    if len(m) <= 1:
        return m
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]
 
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

a = [54,26,93,17,77,31,44,55,20,23,87,94,88,34,67,32,69]
print(a)
a = merge_sort(a)
print(a)