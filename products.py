

class Product:
     def __init__(self, name:str, price:float, quantity:int):
          """
          Creates the instance variables (active is set to True).
          If something is invalid (empty name / negative price or
          quantity), raises an exception.
          The 'active' attribute is boolean and reflects product
          availability. It is dynamically set during object
          instantiation.
          """

          # Error handling

          if not isinstance(name, str):
               raise TypeError("Name must be a string")
          if not name:
               raise ValueError("Name must contain characters")

          if not isinstance(price, (int, float)):
               raise TypeError("Price must be a number")
          if price < 0:
               raise ValueError("Price must be higher than 0")

          if not isinstance(quantity, int):
               raise TypeError("Quantity must be an integer")
          if quantity < 0:
               raise ValueError("Quantity must be 0 or higher")

          # Attributes

          self.name = name
          self.price = price
          self.quantity = quantity
          self.active:bool = quantity > 0


     def get_quantity(self):
          """
          Getter function for quantity.
          Returns the quantity.
          """
          return self.quantity


     def set_quantity(self, quantity):
          """
          Setter function for quantity.
          If quantity reaches 0, deactivates the product.
          Prints a message informing the user of the availability
          of the product.
          """
          try:
               self.quantity: int = quantity
               if self.quantity > 0:
                    self.activate()
               else:
                    self.deactivate()
          except:
               if not isinstance(quantity, int):
                    raise TypeError("Quantity must be an number")
               if quantity < 0:
                    raise ValueError("Quantity must be 0 or higher")
          finally:
               if self.active:
                    print(f"Product currently available, {self.quantity} units left.")
               else:
                    print("Product currently unavailable.")
                    print(self.quantity)


     def is_active(self) -> bool:
          """
          Getter function for active.
          Returns True if the product is active, otherwise False.
          """
          return self.active


     def activate(self):
          """
          Activates the product.
          """
          self.active: bool = True


     def deactivate(self):
          """
          Deactivates the product.
          """
          self.active: bool = False


     def show(self) -> str:
          """
          Returns a string that represents the product, for example:
          "MacBook Air M2, Price: 1450, Quantity: 100"
          """
          return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Promotion: "


     def buy(self, quantity):
          """
          Buys a given quantity of the product.
          Raises an Exception for incorrect inputs.
          Updates the quantity of the product.
          If quantity reaches 0, deactivates product.
          Returns the total price (float) of the purchase.
          """
          try:
               if not isinstance(quantity, (int, float)):
                    raise TypeError("Quantity must be a number")
               if quantity <= 0:
                    raise ValueError('Please introduce at least one unit to buy')
               if quantity > self.quantity:
                    raise ValueError("Quantity requested higher than quantity available")

               if isinstance(self.quantity, str):
                    return quantity * self.price
               elif self.quantity >= quantity:
                    total_price = quantity * self.price
                    self.quantity -= quantity
               else:
                    raise ValueError(f"Not enough {self.name} units in store.")

               if self.quantity == 0:
                    self.deactivate()
                    print(f"\n{self.name} no longer available")

          except Exception as e:
               print("Error: ", e)
               return quantity * self.price

          return total_price

#######

class NonStockedProduct(Product):
     """
     This subclass represents a Product without
     a numerical quantity attribute.
     """
     def __init__(self, name:str, price:float):
          super().__init__(name, price, 0)
          self.quantity = "Unlimited"
          self.active:bool = True


#######

class LimitedProduct(Product):
     """
     This subclass represents a Product with
     limited quantity, maximum
     """
     def __init__(self, name:str, price:float, quantity:int, maximum:int):
          super().__init__(name, price, quantity)
          self.maximum = maximum

     def show(self) -> str:
          """
          Returns a string that represents the product,
          for example:
          "MacBook Air M2, Price: 1450, Quantity: 100, Maximum: 1"
          """
          super().show()
          return (f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
                  f", Maximum: {self.maximum}, Promotion: ")