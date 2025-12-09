def ask_address():
    while True:
        email = input("Please Enter Your Email Address: ")
        if "@" in email and "." in email:
            break
        else: print("Invalid! Email Try Again.")
    return email
