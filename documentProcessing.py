def do_list(menu, list_of_dishes):
    dish = ''
    cycle = 0

    for letter in menu.read():
        if letter == ' ':
            list_of_dishes[cycle].append(dish)
            dish = ''
        elif letter == "\n":
            list_of_dishes[cycle].append(dish)
            dish = ''
            cycle += 1
        else:
            dish += letter
        list_of_dishes = list(list_of_dishes)

    for i in list_of_dishes:
        if i == ['']:
            list_of_dishes.remove(i)
    return list_of_dishes


def remove_store(count_of_store, list_of_dishes):
    for i in range(count_of_store):
        del (list_of_dishes[i][0])
    return list_of_dishes
