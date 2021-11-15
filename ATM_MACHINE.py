# This is the ATM Machine class

from datetime import datetime, timedelta

class ATM_Machine :

  def __init__(self, address, status, last_refill, next_refill, min_bal, cur_bal):
    self.address = address
    self.status = status
    self.last_refill = last_refill
    self.next_refill = next_refill
    self.min_bal = min_bal
    self.cur_bal = cur_bal

  def __str__(self):
    string = ""
    string += "Address: " + self.address
    string += ", Status: " + self.status
    string += ", Last Refill Date: " + self.last_refill
    string += ", Next Refill Date: " + self.next_refill
    string += ", Minimum Balance Enquiry: $" + self.min_bal
    string += ", Current Balance: $" + self.cur_bal
    return string
  
  def refill(self, amount):
    self.cur_bal += amount
    refillDate = datetime.now().date()
    month = timedelta(30)
    self.last_refill = str(refillDate)
    self.next_refill = str(refillDate + month)
    