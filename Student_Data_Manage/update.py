import json
from Student_Data_Manage.input import input_contact_update
from Student_Data_Manage.read_write_file import write_json

def update_opration(json_file, data):
    if len(data)>0:    
        while True:
            print(">>>>>>>>>Update Menu<<<<<<<<<")
            name = input("Please Enter Name: ")
            found = False

            for user in data:
                if user["name"].lower() == name.lower(): 
                    print(json.dumps(user, indent=4))
                    found = True
                    
                    print("1. Update Name")
                    print("2. Update Address")
                    print("3. Update Contact")
                    print("4. Back")

                    choice = input("Enter Your Choice: ")

                    if not choice.isdigit():
                        print("Enter Only Number, Not Character.")
                        return

                    choice = int(choice)

                    if choice == 1:
                        user["name"] = input("Please Enter New Name: ") 
                        write_json(json_file, data)
                        print("Name Updated Successfully.")

                    elif choice == 2:
                        user["address"] = input("Please Enter New Address: ") 
                        write_json(json_file, data)
                        print("Address Updated Successfully.")

                    elif choice == 3:
                        user["contact"] = input_contact_update()
                        write_json(json_file, data)
                        print("Contact Updated Successfully.")

                    elif choice == 4:
                        return

                    return 

            if not found:
                print("Name Not Found.")
    else: 
        print("\nSorry! No Data Avliable For Update") 