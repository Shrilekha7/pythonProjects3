#TaskManagerWithIteration.py
tasks = []  # List to store all tasks

def add_task():
    """Add a new task by asking for user input"""
    # Get task name and due date from the user
    name = input("Enter task name: ")
    due_date = input("Enter task due date: ")
  
    # Create a task dictionary with name, due date, and completed status
    task = {'name': name, 'due_date': due_date, 'completed': False}
    
    # Add the new task to the tasks list
    tasks.append(task)
    
    # Confirm that the task has been added
    print(f"Task added: {task['name']} (Due: {task['due_date']})")

def complete_task():
    """Mark a task as complete by user input"""
    # Get the task name from the user
    name = input("Enter task name to mark as complete: ")
    
    # Loop through tasks to find the task by name
    for task in tasks:
        if task['name'] == name:
            task['completed'] = True  # Mark task as completed
            print(f"Task completed: {task['name']}")
            return  # Exit the function once the task is found and updated
    
    # If the task is not found, inform the user
    print(f"Task not found: {name}")

def remove_task():
    """Remove a task by user input"""
    # Get the task name from the user
    name = input("Enter task name to remove: ")
    
    # Loop through tasks to find the task by name
    for task in tasks:
        if task['name'] == name:
            tasks.remove(task)  # Remove the task from the list
            print(f"Task removed: {task['name']}")
            return  # Exit the function once the task is found and removed
    
    # If the task is not found, inform the user
    print(f"Task not found: {name}")

def view_tasks():
    """View all tasks with their status"""
    # If there are no tasks, inform the user
    if not tasks:
        print("No tasks available.")
        return  # Exit the function if no tasks exist
    
    # Loop through the tasks and display each one
    for task in tasks:
        # Determine if the task is completed or incomplete
        status = 'Completed' if task['completed'] else 'Incomplete'
        
        # Print task details (name, due date, and status)
        print(f"Task: {task['name']}, Due: {task['due_date']}, Status: {status}")

def mainmethod():
    """Main method to run the task manager"""
    print("***** WELCOME TO TASK MANAGER *****")
    
    # Keep the program running until the user chooses to exit
    while True:
        # Display the menu options
        print("\nMenu:")
        print("Enter 1 to add tasks")
        print("Enter 2 to complete tasks")
        print("Enter 3 to remove tasks")
        print("Enter 4 to view tasks")
        print("Enter 0 to exit the task manager")
        
        # Get the user's choice and ensure it's a valid integer
        try:
            choice = int(input("Please enter your choice: "))
        except ValueError:
            print("Invalid input, please enter a number between 0 and 4.")
            continue  # Restart the loop if input is not valid
        
        # Handle each menu option based on the user's choice
        if choice == 1:
            add_task()  # Add a new task
        elif choice == 2:
            complete_task()  # Mark a task as completed
        elif choice == 3:
            remove_task()  # Remove a task
        elif choice == 4:
            view_tasks()  # View all tasks
        elif choice == 0:
            print("****** Thank you for using Task Manager ******")
            break  # Exit the program
        else:
            print("Invalid choice, please try again.")  # Handle invalid choices

# Run the main method to start the task manager
mainmethod()





