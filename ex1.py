def print_options(tasks):
    for (i, item) in tasks.items():
        print(str(i) + item)


def print_list(items):
    for item in items:
        print(item)


todo_manager = {
    1: " Insert a new task",
    2: " Remove a task", # by typing its exact content
    3: " Show all existing tasks",
    4: " Close the program"
}

tasks = []
print_options(todo_manager)
choice = int(input("Select an option: "))
finish = False

while not finish:
    if choice == 1:
        task = input(str("Insert the new task: "))
        tasks.append(task)
        choice = int(input("Select an option: "))
    elif choice == 2:
        task = input(str("Which task you want to remove: "))
        tasks.remove(tasks)
        choice = int(input("Select an option: "))
    elif choice == 3:
        tasks.sort()
        print_list(tasks)
        choice = int(input("Select an option: "))
    elif choice == 4:
        finish = True
    else:
        print("Wrong input")
        choice = int(input("Select an option: "))