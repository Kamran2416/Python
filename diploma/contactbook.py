contact_book={"irqan":{'city': "Mumbai",
                        'phone':'2355623524','emil':"irqan@gmail"},
              "Kamran":{'city': "Mumbai",
                        'phone':'8345878543','emil':"kamran@gmail"},
              "Hassan":{'city': "Mumbai",
                        'phone':'3749486537','emil':"hassan@gmail",}}



def add_contact():
    name=input("Enter The Name: ")
    city=input("Enter The City Name: ")
    phone=input("Enter The Phone Number: ")
    email=input("Enter The Email Address: ")
    if ((len(name) < 2) or (len(city) < 2) or (len(phone) < 10) or (len(email) < 8)):
        print("Error :Invalid fields")
        return

    contact_book[name]={"City":city,"phone": phone,"email":email}

def search_contact(name):
    if name in contact_book:
        print("You Searched "+ name,contact_book[name])
    else:
        print("Contact not Found ")

def delte_contact(name):
    if name in contact_book:
        del contact_book[name]
    else:
        print("Contact Not Found ")

def update_contact(name):
    if name in contact_book:
        add_contact()
    else:
        print("\nContact not Found ")

def print_contact():
    print("\nContact List is: ")
    for k ,v in contact_book:
        print(k,v['phone'])


add_contact()
update_contact("Ronaldo")
delte_contact("Hassan")
search_contact("Kamran")
print_contact()

