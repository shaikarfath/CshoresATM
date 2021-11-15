# Admin Module
# from django.shortucts import render
from datetime import datetime, timedelta
import random
import ATM_CARD
from ATM_CARD import ATM_Card
from ATM_MACHINE import ATM_Machine
import User

accounts = []


class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password


def addAdmin():
    username = input("- Enter your username: ")
    password = input("- Enter your password: ")
    accounts.append(Admin(username, password))
    print("New admin account added")
    # return render("admin_login.html")


# Searches Admin.accounts for a given username
def findAccount(acct):
    i = 0
    while i < len(accounts):
        if acct == accounts[i].username:
            return i
        i += 1
    return -1


# Checks username and password for admin login
def login():
    account = -1
    while account == -1:
        account = findAccount(input("- Enter your username: "))
        if account == "0":
            print("Quit Login")
            return -1
        if account == -1:
            print("There is no account with this username, please try again or enter '0' to quit")
    while (True):
        password = input("- Enter your password: ")
        if (password == "0"):
            print("Quit Login")
            return -1
        if (password == accounts[account].password):
            print("Login successful. Welcome " + accounts[account].username)
            return account
        print("Login failed. Please try again or enter '0' to quit")


# Adds new user account
def addCard():
    check = 0
    while (check != -1):
        username = input("- Enter the account name: ")
        check = User.findAccount(username)
        if (username == "0"):
            print("Quit Create New Account")
            return
        if (check != -1):
            print("An account with this username already exists, please enter a different username or '0' to quit")
    check = -1
    pin = ATM_CARD.enterPIN("- Enter a 4-digit pin number: ")
    address = input("- Enter your address: ")
    phone = input("- Enter your phone number: ")
    check = 0
    while (check != -1):
        actNum = random.randint(0, 999999999)
        check = User.findAccount(actNum)
    today = datetime.now().date()
    year = timedelta(365)
    nextYear = datetime.now().date() + year
    bal = 0
    status = 'activated'
    User.accounts.append(ATM_Card(actNum, pin, username, today, nextYear, address, bal, phone, status))
    print("New user account added with account number: " + str(actNum))
    return


# Displays info about the ATM
def viewMachineStatus(machine):
    print("Address: " + machine.address)
    print("ATM Status: " + machine.status)
    print("Minimum balance enquiry: $" + str(machine.min_bal))
    print("Available funds: $" + str(machine.cur_bal))
    print("Previous refill date: " + machine.last_refill)
    print("Next scheduled refill date: " + machine.next_refill)
    return


# Allows admin to change user account info
def updateATMCard(card):
    cont = True
    while (cont):
        print()
        print("1. Lock ATM Card")
        print("2. Activate ATM Card")
        print("3. Reset PIN")
        print("4. Reset Phone Number")
        print("5. Update Expiry Date")
        print("6. Exit")
        choice = input("- Please select one of the above actions: ")
        print()
        if (choice == "1"):
            card.lockCard()
        elif (choice == "2"):
            card.activateCard()
        elif (choice == "3"):
            card.resetPIN()
        elif (choice == "4"):
            card.resetPhone()
        elif (choice == "5"):
            card.updateExpiryDate()
        elif (choice == "6" or choice == "0"):
            print("Quit Update User Account")
            cont = False
        else:
            print("Input not recognized. A valid input is a number between 1 and 6")
    return


# Main admin menu
def parser(machine):
    print()
    print("1. Update User Account")
    print("2. Add New User Account")
    print("3. Check ATM Status")
    print("4. Logout")
    choice = input("- Please select one of the above actions: ")
    print()
    if (choice == "1"):
        account = -1
        while (account == -1):
            answer = input("- Enter the account name or number: ")
            account = User.findAccount(answer)
            if (answer == "0"):
                print("Quit Update User Account")
                return True
            elif (account == -1):
                print("There is no account with this username or number, please try again or enter '0' to quit")
            else:
                card = User.accounts[account]
                print("Updating account: " + User.accounts[account].acct_name)
                updateATMCard(card)
                return True
    elif (choice == "2"):
        addCard()
        return True
    elif (choice == "3"):
        viewMachineStatus(machine)
        return True
    elif (choice == "4" or choice == "0"):
        User.writeFile(machine)
        print("Logged out")
        return False
    else:
        print("Input not recognized. A valid input is a number between 1 and 4")
        return True
