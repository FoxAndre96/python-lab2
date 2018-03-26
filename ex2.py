from sys import argv


def print_options(list_task):
    for (i, item) in list_task.items():
        print(str(i) + item)


def print_list(items):
    for item in items:
        print(item)


def print_file(elem, file_txt):
    for t in elem:
        file_txt.write(t + '\n')


# create a file
filename = argv[1]
txt = open(filename) # open the file

file_tasks = txt.read() # reading the file

todo_manager = {
    1: " Insert a new task",
    2: " Remove a task", # by typing its exact content
    3: " Show all existing tasks",
    4: " Close the program"
}

tasks = file_tasks.split('\n')
txt.close()
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
        tasks.remove(task)
        choice = int(input("Select an option: "))
    elif choice == 3:
        tasks.sort()
        print_list(tasks)
        choice = int(input("Select an option: "))
    elif choice == 4:
        finish = True
        txt = open(filename, 'w')
        print_file(tasks, txt)
        txt.close()
    else:
        print("Wrong input")
        choice = int(input("Select an option: "))