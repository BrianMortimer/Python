import hashlib
import os

users = {}

def addUser():
    username = input('Enter username: ')
    password = input('Enter password: ')

    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return username, salt, key


def verification(users):
    username = 'brian'

    password = input('Enter password: ')

    salt = users[username]['salt']
    key = users[username]['key']

    new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

    if new_key == key:
        print('Correct')
    else:
        print('incorrect')

newUser = addUser()
users[newUser[0]] = {'salt': newUser[1], 'key': newUser[2]}
verification(users)