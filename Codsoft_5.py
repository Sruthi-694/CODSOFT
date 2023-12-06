class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print(f"Contact {name} added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts.")
        else:
            for contact in self.contacts:
                print(contact)

    def search_contact(self, name):
        found_contacts = [contact for contact in self.contacts if contact.name == name]
        if found_contacts:
            for contact in found_contacts:
                print(contact)
        else:
            print(f"No contact found with name {name}.")

    def update_contact(self, name, new_phone, new_email):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = new_phone
                contact.email = new_email
                print(f"Contact {name} updated.")
                return
        print(f"No contact found with name {name}.")

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]
        print(f"Contact {name} deleted.")


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

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_book.add_contact(name, phone, email)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            name = input("Enter name to search: ")
            contact_book.search_contact(name)
        elif choice == '4':
            name = input("Enter name to update: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            contact_book.update_contact(name, new_phone, new_email)
        elif choice == '5':
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)
        elif choice == '6':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
