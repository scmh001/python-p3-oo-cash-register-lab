#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.prev_transaction = []
    
  def add_item(self, item, price, quantity=1):
    self.items.extend([item] * quantity)
    self.total += price * quantity
    self.prev_transaction.append({"item": item, "price": price, "quantity": quantity})
    
  def apply_discount(self):
    if self.discount:
        self.total = int(self.total * ((100 - self.discount) / 100))
        print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")
      
  def void_last_transaction(self):
      if self.prev_transaction:
        last_transaction = self.prev_transaction.pop()
        self.total -= last_transaction['price'] * last_transaction['quantity']
        self.items = [item for item in self.items if item != last_transaction["item"]]


# for _ in range(last_transaction['quantity']):
#           self.items.remove(last_transaction['item'])

#  for i in range(quantity):
#       self.items.append(item)