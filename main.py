# 버블 정렬

numbers = [7,3,2,9]

for front_index in range(0,len(numbers)-1):
  for index in range(front_index+1,len(numbers)):
    if numbers[front_index]>numbers[index]:

      temp = numbers[front_index]
      numbers[front_index] = numbers[index]
      numbers[index] = temp
    print(numbers)