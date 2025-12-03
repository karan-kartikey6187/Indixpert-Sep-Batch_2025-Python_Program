import requests
import json

def by_id():
    json_response=requests.get("https://jsonplaceholder.typicode.com/users")
    json_response=json_response.json()
    id=input("Please Enter ID: ")
    found=False
    for data in json_response:
        if str(data["id"])==id:
            print(json.dumps(data,indent=4))
            found=True
            return

    if not found:
       print("No Record Found!")

def by_email():
    json_response=requests.get("https://jsonplaceholder.typicode.com/users")
    json_response=json_response.json()
    email=input("Please Enter Email: ")
    found=False
    for data in json_response:
        if str(data["email"])==email:
            print(json.dumps(data,indent=4))
            found=True
            return

    if not found:
       print("No Record Found!")

def by_address_city():
    json_response=requests.get("https://jsonplaceholder.typicode.com/users")
    json_response=json_response.json()
    city=input("Please Enter City Name: ")
    found=False
    for data in json_response:
            if data["address"]["city"].lower()==city.lower():
                print(json.dumps(data,indent=4))
                found=True
                return
    if not found:
       print("No Record Found!")            

def by_address_zip_code():
    json_response=requests.get("https://jsonplaceholder.typicode.com/users")
    json_response=json_response.json()
    zipcode=input("Please Enter Zip Code: ")
    found=False
    for data in json_response:
            if data["address"]["zipcode"]==zipcode:
                print(json.dumps(data,indent=4))
                found=True
                return

    if not found:
       print("No Record Found!")

def by_addess_longitude():
    json_response=requests.get("https://jsonplaceholder.typicode.com/users")
    json_response=json_response.json()
    longitude=input("Please Enter Longitude: ")
    found=False
    for data in json_response:
            if data["address"]["geo"]["lng"]==longitude:
                print(json.dumps(data,indent=4))
                found=True
                return

    if not found:
       print("No Record Found!")

def by_addess_latitude():
    json_response=requests.get("https://jsonplaceholder.typicode.com/users")
    json_response=json_response.json()
    latitude=input("Please Enter Latitude: ")
    found=False
    for data in json_response:
            if data["address"]["geo"]["lat"]==latitude:
                print(json.dumps(data,indent=4))
                found=True
                return

    if not found:
       print("No Record Found!")      
