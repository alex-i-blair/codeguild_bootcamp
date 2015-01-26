import os
import sys


def add():
    name = raw_input("Name of contact: ")
    os.system('clear')
    phone_number = raw_input("Phone#: ")
    os.system('clear')
    email_address = raw_input("Email: ")
    os.system('clear')
    address = raw_input("Street address: ")
    os.system('clear')

    contact = {"Name": name, "Phone Number": phone_number, "Email Address": email_address, "Street Address": address}

    print contact["Name"]
    print "Phone Number:  %s" % contact["Phone Number"]
    print "Email Address:  %s" % contact["Email Address"]
    print "Street Address:  %s" % contact["Street Address"]
    return contact


def contact(address_book, name):
    for contact in address_book:
        if contact["Name"] == name:
            os.system('clear')
            print contact["Name"]
            print "Phone Number:  %s" % contact["Phone Number"]
            print "Email Address:  %s" % contact["Email Address"]
            print "Street Address:  %s" % contact["Street Address"]


def print_contact_names(address_list):
    for contact in address_list:
        print contact["Name"]


def new_contact():
    os.system('clear')
    contact = add()
    address_book.append(contact)
    start_over()


def view_contact():
    os.system('clear')
    print_contact_names(address_book)
    contact = raw_input("Which contact card would you like to view?: ")
    contact(address_book, contact)
    start_over()


def delete_contact():
    os.system('clear')
    print_contact_names(address_book)
    delete = raw_input("Which contact would you like to delete?: ")
    for index, contact in enumerate(address_book):
        if contact["Name"] == delete:
            del address_book[index]
    print_contact_names(address_book)
    start_over()


def start_over():
    start_over = raw_input("Return to main menu?: ").lower()
    if start_over == "y" or start_over == "yes":
        main()
    else:
        sys.exit()


def main():
    while True:
        os.system('clear')
        print home[1]
        print home[2]
        print home[3]
        print home[4]
        print home[5]
        selection = raw_input("What would you like to do?:  ")
        if selection == "1":
            new_contact()
        elif selection == "2":
            view_contact()
        elif selection == "3":
            delete_contact()
        elif selection == "4":
            save()
        elif selection == "5":
            sys.exit()


def save():
    f = open("address_book.txt", 'a')
    external_ab = []
    for contact in address_book:
        for key in contact:
            external_ab.append(key + "\t")
            external_ab.append(contact[key] + "\n")
    f.write("".join(external_ab))
    f.close()

# def read():

address_book = []
home = {1: "1)  Add new contact", 2: "2)  View a contact",
        3: "3)  Delete a contact", 4: "4)  Save to disk", 5: "4)  Exit"}

main()

