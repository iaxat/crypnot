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

    def load_key(self, generate_key()):
            return open("secret.key", "rb").read()


    def result(self):
        print('------------------------------------------------------------')
        print('The program will start from here')
        print('')
        print('')
        

    