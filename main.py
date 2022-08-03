voted = {}

def check_voter(name):
  if voted.get(name):
    print("X")

  else:
    voted[name] = True
    print("Vote")


check_voter("tom")
check_voter("mike")
check_voter("tom")