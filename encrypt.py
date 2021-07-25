from genericpath import isdir
from cryptography.fernet import Fernet
import os

with open('secret.txt', 'rb') as filekey:
    key = filekey.read()

fernet = Fernet(key)

def encrypt(selected_file):
    with open(selected_file, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(selected_file, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
        print(f"You have successfully encrypted {selected_file}")


def decrypt(selected_file):
    with open(selected_file, 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(selected_file, 'wb') as dec_file:
        dec_file.write(decrypted)
        print(f"You have successfully decrypted {selected_file}")

def user_select():
    encrypt_or_decrypt = int(input("Select 1 to encrypt, or 2 to to decrypt your file :"))
    if encrypt_or_decrypt == 1:
        selected_file = str(input("Select a file you would like to encrypt :"))
        if isdir(selected_file):
            loop_through_all_files(encrypt_or_decrypt, selected_file)
        else:
            return encrypt(selected_file)
    elif encrypt_or_decrypt == 2:
        selected_file = input("Select a file to decrypt :")
        if isdir(selected_file):
            loop_through_all_files(encrypt_or_decrypt, selected_file)
        else:
            return decrypt(selected_file)
    else:
        return print("Enter a valid input  ")


def loop_through_all_files(enc_or_dec, encrypt_or_decrypt):
    directory = encrypt_or_decrypt
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            filepath = subdir + os.sep + file
            if enc_or_dec == 1:
                encrypt(filepath)
            else:
                decrypt(filepath)

user_select()
