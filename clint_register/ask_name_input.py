def ask_name():
    while True:
        first_name=input("Please Enter Your First Name: ")
        if first_name.isalpha()==True:
            break
        else: print("Invalid! Name Please Enter Only Latters.")
    while True:
        last_name=input("Please Enter Your Last Name: ")
        if last_name.isalpha()==True:
            break
        else: print("Invalid! Name Please Enter Only Latters.")    
    return first_name+" "+last_name