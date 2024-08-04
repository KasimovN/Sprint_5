import random


class RandomCreds:
    @staticmethod
    def random_email():
        return f'nikolai_kasimov_12_{random.randint(100, 999)}@yandex.ru'

    @staticmethod
    def random_password():
        chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        length = 6
        password = ''
        for i in range(length):
            password += random.choice(chars)
        return password

