def Create_files():
    try:
        number=int(input("How Many File You Want To Create: "))
        for i in range(number):
            with open(f"File {i+1}.txt",'w') as f:
                f.write(f"This is File Number {i+1}")
        print(f"All {number} Files Created Successfully.")
    except Exception:
        print("Invalid Input! Please Enter Only Numbers Not Character")
        Create_files()

Create_files()