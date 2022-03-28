#Imports.

import string
import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select as WebSelect
from webdriver_manager.chrome import ChromeDriverManager

class AccountCreation():

    #Set the global variables:

    global First_Name

    global Last_Name

    global Username

    global Password

    global Confirm

    global Gmail

    #Create the Gmails Username:

    Username = "".join(random.choices(string.ascii_letters + string.digits , k = 10))

    #Create the Gmail s Password:

    Password = "".join(random.choices(string.ascii_letters + string.digits , k = 10))

    #Confirm the Gmails password:

    Confirm = Password()

    #Create the Gmail variable:

    Gmail = f"{Username}@protonmail.com"

class AccountCreationDataInput():

    #Define the Driver for the account creation:

    Gmail_Driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    #Define the Gmail account creation site URL:

    Gmail_Driver.get("https://protonmail.com/signup")

    #Search for the Gmail account creation input boxes:

    Free_Plan_Dropdown = Gmail_Driver.find_element_by_id("plan-free")

    WebSelect(Free_Plan_Dropdown) #Press the drop down of the free plan selection.

    Gmail_Driver.find_element_by_id("freePlan").click() #Press the free plan button to confirm the plan.

    Gmail_Driver.find_element_by_xpath('//a[@href="https://account.protonmail.com/signup"]') #Have Selenium press the "Create an account" href link.

    U_Input = Gmail_Driver.find_element_by_id("username") #Input the username.

    U_Input.send_keys(Username)

    P_Input = Gmail_Driver.find_element_by_id("password") #Input the password.

    P_Input.send_keys(Password)

    C_Input = Gmail_Driver.find_element_by_id("repeat-password") #Input the confirmation password.

    C_Input.send_keys(Confirm)

    Gmail_Driver.find_element_by_class_name("button button-large button-solid-norm w100 mt1-75").click() #Press "Next" button

    Gmail_Driver.find_element_by_class_name("button button-large button-ghost-norm w100 mt0-5").click() #Press button to skip recovery information.

    Gmail_Driver.find_element_by_class_name("button button-solid-norm w100").click() #Press Confirm no recovery option.

    Gmail_Driver.find_element_by_class_name("button button-solid-norm w100").click() #Select plan.

    Gmail_Driver.find_element_by_id("checkbox").click() #Bypass captcha.