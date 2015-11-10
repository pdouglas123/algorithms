def insertion_sort(list):
    for i in range(1,len(list)):
        val_current = list[i]
        pos = i 
        while((pos > 0) and (list[pos-1] > val_current)):
            list[pos] = list[pos-1]
            pos = pos-1     
        if pos != i:
            list[pos] = val_current 
    return list 
    
if __name__ == "__main__":  
    list = [54,26,93,17,77,31,44,55,20,23,87,94,88,34,67,32,69]
    print(list)
    print insertion_sort(list)