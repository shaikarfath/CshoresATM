# User Module

import ATM_CARD
from ATM_CARD import ATM_Card
from ATM_MACHINE import ATM_Machine

accounts = []

# Finds user account given either the account name or account number
def findAccount(acct):
  i = 0
  while(i < len(accounts)):
    if(acct == accounts[i].acct_name  or acct == str(accounts[i].acct_num)):
      return i
    i += 1
  return -1

# Checks account name/number and pin for user login
def login():
  account = -1
  while(account == -1):
    account = findAccount(input("- Enter your account name or number: "))
    if(account == "0"):
      print("Quit Login")
      return -1
    if(account == -1):
      print("There is no account with this username or number, please try again or enter '0' to quit")
    elif(accounts[account].status == 'locked'):
      print("This account is locked, see admin to have it unlocked")
      return -1
  attempts = 0
  while(attempts < 3):
    pin = ATM_CARD.enterPIN("- Enter your pin number: ")
    if(pin == "0"):
      print("Quit Login")
      return -1
    if(pin == accounts[account].pin):
      print("Login successful. Welcome " + accounts[account].acct_name)
      return account
    if(attempts < 2):
      print("Login failed. Please try again or enter '0' to quit. 3 failed login attempts will result in account being locked")
    attempts += 1
  print("Too many failed attempts, this account has been locked")
  accounts[account].status = 'locked'
  return -1

# Transfers money from user's account to another
def transfer(card):
  account = -1
  while(account == -1):
    username = input("- Enter the beneficiary's account name or number: ")
    if(username == "0"):
      print("Quit Transfer")
      return
    account = findAccount(username)
    if(account == -1):
      print("There is no account with this username or number, please try again or enter '0' to quit")
  card2 = accounts[account]
  amount = card.bal + 1
  while(amount > card.bal):
    amount = ATM_CARD.enterInt("- Enter the amount you would like to transfer: $")
    if(amount == 0):
      print("Quit transfer")
      return
    if(amount > card.bal):
      print("Insufficient funds, you have $" + str(card.bal) + " in your account. Please enter another amount or '0' to quit")
  card.bal -= amount
  card2.bal += amount
  print("Transfer Successful.")
  return

# Takes money out of the ATM and user's account
def withdraw(card, machine):
  amount = machine.cur_bal + 1
  while(amount > card.bal or amount > machine.cur_bal or amount < machine.min_bal):
    amount = ATM_CARD.enterInt("- Enter the amount you would like to withdraw: $")
    if(amount == 0):
      print("Quit Withdraw")
      return
    elif(amount < machine.min_bal):
      print("Minimum transaction is $" + str(machine.min_bal) + ". Please enter another amount or '0' to quit")
    elif(amount > card.bal):
      print("Insufficient funds, you have $" + str(card.bal) + " in your account")
      print("Please enter another amount or '0' to quit")
    elif(amount > machine.cur_bal):
      print("Insufficient funds, the ATM has only $" + str(machine.cur_bal) + " available to be withdrawn")
      print("Please enter another amount or '0' to quit")
  card.bal -= amount
  machine.cur_bal -= amount
  print("Withdraw Successful")
  print("Remaining Balance: $" + str(card.bal))
  return

# Puts money into the ATM and user's account
def deposit(card, machine):
  amount = ATM_CARD.enterInt("- Enter the amount you would like to deposit: $")
  card.bal += amount
  machine.cur_bal += amount
  print("Deposit Successful")
  print("Balance: $" + str(card.bal))
  return

def balanceEnquiry(card):
  print("Your balance is: $" + str(card.bal))

# Writes account info from User.accounts into UserAccounts.txt
def writeFile(machine):
  with open("UserAccounts.txt", "w") as txt_file:
    txt_file.write(machine.address + "," + machine.status + "," + machine.last_refill + "," + machine.next_refill + "," + str(machine.min_bal) + "," + str(machine.cur_bal) + "\n")    
    i = 0
    while(i < len(accounts)):
      txt_file.write(str(accounts[i].acct_num) + "," + str(accounts[i].pin) + "," + accounts[i].acct_name + "," + str(accounts[i].issue_date)+ "," + str(accounts[i].expiry_date) + "," + str(accounts[i].address) + "," + str(accounts[i].bal) + "," + str(accounts[i].phone_num) + "," + str(accounts[i].status) + "\n")
      i += 1
    txt_file.close()
    
    #issue_date, expiry_date, address, bal, phone_num, status
    #for line in accounts:
      #txt_file.write(" ".join(line) + " ")
  
  
# User menu
def parser(card, machine):
  print()
  balanceEnquiry(card)
  print("1. Withdraw")
  print("2. Deposit")
  print("3. Transfer")
  print("4. Change PIN")
  print("5. Change Phone Number")
  print("6. Logout")
  choice = input("- Please select one of the above actions: ")
  print()
  if(choice == "1"):
    withdraw(card, machine)
    return True
  elif(choice == "2"):
    deposit(card, machine)
    return True
  elif(choice == "3"):
    transfer(card)
    return True
  elif(choice == "4"):
    card.resetPIN()
    return True
  elif(choice == "5"):
    card.phonePasscode()
    return True
  elif(choice == "6" or choice == "0"):
    writeFile(machine)
    print(card.acct_name + " logged out")
    return False
  else:
    print("Input not recognized. A valid input is a number between 1 and 6")
    return True

  
  
