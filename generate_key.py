from cryptography.fernet import Fernet

with open("secret.txt", 'wb') as f:
    f.write(Fernet.generate_key())