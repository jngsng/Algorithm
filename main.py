# 퀵 정렬 / 재귀

numbers = [40,35,27,50,75, 123, 1245, 214, 35, 436, 35]

def quickSort(array):
  if len(array) < 2:
    return array
  else:
    pibot = array[0]
    less = [number for number in array[1:] if number <= pibot]
    greater = [number for number in array[1:] if number >= pibot]
    return quickSort(less) + [pibot] + quickSort(greater)

print(quickSort(numbers))