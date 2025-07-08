from functools import wraps

def parse_input_validator(func):
    @wraps(func)
    def wrapper(user_input):
        if not user_input:
            return "Invalid input. Please enter a command."
        return func(user_input)
    return wrapper

@parse_input_validator
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact_validator(func):
    @wraps(func)
    def wrapper(args, contacts):
        if len(args) != 2:
            return "Invalid number of arguments. Usage: add <name> <phone>"
        name, phone = args
        if not name or not phone:
            return "Name and phone cannot be empty."
        if name in contacts:
            return "Contact already exists."
        return func(args, contacts)
    return wrapper

@add_contact_validator
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def list_contacts_validator(func):
    @wraps(func)
    def wrapper(contacts):
        if not isinstance(contacts, dict) or not contacts:
            return "No contacts found."
        return func(contacts)
    return wrapper

@list_contacts_validator
def list_contacts(contacts):
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def find_contact_validator(func):
    @wraps(func)
    def wrapper(args, contacts):
        if len(args) != 1:
            return "Invalid number of arguments. Usage: find <name>"
        return func(args, contacts)
    return wrapper

@find_contact_validator
def find_contact(args, contacts):
    name = args[0]
    phone = contacts.get(name)
    return f"{name}: {phone}" if phone else "Contact not found."

def change_contact_validator(func):
    @wraps(func)
    def wrapper(args, contacts):
        if len(args) != 2:
            return "Invalid number of arguments. Usage: change <name> <new_phone>"
        return func(args, contacts)
    return wrapper

@change_contact_validator
def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "list":
            print(list_contacts(contacts))
        elif command == "find":
            print(find_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
