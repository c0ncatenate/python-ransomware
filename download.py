#!/usr/bin/python3

import ftplib
import os
import colorama

HOSTNAME = '<hostname>'
USERNAME = '<username>'
PASSWORD = '<password>'

# Connect to the FTP server
ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)

# force UTF-8 encoding
ftp_server.encoding = "utf-8"

filename = 'thekey.key'

with open(filename, 'wb') as file:
    ftp_server.retrbinary(f'RETR {filename}', file.write)

ftp_server.dir()

