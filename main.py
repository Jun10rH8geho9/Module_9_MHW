def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'No user with this name'
        except ValueError:
            return "Give me name and number please"
        except IndexError:
            return "Enter user name and number please"
    return inner

@input_error
    # Привітання
def greeting():
    return "How can I help you?"

    # Створили словник контактів
contacts = {}

    # 1. Створюємо, зберігаємо та виводимо новий контакт.
@input_error 
def new_contact(command):
    name = command.split(' ')[1]
    number = command.split(' ')[2]
    contacts[name] = number
    return f"Контакт {name} з номером телефону {number} було збережено."

    # 2. Зберігаємо в пам'яті новий номер телефону для існуючого контакту
@input_error   
def change_number(command):
    name = command.split(' ')[1]
    new_number = command.split(' ')[2]
    if name in contacts:
        contacts[name] = new_number
        return(f"Номер телефону контакту {name} було замінено на {new_number}.")
    else:
        return("Контакт не знайдено.")
    
    # 3. Виводить у консоль номер телефону для зазначеного контакту
@input_error
def number_by_name(command):
    name = command.split(' ')[1]
    if name in contacts:
        return contacts[name]
    else:
        return "Контакт не знайдено."
    # 4. Виводимо всі номери які записали    
@input_error
def print_all_contacts():
    for name, number in contacts.items():
        print(f"Контакт: {name}, Номер телефону: {number}")

#Користувач вводить абракадабру
def unknown_command(command):
    return f"Ви ввели невідому команду: {command}"

def command_handler():
    while True:
        command = input("Введіть команду: ").lower()
        if command == "exit" or command == "close" or command == "good bye":
            print("Good bye!")
            break
        elif command == "hello":
            print(greeting())
            # 1. Створюємо, зберігаємо та виводимо новий контакт.
        elif command.startswith("add"):
            print(new_contact(command))
            # 2. Зберігає в пам'яті новий номер телефону для існуючого контакту
        elif command.startswith("change"):
            print(change_number(command))
            # 3. Виводимо у консоль номер телефону для зазначеного контакту
        elif command.startswith("phone"):
            print(number_by_name(command))
            # 4. Виводимо всі номери які записали
        elif command == "show all":
            print_all_contacts()
        else:
            print(unknown_command(command))
       
if __name__ == "__main__":
    command_handler()