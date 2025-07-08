from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
    # Не потребує додаткових реалізацій
		pass

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        # перевірка номера (10 цифр)
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("Phone number must contain exactly 10 digits")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone (self, phones):
        try:
            phone = Phone(phones)
            self.phones.append(phone)
        except ValueError as i:
            print(f"Error adding phone: {i}")

    def edit_phone(self, old_number, new_number):
        for idx, phone in enumerate(self.phones):
            if phone.value == old_number:
                try:
                    self.phones[idx] = Phone(new_number)
                    return True
                except ValueError as e:
                    print(f"Error editing phone: {e}")
                    return False
        print("Old number not found")
        return False

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def remove_phone(self, phones):
        self.phones = [phone for phone in self.phones if phone.value != phones]

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")


# Так, користовувася і чатом в тому числі, але всеодно я багато аналізував та вивчав як це зробити
# досить складна тема тому мені дуже прикро що я не зміг це зробити самостійно.
# Я буду вдосконалювати свої навички щоби все це можна було прописати самому
