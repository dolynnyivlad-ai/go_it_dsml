def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except Exception as e:
        return f'{e}'


def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Contact updated."
        else:
            return f"Contact {name} not found."
    except Exception as e:
        return f'{e}'


def phone_username(args, contacts):
    try:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return f"Contact {name} not found."
    except Exception as e:
        return f'{e}'


def show_phone(contacts):
    return contacts


# cercle request - response
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == 'add'.lower():
            print(add_contact(args, contacts))
        elif command == 'change'.lower():
            print(change_contact(args, contacts))
        elif command == 'phone'.lower():
            print(phone_username(args, contacts))
        elif command == 'show'.lower():
            print(show_phone(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
