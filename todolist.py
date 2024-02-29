tasks = []  # A list to store tasks

def addtask(task):
    tasks.append(task)
    print(f'Task "{task}" added successfully.')

def removetask(task):
    task = task.replace(" ", "")
    if task in tasks:
        tasks.remove(task)
        print(f'Task "{task}" removed successfully.')
    else:
        print(f'Task "{task}" not found.')

while True:
    print("1. Enter your task")
    print("2. Display tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter your task: ")
        addtask(task)
    elif choice == 2:
        print("Tasks:", tasks)
    elif choice == 3:
        task = input("Enter task to remove: ")
        removetask(task)
    elif choice == 4:
        quit()
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
