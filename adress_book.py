from collections import UserDict
from datetime import datetime

class Field:
    pass
       
class Bithday(Field):    #  'dd mm yyyy'
    
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if <condishion>:
            self.__value = new_value


class Phone(Field):
    def __init__(self, phone):
        self.__phone = None
        self.phone = phone


    @property
    def phone(self):
        return self.__value

    @phone.setter
    def phone(self, new_value):
        if < condishion >:
            self.__value = new_value

class Name(Field):
    def __init__(self, name):
        self.name = name


class Record:
    def __init__(self, name: Name, bithday: Bithday = None, *phones):
        self.name = name
        self.bithday = bithday
        self.phones = list(phones)
    
    def add_phone(self, phone_number: Phone):
        self.phones.append(phone_number)

    def change_phone(self, phone_number_old: Phone, phone_number_new: Phone):
        self.phones.remove(phone_number_old)
        self.phones.append(phone_number_new)

    def del_phone(self, phone_number: Phone):
        self.phones.remove(phone_number)

    def days_to_birthday(self):
        if self.bithday:
            current_datetime = datetime.now()
            bd_date = datetime.strptime(self.bithday, '%d %m %Y').date()
            bithday_this_year = datetime(
                current_datetime.year, bd_date.month, bd_date.day)
            if bithday_this_year.date() >= current_datetime.date():
                days_delta = bithday_this_year.date() - current_datetime.date()

            else:
                days_delta = datetime(current_datetime.year + 1, bd_date.month,
                                    bd_date.day).date() - current_datetime.date()
            return days_delta.days


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.name] = record
