# 단순탐색

arr = [1,2,3,4,5,6,7,8,9,10]

def SimpleSearch(arr, targetNum):
  for index in range(0, len(arr)):
    if arr[index] == targetNum:
      return index
  return -1

print(SimpleSearch(arr,8))