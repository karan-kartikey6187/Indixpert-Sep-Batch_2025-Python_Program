import json
clint_all_data=[]

def review(data):
    i=1
    print(">>>>>>>>>>>>Client Details<<<<<<<<<<<<<")
    for key,value in data.items():
        if key != "document":
            print(f"{key}-{value}")        
    for doc in data["document"]:
        print(f"{key} {i}:",end="")
        print(f" name-{doc['document']} , image-{doc['image']}") 
        i+=1     
    while True:
        print("1.Submit") 
        print("2.Cancel")   
        choice=int(input("Enter Your Choice: "))
        if choice==1:
            clint_all_data.append(data)
            print(json.dumps(clint_all_data,indent=5))
            print("Submitted Successfully.")
            break
        elif choice==2:
            print("Cancelled Successfully.") 
            break
        else: 
            print("Invalid! Choice.")  