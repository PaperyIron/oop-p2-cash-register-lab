#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.previous_transactions = []

  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self, value):
    if not isinstance(value, int) or value < 0 or value > 100:
      print('Not valid discount')
    else:
      self._discount = value
  
  def add_item(self, item, price, quantity = 1):
    self.total += price * quantity
    for _ in range(quantity):
      self.items.append(item)
    transaction = {
      'item': item,
      'price': price,
      'quantity': quantity
    }
    self.previous_transactions.append(transaction)

  def apply_discount(self):
    if self._discount > 0:
      discount_amount = self.total * (self._discount / 100)
      self.total -= discount_amount
      print(f'After the discount, the total comes to ${self.total:g}.')
    else:
      print('There is no discount to apply.')

  def void_last_transaction(self):
        if len(self.previous_transactions) == 0:
            return
        
        last_transaction = self.previous_transactions.pop()
        
        transaction_total = last_transaction['price'] * last_transaction['quantity']
        self.total -= transaction_total
        
        item_name = last_transaction['item']
        quantity = last_transaction['quantity']
        
        for _ in range(quantity):
            if item_name in self.items:
                self.items.remove(item_name)
    
    
    
    


