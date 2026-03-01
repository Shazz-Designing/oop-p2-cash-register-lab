#!/usr/bin/env python3

class CashRegister:
    """
    CashRegister simulates a simple e-commerce cash register.
    It tracks items added, total cost, discounts, and allows voiding
    the last transaction.
    """

    def __init__(self, discount=0):
        # Discount percentage to apply (e.g., 20 for 20%)
        self.discount = discount
        
        # Running total of all items
        self.total = 0
        
        # List storing all items added (including duplicates)
        self.items = []
        
        # Tracks the amount from the most recent transaction
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        """
        Adds an item to the register.
        Supports optional quantity.
        Updates total and stores last transaction amount.
        """
        for _ in range(quantity):
            self.items.append(title)

        amount = price * quantity
        self.total += amount
        self.last_transaction_amount = amount

    def apply_discount(self):
        """
        Applies discount to the total if discount > 0.
        Prints the appropriate message.
        """
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        """
        Removes the last transaction amount from the total.
        """
        self.total -= self.last_transaction_amount