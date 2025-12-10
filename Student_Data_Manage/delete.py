from Student_Data_Manage.input import input_contact_delete
from Student_Data_Manage.read_write_file import write_json

def delete_opration(json_file, students_data):
    while True:
        print(">>>>>>>>>>>>>>Delete Menu<<<<<<<<<<<<<<")
        print("1. Delete By Name.")
        print("2. Delete By Contact.")
        print("3. Back.")

        choice = input("Please Enter Your Choice: ")

        if choice.isdigit(): 
            choice = int(choice)
        else:
            print("Enter Only Number, Not Character.")
            continue

        found = False    

        if choice == 1:
            i=0    
            delete_name = input("Please Enter Name: ")                    
            while i < len(students_data):
                if students_data[i]["name"].lower() == delete_name.lower():
                    students_data.pop(i)
                    found = True
                else:
                    i += 1
            write_json(json_file, students_data) 

                    

        elif choice == 2:
            i=0
            delete_contact = input_contact_delete()
            while i < len(students_data):
                if students_data[i]["contact"] == delete_contact:
                    students_data.pop(i)
                    found = True
                else:
                    i += 1
            write_json(json_file, students_data) 

        elif choice == 3:
            return

        if not found:
           print("User Not Found!.")
        if found:
            print("Deleted Successfully.")   
