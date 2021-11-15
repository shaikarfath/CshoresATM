# Welcome to our ATM Software :)
# Team: CShores
# LaNaya Goss, Daniel Kunigan, Kiranmai Machiraju, Hugh Page, Arfath Shaik

from ATM_CARD import ATM_Card
import User
import Admin
from Admin import Admin as ADMIN
from ATM_MACHINE import ATM_Machine
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/activate_card")
def activate_card():
    return render_template("activate_card.html")

@app.route("/add_atm")
def add_atm():
    return render_template("add_atm.html")

@app.route("/admin_login")
def admin_login():
    return render_template("admin_login.html")

@app.route("/atm_status")
def atm_status():
    return render_template("atm_status.html")

@app.route("/balance")
def balance():
    return render_template("balance.html")

@app.route("/block_card")
def block_card():
    return render_template("block_card.html")

@app.route("/card_no")
def card_no():
    return render_template("card_no.html")

# Reads UserAccounts.txt to put all account info into User.accounts
def readFile():
  txt_file = open("UserAccounts.txt", "r")
  file = txt_file.read()
  txt_file.close()
  if file[(len(file) - 1)] == "\n":
    file = file[:-1]
  file = file.split("\n")
  file[0] = file[0].split(",")
  address = file[0][0]
  status = file[0][1]
  last_refill = file[0][2]
  next_refill = file[0][3]
  min_bal = int(file[0][4])
  cur_bal = int(file[0][5])
  machine = ATM_Machine(address, status, last_refill, next_refill, min_bal, cur_bal)
  i = 1
  while(i < len(file)):
    file[i] = file[i].split(",")
    actNum = int(file[i][0])
    pin = int(file[i][1])
    username = file[i][2]
    today = file[i][3]
    nextYear = file[i][4]
    address = file[i][5]
    bal = int(file[i][6])
    phone = file[i][7]
    status = file[i][8]
    User.accounts.append(ATM_Card(actNum, pin, username, today, nextYear, address, bal, phone, status))
    i += 1
  return machine

# Starting menu
def parser(machine):
  Admin.accounts.append(ADMIN('Admin', 'abc123'))
  cont = True
  while(cont):
    print()
    print("1. Login as admin")
    print("2. Login as user")
    print("3. Exit Program")
    choice = input("- Please select one of the above actions: ")
    print()
    if(choice == "1"):
      if(Admin.login() != -1):
        cont_admin = True
        while(cont_admin):
          cont_admin = Admin.parser(machine)
    elif(choice == "2"):
      account = User.login()
      if(account != -1):
        card = User.accounts[account]
        cont_user = True
        while(cont_user):
          cont_user = User.parser(card, machine)
    elif(choice == "3" or choice == "0"):
      print("Exiting ATM Program")
      cont = False
    else:
      print("Input not recognized. A valid input is a number between 1 and 3")
  return

def main():
  machine = readFile()
  parser(machine)

if __name__ == "__main__":
  app.run(debug=True)
