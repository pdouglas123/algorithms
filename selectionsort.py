def selection_sort(list):
    for i, e in enumerate(list):
        mn = min(range(i,len(list)), key=list.__getitem__)
        list[i], list[mn] = list[mn], e
    return list
	
if __name__ == "__main__":
    
    list = [54,26,93,17,77,31,44,55,20,23,87,94,88,34,67,32,69]
    print(list)
    print selection_sort(list)