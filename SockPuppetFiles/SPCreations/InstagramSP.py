#Imports.

from ast import Pass
import random
import string
import instabot

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select as WebSelect
from webdriver_manager.chrome import ChromeDriverManager

#Local variable imports.

from SockPuppetFiles.SPCreations.GmailSP import Gmail

class AccountCreation():

    #Set global variables:

    global Full_Name

    global Username

    global Password

    Full_Name = "".join(random.choices(string.ascii_letters + string.digits) , k = 15)

    Username = "".join(random.choices(string.ascii_letters + string.digits) , k = 10)

    Password = "".join(random.choice(string.ascii_letters + string.digits) , k = 18)

class AccountCreationDataInput():

    #Define the driver for account creation:

    Instagram_Driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    #Get the Instagram page to sign up to.

    Instagram_Driver.get("https://www.instagram.com/accounts/emailsignup/")

    #Search for the input box:

    Gmail_Input = Instagram_Driver.find_element_by_name("emailOrPhone") #Input the Gmail into the sign-up page.

    Gmail_Input.send_keys(Gmail)

    FN_Input = Instagram_Driver.find_element_by_name("fullName") #Input the First Name into the sign-up page.

    FN_Input.send_keys(Full_Name)

    U_Input = Instagram_Driver.find_element_by_name("username") #Input the Username into the sign-up page.

    U_Input.send_keys(Username)

    P_Input = Instagram_Driver.find_element_by_name("password") #Input the Password into the sign-up page.

    P_Input.send_keys(Password)

    Age_Month_DropDown = Instagram_Driver.find_element_by_name("")