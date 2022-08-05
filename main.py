from collections import deque

graph = {}
graph["you"] = ["allice", "bob", "claire", "mm"]


def person_is_seller(name):
    return (name[-1]) == 'm'


def search_name(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller")
                return True
        else:
            search_queue += graph[person]
            searched.append(person)

    return False


search_name("you")
