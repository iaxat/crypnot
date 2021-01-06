# Encrypt and Decrypt the Text Files

import os
import system
from cryptography import fernet
import random
import time
import json
import numpy
import math
import pandas

# The class section is made for the class for image and text encryption
# The libraries will be used for the encryption and decryption for the data

class Crypnot():
    def generate_key(self):
        # This will generate the key and save it
        key = fernet.generate_key()
        with open('secret.key','wb') as key_file:
            key_file.write(key)

        return key_file

    def load_key(self):
            return open("secret.key", "rb").read()


    def encrypt_message(self,message):
        key = load_key()
        encoded_msg = message.encode()
        f = fernet(key)
        encrypted_message = f.encrypt(encoded_msg)
        print(encrypted_message)

    def read_file(self,input_file):
        with open(input_file,'r') as input_file_open:



    def decrypt_message(self):    
    


    def text_option:



    def file_option:


    def image_option:




    def start(self):
        print('------------------------------------------------------------')
        print('The program will start from here')
        print('')
        print('')
        option = input('Encrypt Options: 1.Text  2.File  3.Image')
        if option == '1':
            print('Awesome you have selected Text Option')
            text_option()
        elif option == '2':
            print('Awesome you have selected File Option')
            file_option()
        elif option == '3':
            print('Awesome you have selected Image Option')
            image_option()