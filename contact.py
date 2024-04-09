class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("Contact list is empty.")
            return
        print("Contact List:")
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, keyword):
        found_contacts = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, index, updated_contact):
        self.contacts[index] = updated_contact

    def delete_contact(self, index):
        del self.contacts[index]

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_manager.add_contact(contact)
            print("Contact added successfully!")

        elif choice == '2':
            contact_manager.view_contacts()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            found_contacts = contact_manager.search_contact(keyword)
            if found_contacts:
                print("Found contacts:")
                for contact in found_contacts:
                    print(f"Name: {contact.name}, Phone: {contact.phone_number}")
            else:
                print("No contacts found.")

        elif choice == '4':
            index = int(input("Enter the index of the contact to update: "))
            if 0 <= index < len(contact_manager.contacts):
                name = input("Enter name: ")
                phone_number = input("Enter phone number: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                updated_contact = Contact(name, phone_number, email, address)
                contact_manager.update_contact(index, updated_contact)
                print("Contact updated successfully!")
            else:
                print("Invalid index.")

        elif choice == '5':
            index = int(input("Enter the index of the contact to delete: "))
            if 0 <= index < len(contact_manager.contacts):
                contact_manager.delete_contact(index)
                print("Contact deleted successfully!")
            else:
                print("Invalid index.")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()