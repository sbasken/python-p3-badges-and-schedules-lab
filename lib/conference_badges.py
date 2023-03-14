def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    new_list = list()
    for name in names:
        new_list.append(f"Hello, my name is {name}.")
    return new_list

def assign_rooms(names):
    new_list = list()
    room = 0
    for name in names:
        room += 1
        new_list.append(f"Hello, {name}! You'll be assigned to room {room}!")
    return new_list

def printer(names):
    room = 0
    for name in names:
        print(badge_maker(name))
    for name in names:
        room += 1
        print(f"Hello, {name}! You'll be assigned to room {room}!")
