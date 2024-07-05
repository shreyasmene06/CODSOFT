'''A To-Do List application is a useful project that helps users manage
and organize their tasks efficiently. This project aims to create a
command-line or GUI-based application using Python, allowing

users to create, update, and track their to-do lists'''

tasks=[]
def Add_task():                                     #adds a task in the to-do list
    Input=input("Enter a Task : ")
    tasks.append(Input)
    print("Task Added Successfully !")

def Del_task():
    rem=int(input("Enter Task no. To Be Deleted : "))
    if rem>len(tasks):                              #checks if the entered value to be deleted is within the to do list or not
        print("Invalid Task no.")
    elif len(tasks)==0:
        print("No Tasks To Delete")
    else:
        tasks.pop(rem-1)
        print("Task Removed Succesfully !")         #deletes the selected task in the to do list

def Edit_task():
    x=int(input("Enter Task no. To Be Editted : "))
    if x>len(tasks):                                 #checks if the entered value to be deleted is within the to do list or not
        print("Invalid Task No.")
    elif len(tasks)==0:
        print("No Tasks To Edit")
    else:
        edit=input("Enter Editted Task")
        tasks[x]=edit
        print("Task Editted Successfully !")        #edits the selected task in the to do list

def View_task():
  print("\n=====TASKS=====")
  if len(tasks)==0:
    print("No Tasks Found")
  else:
    for i in range(len(tasks)):
      print(f'{i+1}. {tasks[i]}')                   #lists all the tasks in the list


def main():
  """Main loop for the to-do list application."""
  while True:
    print("\n====== TO DO LIST APPLICATION =====")
    print("1. Add Task")
    print("2. Remove Task")                         #main body which joins all different functions and make a interaction with user
    print("3. Edit Task")
    print("4. View Tasks")
    print("5. Exit")

    try:
      choice = int(input("Enter your choice: "))

      if choice == 1:
        Add_task()
      elif choice == 2:
        Del_task()
      elif choice == 3:
        Edit_task()
      elif choice == 4:
        View_task()
      elif choice == 5:
        print("Exiting...")
        break
      else:
        print("Invalid choice.")
    except ValueError:
      print("Invalid input. Please enter a number.")

if __name__ == "__main__":
  tasks = []
  main()
