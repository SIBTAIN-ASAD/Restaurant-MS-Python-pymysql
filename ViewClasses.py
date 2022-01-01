class Admin:
    def __init__(self,name,pwd,email):
        self.id = -1
        self.name = name
        self.pwd = pwd
        self.email = email

class Customer:
    def __init__(self,name,pwd,email):
        self.id = -1
        self.name = name
        self.pwd = pwd
        self.email = email

class Dish:
    def __init__(self,name, ingredients,price,category):
        self.id = -1
        self.name = name
        self.ingredients = ingredients
        self.price = price
        self.category = category
        self.quantity = 1

class Order:
    def __init__(self, cus_email, dish, quantity , price):
        self.id = -1
        self.cus_email = cus_email
        self.dish = dish
        self.quantity = quantity
        self.price = price
