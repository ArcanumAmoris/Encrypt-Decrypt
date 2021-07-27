# Encrypt-Decrypt
Encrypt-Decrypt is a package you can use to easily encrypt and decrypt files, and even entire directories that you want to keep hidden from peering eyes.

## Installation
You can clone this repo into a new directory with the following commands.

```bash 
git clone https://github.com/ArcanumAmoris/Encrypt-Decrypt
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt.

```bash
cd Encrypt-Decrypt
pip install requirements.txt
```

## Usage
1. Run the generate_key.py script to generate a secret key with the following commands.

```bash 
python3 generate_key.py
```

2. Now that you have your secret key stored in secret.txt you can safely encrypt any file or directory. Simply run the encrypt.py script with the following commands.

```bash 
python3 encrypt.py
```

3. You will be prompted to select encrypt or decrypt. Select 1 to encrypt and 2 to decrypt.

4. After selecting encrypt/decrypt you will be prompted to select a file or directory which you would like to encrypt/decrypt. Enter the name of the file or directory and hit enter. 
If the file/directory you'd like to encrypt is not at the same directory level as you are presently in, simply copy-paste the full path to the file/directory. On windows make sure to remove the quotes. Incorrect: "full_path_example" Correct: full_path_example.

5. You should see "You have successfully encrypted/decrypted 'name of file'".

# IMPORTANT 
1. DO NOT LOSE YOUR KEY (secret.txt) FILE. IF YOU HAVE ENCRYPTED YOUR FILES AND LOSE YOUR KEY, YOU WILL NOT BE ABLE TO DECRYPT YOUR FILES.
2. DO NOT EDIT, COPY-PASTE, OR TAMPER WITH THE KEY IN ANY WAY. IF YOU DO THE KEY WILL BE USELESS. 


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)