# MAX없이 최대값 구하기

list = [9,22,3,7,4,5]

def solution(list):
  
  result = list[0];
  
  for num in list:
    if result < num:
      result = num
  
  return result

# max
print("=>",solution(list))