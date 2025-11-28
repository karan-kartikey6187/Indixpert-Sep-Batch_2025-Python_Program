import uuid
import document_input
import ask_address_input
import ask_name_input
import review_data

def register_data():
    clint={
    "id":uuid.uuid4().hex[:13],
    "name":ask_name_input.ask_name(),
    "email":ask_address_input.ask_address(),
    "document":document_input.documents()
    }
    return clint
 

clint_data=register_data()
review_data.review(clint_data)

