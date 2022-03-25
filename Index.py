#Imports.

import os
import sys
import uuid
import json

from colorama import Fore

#Store the function to be used within the console:

class DatabaseCount():

    #Set global variables:

    global Database_Count

    for n in range(len):

        with open("JsonDataBase\\Target.json" , "r") as f:

            Database_Count = json.loads(f)

class Functions():

    #Set global functions:

    global Overseer_Help

    global Overseer_Start

    global Overseer_Exit

    def Overseer_Help():

        print("To use the console, simply type 'start' or to exit, type 'exit'")

    def Overseer_Start():

        print(Fore.MAGENTA + "Starting Overseer now...")

        Target_Username = input("Please input a new target using a name or alias.") #Get the name or alias of a new target.

        Target_UUID = uuid.uuid4()

        #Set the target payload number + tag:

        TargetPayloadName = "TargetPayload" + len(Database_Count) + 1

        TargetPayloadName = { #Create the payload for the foundation JSON target database.
            "Username : " : Target_Username(),
            "Target ID : " : Target_UUID()
        }
        
        with open("JsonDataBase\\Target.json" , "w") as f:

            json.dumps(TargetPayloadName , f)

    def Overseer_Exit():

        print(Fore.MAGENTA + "Exiting Overseer now...")

        sys.exit

    #List of the functions inside of the function dictionary.

    global Function_Dictionary

    Function_Dictionary = {"help" : Overseer_Help , "start" : Overseer_Start , "exit" : Overseer_Exit} #Creates new function aliases for easier access to the functions for the user to use in the console.

#Open console:

class Console():

    #Set global variables:

    global Command_Ran

    os.system("cls") #Clear the current text within the console.

    os.system("title Overseer.") #Change the default title for CMD to "Overseer.".

    #Print out the menu for the console:

    while True:

        Command_Ran = input("Please input a command to run <use the 'help' command to show a list of features'> : ").lower()

        if Command_Ran in Function_Dictionary == False: #Check the dictionary for a valid function to run.

            print(Fore.RED + "Please re-input a correct command, use <help> to look at available commands.") #Error message if invalid input.

            continue

        else:

            break

class Run():

    if Command_Ran == "help":

        Overseer_Help()

    elif Command_Ran == "start":

        Overseer_Start()

    elif Command_Ran == "exit":

        Overseer_Exit()