contact = []

def add():
    name = input("Enter Name: ")
    number = int(input("Enter Number: "))
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contact.append([name, number, email, address])
    print("Contact Added Successfully...")

def view():
    if contact:
        for i in contact:
            print(f"Name: {i[0]}, Number: {i[1]}, Email: {i[2]}, Address: {i[3]}")
    else:
        print("No Contacts to Display.")

def search():
    name = input("Enter Name To Search Details: ").lower()
    found = False
    for i in contact:
        if i[0].lower() == name:
            print(f"Name: {i[0]}, Number: {i[1]}, Email: {i[2]}, Address: {i[3]}")
            found = True
    if not found:
        print("No Records Found")

def update():
    name_to_update = input("Enter Name To Edit Details: ").lower()
    found = False
    for i in contact:
        if i[0].lower() == name_to_update:
            name = input("Enter Name: ")
            number = int(input("Enter Number: "))
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            i[0] = name
            i[1] = number
            i[2] = email
            i[3] = address
            print("Updated Successfully...")
            found = True
    if not found:
        print("Record Not Found")

def delete():
    name_to_delete = input("Enter Name To Delete Details: ").lower()
    found = False
    for i in contact:
        if i[0].lower() == name_to_delete:
            contact.remove(i)
            print("Contact Deleted Successfully...")
            found = True
            break  # Exit loop after deletion
    if not found:
        print("Record Not Found")

def main():
    while True:
        ans = int(input('''Enter 1 To Continue and 2 To Exit: '''))
        if ans == 1:
            print("Enter 1 To Add Contact Info")
            print("Enter 2 To View Contact Details")
            print("Enter 3 To Search Contact Info")
            print("Enter 4 To Update Contact Info")
            print("Enter 5 To Delete Contact")
            choice = int(input("Choice: "))
            if choice == 1:
                add()
            elif choice == 2:
                view()
            elif choice == 3:
                search()
            elif choice == 4:
                update()
            elif choice == 5:
                delete()
            else:
                print("Invalid Choice")
        elif ans == 2:
            print("Exitting...")
            break
        else:
            print("Invalid Entry")

if __name__ == "__main__":
    main()
