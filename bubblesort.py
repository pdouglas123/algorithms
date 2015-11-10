def bubbleSort(list):
    for passes in range(len(list)-1,0,-1):
        for i in range(passes):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20,23,87,94,88,34,67,32,69]
print(alist)
bubbleSort(alist)
print(alist)
print range(10,-4, -1)