word = "qweklbrwklbfklsdanflnasdfklasdfnklasdnflk"


def letter_count(word):
  map = {}
  most = {}
  for alphabet in word:
    if map.get(alphabet) == None:
      map[alphabet] = 1
    else:
      map[alphabet] += 1

  max = -1
  for key in map:
    if map[key] > max:
      max = map[key]
      
  return max


print(letter_count(word))
