users={
    1:{
        'name':'greeshma',
        'number':'9392375701',
        'email':'greeshmareddy2218@gmail.com'
    },
    2:{
        'name':'bunny',
        'number':'9494581244',
        'email':'bhargavipriya3@gmail.com'
    }
}

def add_contact(contact_id,username,number,email):
    print("we are in add contact")
    if contact_id in users:
        return "contact already exists"
    users[contact_id]={
        "name":name,
        "number":number,
        "email":email
    }
    return "contact added successfully"
    
def delete_contact(contact_id):
    print("we are in delete contact")
    if contact_id in users:
        del users[contact_id]
        return "contact deleted successfully"
    return "contact not found"
def show_contact(contact_id):
    print("we are in to show particular contact")
    if contact_id in users:
        return users[contact_id]
    return "contact not found"
def show_all_contacts():
    print("we are in show all contact")
    if len(users) == 0:
        print("No contacts available.")
    else:
        for cid, details in users.items():
            print("\nContact ID:", cid)
            print("Name :", details["name"])
            print("number:", details["number"])
            print("Email:", details["email"])

#main
if __name__=="__main__":
    while True:
        print("welcome to the contacts page")
        print("1.add contacts  \n 2.delete contact \n 3.show contact \n 4.show all contacts \n 5.exit")
        choice=int(input("enter your choice:"))
        if choice==1:
            contact_id=int(input("enter the contact id"))
            name=input("enter a name:")
            number=input("enter a number:")
            email=input("enter a mail:")
            contact=add_contact(contact_id,name,number,email)
            print("your contact is added:",contact)
        elif choice==2:
            contact_id=int(input("enter the contact id:"))
            result=delete_contact(contact_id)
            print("deleted contact is:",result)
        elif choice==3:
            contact_id=int(input("enter the contact id:"))
            result = show_contact(contact_id)
            if isinstance(result, dict):
                print("Name  :", result["name"])
                print("Number:", result["number"])
                print("Email :", result["email"])
            else:
                print(result)
        elif choice==4:
            result=show_all_contacts()
            print("all contacts are:",result)
        elif choice==5:
            print("thanks for the above operations")
            exit()
        else:
            print("invalid choice, select choice from 1 to 5")


            
