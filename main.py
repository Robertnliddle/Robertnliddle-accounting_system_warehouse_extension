import json


class Manager:
    def __int__(self, warehouse):
        self.warehouse = warehouse
        self.tasks = {}

    def assign(self, task, method):
        self.tasks[task] = method

        def wrapper(func):
            self.tasks[product_name] = func
        return wrapper

    def execute(self, task, method, *args, **kwargs):
        if task in self.tasks:
            method = self.tasks[task]
        return method(*args, **kwargs)

    def purchase_decorator(self, function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result
        return wrapper

    def balance_decorator(self, function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result
        return wrapper

    def sale_decorator(self, function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result
        return wrapper

    def review(self, function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result
        return wrapper


balance = 0
warehouse = {}
history = []

commands_list_msg = """Select a command: 
- balance: add or subtract from the account
- sale: name of product, quantity and update the warehouse accordingly
- purchase: name of the product, its price, quantity and update to warehouse and account
- account: display the current account balance
- warehouse_list: display the total inventory in the warehouse along with products prices and quantities
- warehouse: display a product and its status in the warehouse
- review: Review the history
- end: exit the program"""

commands_add_sub_msg = """Select if you want to add or subtract to the balance
- add 
- subtract"""

while True:
    print(commands_list_msg)
    action = input("Select a command: ")
    print("Selected command: ", action)
    if action == "end":
        print("Exiting the program...")
        break

    elif action == "balance":
        print(commands_add_sub_msg)
        action = input("Select a command: ")
        if action == "add":
            amount = int(input("Enter the amount to add to the balance: "))
            balance += amount
            print("The amount have been added to the balance")
            history.append(balance)
        elif action == "subtract":
            sub = int(input("Enter the amount to subtract: "))
            balance -= sub
            if balance < 0:
                print("The action is not possible")
                balance += sub
            elif sub <= 0:
                print("The action is not possible")
            else:
                print("The amount have been subtracted to the balance")
                history.append(balance)

    elif action == "sale":
        product_name = input("Enter the products name: ")
        price = int(input("Enter the price: "))
        quantity = int(input("Enter the quantity sold: "))
        if product_name in warehouse:
            if quantity <= warehouse[product_name]:
                total_price = price * quantity
                balance += total_price
                warehouse[product_name] -= quantity
                print(f"Products sold:{product_name},Quantity:{quantity}")
                history.append(product_name)
        else:
            print("Product not found in the warehouse or the quantity is not enough")

    elif action == "purchase":
        product_name = input("Enter the name of the product: ")
        price = int(input("Enter the price: "))
        quantity = int(input("Enter the quantity: "))
        total_price = price * quantity
        if total_price > balance:
            print("You have to low balance in your account")
            continue
        balance -= total_price
        print(f"You purchase {product_name}{quantity} items for {total_price}")
        if product_name not in warehouse:
            warehouse[product_name] = 0
        warehouse[product_name] += quantity
        history.append(product_name)

    elif action == "account":
        print(f"Current account balance is: {balance} ")

    elif action == "warehouse_list":
        for product_name, quantity in warehouse.items():
            print(f"{product_name}: {quantity}")

    elif action == "warehouse":
        product_name = input("Enter the products name: ")
        if product_name in warehouse:
            print(f"{product_name} is available at the warehouse: {warehouse[product_name]}")
        else:
            print(f"The product name you are looking for are not in the warehouse")

    elif action == "review":
        first_index = int(input("Enter the first index: "))
        second_index = int(input("Enter the second index: "))
        for entry in history[first_index:second_index]:
            print(entry)
    else:
        print(f"The command are not supported {action}. Please select another command.")
