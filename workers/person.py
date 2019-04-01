import abc
import re

NUMBER_START_ID_COUNT = 0


class Person(object):
    _id = NUMBER_START_ID_COUNT

    def __init__(self, first_name, last_name, year_of_birth, email, phones, address):

        if first_name:
            self.first_name = first_name
        else:
            raise TypeError("first_name should not be empty")

        if last_name:
            self.last_name = last_name
        else:
            raise TypeError("last_name should not be empty")

        self.id = Person.add_id()

        self.year_of_birth = year_of_birth
        self.email = self.check_email(email)
        self.__phones = []

        for phone in phones:
            self.__phones.append(Phone(phone))

        if len(address) == 3:
            self.address = PobAddress(address)
        elif len(address) == 4:
            self.address = StreetAddress(address)

    @classmethod
    def add_id(cls):
        cls._id += 1
        return cls._id

    @staticmethod   # todo: ask if so ???
    def check_email(email):
        phone_re_pattern = r"^[a-zA-Z0-9]+@([a-zA-Z0-9]+.)*hwltd.com$"
        res = re.match(phone_re_pattern, email)
        if res:
            return email
        else:
            raise ValueError("the Email don't match the pattern")


class Phone(object):

    def __init__(self, number):
        phone_re_pattern = r"[+/d]?[-/d]*"
        res = re.match(phone_re_pattern, number)
        if res:
            self.number = number
        else:
            # error while constructing an object dont construct one at all.
            raise ValueError("the Phone number don't match the pattern")


class Address(object):
    def __init__(self, country, city):
        if not country and not city:
            raise TypeError("Address must have a country and a city")

        self.country = country
        self.city = city

    def __str__(self):
        return f'{self.country} city: {self.city} {self._address_details}'

    @property
    @abc.abstractmethod
    def _address_details(self):
        raise NotImplementedError("you need to use StreetAddress or PobAddrees methods instead")


class StreetAddress(Address):
    def __init__(self, country, city, street_name, house_number):
        super.__init__(country, city)
        self.street_name = street_name
        self.house_number = house_number

    @property
    def _address_details(self):
        return f'street: {self.street} Num: {self.house_number}'


class PobAddress(Address):
    def __init__(self, country, city, post_number):
        super.__init__(country, city)
        self.post_number = post_number

    @property
    def _address_details(self):
        return f'Post Office Number:{self.post_number}'
