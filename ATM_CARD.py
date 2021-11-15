# This is the ATM Card class file

from datetime import datetime, timedelta
import random

# Makes certain inputted PIN is a 4-digit number
def enterPIN(message):
  cont = True
  pin = input(message)
  while(cont):
    if(len(pin) == 4):
      try:
        intPin = int(pin)
        cont = False
      except:
        print("PIN can contain only numbers")
        pin = input(message)
        cont = True
    else:
      print("PIN must contain exactly 4 digits")
      pin = input(message)
      cont = True
  return intPin

# Makes certain an input is an integer
def enterInt(message):
  cont = True
  num = input(message)
  while(cont):
    try:
      intNum = int(num)
      cont = False
    except:
      print("Input must be a number")
      num = input(message)
      cont = True
  return intNum

class ATM_Card :

  def __init__(self, acct_num, pin, acct_name, issue_date, expiry_date, address, bal, phone_num, status):
    self.acct_num = acct_num
    self.pin = pin
    self.acct_name = acct_name
    self.issue_date = issue_date
    self.expiry_date = expiry_date
    self.address = address
    self.bal = bal
    self.phone_num = phone_num
    self.status = status

  def __str__(self):
    string =''
    string += 'Account number: ' + self.acct_num
    string += ', PIN: ' + self.pin
    string += ', Account name: ' + self.acct_name
    string += ', Issue Date: ' + self.issue_date
    string += ', Expiry Date: ' + self.expiry_date
    string += ', Balance: $' + str(self.bal)
    string += ', Phone Number: ' + self.phone_num
    string += ', Status : ' + self.status
    
    return string

  def lockCard(self):
    self.status = "locked"
    print("Card successfully locked.")
    return
  
  def activateCard(self):
    self.status = "activated"
    print("Card successfully activated")
    return

  def resetPIN(self):
    new_PIN = enterPIN("- Please enter a new 4-digit pin: ")
    self.pin = new_PIN
    print("PIN successfully changed to " + str(self.pin))
    return

  def resetPhone(self):
    new_phone = input("- Please enter the new phone number: ")
    self.phone_num = new_phone
    print("Phone number successfully changed to " + self.phone_num)
    return
  
  def phonePasscode(self):
    passcode = str(random.randint(100000,999999))
    print("Passcode: " + passcode)
    answer = input("- Please enter the passcode you were sent: ")
    cont = True
    while(cont):
      if(answer == passcode):
        print("Correct passcode")
        cont = False
      else:
        print("Incorrect passcode")
        print("1. Try again")
        print("2. Send new passcode")
        print("3. Quit")
        answer = input("- Please select one of the above actions: ")
        if(answer == "1"):
          answer = input("- Please enter the passcode you were sent: ")
        elif(answer == "2"):
          passcode = str(random.randint(100000,999999))
          print("Passcode: " + passcode)
          answer = input("- Please enter the passcode you were sent: ")
        elif(answer == "3" or answer == "0"):
          print("Quit Change Phone Number")
          return
        else:
          print("Input not recognized. A valid input is a number between 1 and 3")
    self.resetPhone()
    return

  def updateExpiryDate(self):
    year = timedelta(365)
    nextYear = datetime.now().date() + year
    self.expiry_date = str(nextYear)
    print("Expiry date successfully changed to " + self.expiry_date)
    return