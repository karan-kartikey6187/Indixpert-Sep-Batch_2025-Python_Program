documents_list=[]
def documents():
      for i in range(3):
        document_dic={}
        document_dic={
        "document":input(f"Please Enter Your Document {i+1} Name: "),
        "image":input("Paste Your Image Link Here: ")
        }
        documents_list.append(document_dic)
      return documents_list