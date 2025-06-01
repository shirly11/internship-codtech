# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 22:14:56 2025

@author: ADMIN
"""
#1/6/25
# Contact Book Application

contacts = {}

def add_contact():
    name = input("Enter name: ").strip()
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print(f" Contact '{name}' added successfully.\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    print("\n Contact List:")
    for name, info in contacts.items():
        print(f"• {name} - {info['phone']}")
    print()

def search_contact():
    key = input("Enter name or phone number to search: ").strip().lower()
    found = False
    for name, info in contacts.items():
        if key in name.lower() or key in info['phone']:
            print(f"\n Contact Found:\n  Name: {name}\n  Phone: {info['phone']}\n  Email: {info['email']}\n  Address: {info['address']}\n")
            found = True
            break
    if not found:
        print(" Contact not found.\n")

def update_contact():
    name = input("Enter the name of the contact to update: ").strip()
    if name in contacts:
        print("Enter new details (leave blank to keep current value):")
        phone = input(f"New phone [{contacts[name]['phone']}]: ").strip()
        email = input(f"New email [{contacts[name]['email']}]: ").strip()
        address = input(f"New address [{contacts[name]['address']}]: ").strip()

        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address

        print(f"Contact '{name}' updated.\n")
    else:
        print(" Contact not found.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        confirm = input(f"Are you sure you want to delete '{name}'? (yes/no): ").strip().lower()
        if confirm == 'yes':
            del contacts[name]
            print(f"Contact '{name}' deleted.\n")
    else:
        print(" Contact not found.\n")

def main():
    while True:
        print(" Contact Book Menu")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print(" Exiting Contact Book. Goodbye!")
            break
        else:
            print(" Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
