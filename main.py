word = "test"


def letter_count(word):
  map = {}
  for alphabet in word:
    if map.get(alphabet) == None:
      map[alphabet] = 1
    else:
      map[alphabet] += 1

      print("map => ", map)
  return -1


print(letter_count(word))
