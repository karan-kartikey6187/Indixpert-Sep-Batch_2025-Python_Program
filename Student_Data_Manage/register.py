
import uuid
def register_opration(student_data):
    print("\n>>>>>>>>>> Registration Details <<<<<<<<<<")

    student = {}
    student["id"] = uuid.uuid4().hex[:6]
    student["name"] = input("Please Enter Your Name: ")
    student["address"] = input("Please Enter Your Address: ")

    while True:
        try: 
            contact =int(input("Please Enter Your Contact: "))
            if len(str(contact)) == 10:
                student["contact"] = contact
                break
            else:
                print("Invalid contact! Enter 10 digit number.")
        except:
            print("Enter Only Number Not Character.")        

    student_data.append(student) 

    print("Registration Successful")