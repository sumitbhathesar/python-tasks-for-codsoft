class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        self.contacts[name] = {
            "phone_number": phone_number,
            "email": email,
            "address": address
        }
        print(f"Contact {name} added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for name, details in self.contacts.items():
                print(f"Name: {name}")
                print(f"Phone Number: {details['phone_number']}")
                print(f"Email: {details['email']}")
                print(f"Address: {details['address']}\n")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Name: {name}")
            print(f"Phone Number: {self.contacts[name]['phone_number']}")
            print(f"Email: {self.contacts[name]['email']}")
            print(f"Address: {self.contacts[name]['address']}")
        else:
            print("Contact not found.")

    def update_contact(self, name, phone_number=None, email=None, address=None):
        if name in self.contacts:
            if phone_number:
                self.contacts[name]['phone_number'] = phone_number
            if email:
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address
            print(f"Contact {name} updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print("Contact not found.")


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone_number, email, address)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            name = input("Enter name to search: ")
            contact_book.search_contact(name)
        elif choice == "4":
            name = input("Enter name to update: ")
            phone_number = input("Enter new phone number (press enter to skip): ")
            email = input("Enter new email (press enter to skip): ")
            address = input("Enter new address (press enter to skip): ")
            contact_book.update_contact(name, phone_number or None, email or None, address or None)
        elif choice == "5":
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)
        elif choice == "6":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()