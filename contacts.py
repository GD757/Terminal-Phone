

# add the create function

def add_contact(name, phone, contacts):
    try:
        if name != str and phone != int:
            raise TypeError('name must be a string and number must be a number')
        if name and phone not in contacts:
            contacts[name] = phone
            print("contact added.")
    except TypeError as e:
        print(f"Error: {e}")


# create the add function

def list_contacts(contacts):
    if not contacts:
        print("no contacts found")
    else:
        for name, phone in contacts.items():
            print(f"name: {name}, phone: {phone}")



    


