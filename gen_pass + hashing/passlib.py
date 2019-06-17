import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from selenium import webdriver
import random
import string
import datetime


letters = string.ascii_letters + string.digits + string.punctuation
number_of_letters = 12


def pass_gen():

     return "".join([random.choice(letters) for _ in range(number_of_letters)])


def data_gen(filename):

    string = f"{datetime.date.today()}\nfacebook: {pass_gen()}\ngmail: {pass_gen()}\ngithub: {pass_gen()}"
    encrypt(filename,string.encode())




def get_key():

    password_provided = input("Eneter a password: ")
    password = password_provided.encode()

    salt=b'fJr\xf1\xcc}%\x8d\x96\r\x10\xd9\xe7\xaf\xa7\xab'

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=10000,
        backend=default_backend()
    )
    key=base64.urlsafe_b64encode(kdf.derive(password))
    return key


def encrypt(filename,data):

    fernet=Fernet(get_key())
    encrypted = fernet.encrypt(data)

    with open(filename, "wb") as f:
        f.write(encrypted)
    return encrypted


def decrypt(filename):

    with open(filename,'rb') as f:
        data=f.read()
    try:
        fernet=Fernet(get_key())
        decrypted = fernet.decrypt(data)
        print(decrypted.decode())
        return decrypted
    except:
        print("Wrong password!!!")


def get_passwords(filename):

    data = decrypt(filename).decode().split("\n")
    password=list()
    for i in range(1,4):
        password.append(data[i].split(" ")[1])
    return password #<- password : 1.Facebook, 2.Gmail, 3.Github

def facebook(email,password):

    browser = webdriver.Firefox()
    browser.get("https://www.facebook.com")
    python_button = browser.find_elements_by_xpath('//*[@id="email"]')[0]
    python_button.send_keys(email)
    python_button = browser.find_elements_by_xpath('// *[ @ id = "pass"]')[0]
    python_button.send_keys(password)
    #python_button = browser.find_elements_by_xpath('//*[@id="loginbutton"]')[0]
    #python_button.click()

def gmail(email,password):

    browser = webdriver.Firefox()
    browser.get("https://www.gmail.com")
    python_button = browser.find_elements_by_xpath('// *[ @ id = "identifierId"]')[0]
    python_button.send_keys(email)
    python_button = browser.find_elements_by_xpath('//*[@id="identifierNext"]')[0]
    python_button.click()
    python_button = browser.find_elements_by_xpath('//*[@id="password"]')[0]
    python_button.send_keys(password)
    #python_button = browser.find_elements_by_xpath('//*[@id="passwordNext"]')[0]
    #python_button.click()

def github(email,password):

    browser = webdriver.Firefox()
    browser.get("https://github.com/login")
    python_button = browser.find_elements_by_xpath('//*[@id="login_field"]')[0]
    python_button.send_keys(email)
    python_button = browser.find_elements_by_xpath('//*[@id="password"]')[0]
    python_button.send_keys(password)
    #python_button = browser.find_elements_by_xpath('/ html / body / div[3] / main / div / form / div[3] / input[4]')[0]
    #python_button.click()


