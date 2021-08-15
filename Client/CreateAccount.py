#!/usr/bin/env python3

import socket,os,getpass,hashlib

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65433        # The port used by the server

username = input('Enter your new username: ').lower()
fullname = input('Enter your full name: ')
while True:
    password = getpass.getpass('Choose a new strong password: ')
    confirm = getpass.getpass('Confirm your password: ')
    if password==confirm:
        break

gender   = input('Choose your gender: ')
birthday = input('Enter your birthday: ')
countryc = input('Enter your country code: ').upper()
city     = input('Enter your city: ')
zipcode  = input('Enter your zipcode: ')

hashcode = hashlib.sha512(password.encode()).hexdigest()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall((f"{username},{fullname},{gender},{birthday},{countryc},{city},{zipcode},{hashcode}").encode())

    key = s.recv(2048).decode('utf-8')

    if not key.startswith('e: '):
        f = open('Wallet Keys/Private Key.pem', 'wb')
        f.write(key.encode())
        f.close()

        f = open('Wallet Keys/Public Key.pem', 'wb')
        f.write(s.recv(1024))
        f.close()

        f = open('Wallet Keys/Bank Key.pem', 'wb')
        f.write(s.recv(1024))
        f.close()
        print('Account created successfully')
    else:
        print(key)