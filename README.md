<h1 align="center">
  _PR0M3TH3US RANSOMWARE_
 </h1>
 
<img alt = "Compatible" src="https://img.shields.io/badge/Windows%20%26%20Linux-Compatible-brightgreen">


### ***DO NOT RUN THE CONTENTS OF THIS REPO WITHOUT KNOWING WHAT IT DOES! BY RUNNING THE CODE IN THIS REPOSITORY, YOU CLAIM FULL RESPONSIBILITY FOR ANY DATA LOSS YOU MIGHT SUFFER !!**


The code in this repository is for a ransomware. It is a malware and must not be run unknowingly. Your data could get encrypted and/or lost forever.
  
  I created this ransomware on python out of boredom and made it my personal project. It encrypts the files in the directory where the scripts are located and adds the ".pr0m3th3us" extension to them. You can clone this repository onto your computer using:
    
    git clone https://github.com/c0ncatenate/prometheus-ransomware
  
# Usage
## To encrypt files

1.  Open a Linux/Windows terminal in the directory where you cloned this repository.
2.  Run encrypt.py
    
    `python3 encrypt.py`
    
 
 You should see that the test files in the directory get encrypted and their extensions also change.
 
 **DO NOT RUN THE ENCRYPT FILE TWICE IN A ROW AS IT WILL DOUBLE ENCRYPT THE FILES AND OVERWRITE THE KEY FILE FOR THE FIRST ENCRYPTION, MAKING IT IMPOSSIBLE TO DECRYPT IT THE SECOND TIME.**
 
 ## To decrypt files
 
 1.  Open a Linux/Windows terminal in the directory where you cloned this repository.
 2.  Run decrypt.py
      
      `python3 decrypt.py`
 
 3.  Enter "hacking" as the secret phrase.


# TODO
-  ~~Conserve file extensions during encryption and return them after decryption.~~ ✔️
-  Create a more detailed GUI.
-  Create a local copy of the key file somewhere other than the FTP server.
-  Remove FTP functionality as it is difficult to configure OR create a better help section to configure the FTP.
  
    ...

# Disclaimer
I am not responsible for any damage you might cause with this tool. Use it at own risk for testing and learning purposes only! I made this for the sole reason of learning encryption and decryption in python. Please use this in a controlled testing lab environment such as a virtual machine and do not run on your host machine. I am not responsible for any data loss you might suffer due to this tool.
