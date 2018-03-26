def important_tasks(dict_tasks):
    dict = {}
    for (i, item) in dict_tasks.items():
        for (j, item2) in item.items():
            if j == 'urgent' and item2 == True:
                dict[i] = {'todo': item['todo']}

    return dict


def print_options(dict_task):
    for (i, item) in dict_task.items():
        print(i, '')
        for (j, item2) in item.items():
            print(j + ': ' + item2)


tasks = {
    "task1" : {'todo': 'call John for AmI progect organization', 'urgent': True},
    "task2" : {'todo': 'buy a new mouse', 'urgent': True},
    "task3" : {'todo': 'find a present for Angelina\'s birthday', 'urgent': False},
    "task4" : {'todo': 'organize mega pary (last week of April)', 'urgent': False},
    "task5" : {'todo': 'book summer holidays', 'urgent': False},
    "task6" : {'todo': 'whatsapp Mary for a coffee', 'urgent': False},
}


urgent_tasks = important_tasks(tasks)
print_options(urgent_tasks)