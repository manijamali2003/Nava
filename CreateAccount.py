#!/usr/bin/env python3
import os
import socket, random,hashlib
from Nava import  *

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65433        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode('utf-8')
            if data:
                try:
                    split = data.split(',')

                    username = split[0] # manijamali2003
                    if not os.path.isfile (f'Etc/Users Account/{username}'):
                        fullname = split[1] # Mani Jamali
                        gender   = split[2] # 0: Male, 1: Female
                        birthday = split[3] # yyyy/mm/dd
                        countryc = split[4] # IR
                        city     = split[5] # Mashhad
                        zipcode  = split[6] # 11111111
                        hashcode = split[7] # hash of password sha3_513

                        f = open(f'Etc/Users Account/{username}','wb')
                        f.write(f'{fullname},{gender},{birthday},{countryc},{city},{zipcode},{hashcode}'.encode())
                        f.close()

                        key = KeyCreator()

                        f = open(f'Etc/Users Account/Public Keys/{username}.pem','wb')
                        f.write(key.public) # you should create it
                        f.close()

                        conn.sendall(key.private)
                        conn.sendall(key.public)
                    else:
                        conn.sendall(b'e: account exists')
                except:
                    conn.sendall(b'e: some errors')