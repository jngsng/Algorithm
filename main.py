# 이진탐색
# 정렬필요

arr = [1,2,3,4,5,6,7,8,9,10,11,12]

def binarySearch(arr,targetNum):
  start = 0
  end = len(arr) - 1
  midIndex = len(arr)//2
  indexValue = arr[midIndex]
  if indexValue == targetNum:
    return midIndex
  elif indexValue < targetNum:
    start = midIndex + 1
  elif indexValue > targetNum:
    end = midIndex -1
  return -1

print(binarySearch(arr,2))