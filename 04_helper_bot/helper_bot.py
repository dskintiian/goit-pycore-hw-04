from colorama import Fore, Back, Style


def parse_command(input_sting: str):
    try:
        command, *args = input_sting.split()
        return command.strip().lower(), *args

    except ValueError:

        return None, None


def main():
    contacts = {}

    print(hello_handler())
    print(help_handler())
    try:
        while True:
            command, *arguments = parse_command(input('>>'))

            match command:
                case 'hello':
                    print(hello_handler())
                case 'exit':
                    print(format_success('Good bye!'))
                    break
                case 'close':
                    print(format_success('Good bye!'))
                    break
                case 'add':
                    if len(arguments) < 2:
                        print(format_error('Please enter two arguments separated by a space.'))
                        continue

                    phone = arguments.pop()
                    # support double names like Martin James
                    name = ' '.join(arguments)
                    print(add_contact_handler(contacts, name, phone))
                case 'change':
                    if len(arguments) < 2:
                        print(format_error('Please enter two arguments separated by a space.'))
                        continue

                    phone = arguments.pop()
                    # support double names like Martin James
                    name = ' '.join(arguments)
                    print(change_contact_handler(contacts, name, phone))
                case 'phone':
                    if len(arguments) < 1:
                        print(format_error('Please enter an argument.'))
                        continue

                    print(get_contact_handler(contacts, ' '.join(arguments)))
                case 'all':
                    for name in contacts.keys():
                        print(f'{name}: {contacts[name]}')
                case 'help':
                    print(help_handler())
                case _:
                    print(format_error('Invalid command.'))
                    print(help_handler())
    except KeyboardInterrupt:
        print(format_success('\nGood bye!'))


def hello_handler():
    return 'Hello, how can I help you?'


def help_handler():
    return f'''Possible commands:
{Fore.YELLOW}{Back.BLUE}help{Style.RESET_ALL} - prints list of available commands
{Fore.YELLOW}{Back.BLUE}hello{Style.RESET_ALL} - prints a greeting 
{Fore.YELLOW}{Back.BLUE}add [name] [phone number]{Style.RESET_ALL} - create a contact with a phone number
{Fore.YELLOW}{Back.BLUE}change [name] [phone number]{Style.RESET_ALL} - changes a contact phone number 
{Fore.YELLOW}{Back.BLUE}phone [name]{Style.RESET_ALL} - prints contacts phone number
{Fore.YELLOW}{Back.BLUE}all{Style.RESET_ALL} - prints all contacts
{Fore.YELLOW}{Back.BLUE}close{Style.RESET_ALL} або {Fore.YELLOW}{Back.BLUE}exit{Style.RESET_ALL} - terminates a program    
    '''


def add_contact_handler(contacts: dict, name: str, phone: str):
    name = name.lower().capitalize()
    contacts[name] = phone
    return format_success('Contact added')


def change_contact_handler(contacts: dict, name: str, phone: str):
    name = name.lower().capitalize()
    if name in contacts.keys():
        contacts[name] = phone
        return format_success('Contact updated.')

    return format_error('Contact not found.')


def get_contact_handler(contacts: dict, name: str):
    name = name.lower().capitalize()
    if name in contacts.keys():
        return contacts[name]

    return format_error('Contact not found.')


def format_error(error: str):
    return f'{Fore.WHITE}{Back.RED}{error}{Style.RESET_ALL}'


def format_success(message: str):
    return f'{Fore.GREEN}{message}{Style.RESET_ALL}'


if __name__ == '__main__':
    main()
