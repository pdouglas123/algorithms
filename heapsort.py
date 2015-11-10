def heapsort(list):
  for start in range((len(list)-2)/2, -1, -1):
    siftdown(list, start, len(list)-1)
 
  for end in range(len(list)-1, 0, -1):
    list[end], list[0] = list[0], list[end]
    siftdown(list, 0, end - 1)
  return list
 
def siftdown(list, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and list[child] < list[child + 1]:
      child += 1
    if list[root] < list[child]:
      list[root], list[child] = list[child], list[root]
      root = child
    else:
      break
	  
if __name__ == "__main__":
    
    list = [54,26,93,17,77,31,44,55,20,23,87,94,88,34,67,32,69]
    print(list)
    print heapsort(list)