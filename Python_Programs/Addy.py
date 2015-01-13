import os
import sys
def add():
	Name = raw_input("Name of Contact: ")
	os.system('clear')
	PhoneNumber = raw_input("Phone#: ")
	os.system('clear')
	EmailAddress = raw_input("Email: ")
	os.system('clear')
	Address = raw_input("Street address: ")
	os.system('clear')

	Contact = {"Name":Name, "Phone Number":PhoneNumber, "Email Address":EmailAddress, "Street Address":Address} 
	
	print Contact["Name"]
	print "Phone Number:  %s" % Contact["Phone Number"]
	print "Email Address:  %s" % Contact["Email Address"]
	print "Street Address:  %s" % Contact["Street Address"]
	return Contact

def contact(address_book, Name):
	for Contact in address_book:
		if Contact["Name"] == Name:
			os.system('clear')
			print Contact["Name"]
			print "Phone Number:  %s" % Contact["Phone Number"]
			print "Email Address:  %s" % Contact["Email Address"]
			print "Street Address:  %s" % Contact["Street Address"]
			
def print_contact_names(address_list):
	for Contact in address_list:
		print Contact["Name"]

def new_contact():
	os.system('clear')
	Contact = add()
	address_book.append(Contact)
	start_over()
			
def view_contact():
	os.system('clear')
	print_contact_names(address_book)
	Contact = raw_input("Which contact card would you like to view?: ")
	contact(address_book, Contact)
	start_over()
		
def delete_contact():
	os.system('clear')
	print_contact_names(address_book)
	delete = raw_input("Which contact would you like to delete?: ")
	for index, Contact in enumerate(address_book):
		if Contact["Name"] == delete:
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
	for Contact in address_book:
		for key in Contact:
			external_ab.append(key + "\t")
			external_ab.append(Contact[key] + "\n")
	f.write("".join(external_ab))
	f.close()

# def read():

address_book = []
home = {1:"1)  Add new contact", 2:"2)  View a contact", 3:"3)  Delete a contact", 4:"4)  Save to disk", 5:"4)  Exit"}

main()

