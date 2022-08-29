
import string

from random import choice
from random import randint
import names


class Utils:

    @staticmethod
    def gen_random_date():
        day = randint(1, 31)
        month = randint(1, 12)
        year = randint(1900, 2021)
        date = f"{str(day).zfill(2)}/{str(month).zfill(2)}/{str(year)}"
        return date

    @staticmethod
    def gen_random_phone_nr():

        number = randint(111111111, 999999999)
        return str(number)

    @staticmethod
    def gen_random_name():

        name = names.get_first_name()
        return name

    @staticmethod
    def gen_random_surname():

        surname = names.get_last_name()
        return surname

    @staticmethod
    def gen_random_email():
        char_num = randint(3, 12)
        rand_char = ''.join(choice(string.ascii_letters) for i in range(char_num))
        return rand_char + "@gmail.com"

