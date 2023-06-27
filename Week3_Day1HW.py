
## Exercise 1 - Turn the shopping cart program from yesterday into an object-oriented program

# The comments in the cell below are there as a guide for thinking about the problem. However, 
# if you feel a different way is best for you and your own thought process, please do what feels best for you by all means.

# Create a class called cart that retains items and has methods to add, remove, and show

# class Cart():
#     pass
class Cart:
    def __init__(self):
        self.cart = {}

    def add_item(self):
        item = input("Enter the item: ")
        quantity = input("Enter the quantity: ")
        self.cart[item] = quantity
        print(f"Added {quantity} {item} to the cart.")

    def delete_item(self):
        item = input("Enter the item to delete: ")
        if item in self.cart:
            del self.cart[item]
            print(f"{item} removed from the cart.")
        else:
            print(f"{item} is not in the cart.")

    def show_cart(self):
        print("Shopping cart list:")
        for item, quantity in self.cart.items():
            print(f"{item}: {quantity}")

    def shopping_cart(self):
        while True:
            print("1. Shopping Cart menu")
            print("2. Add item")
            print("3. Delete item")
            print("4. Quit")

            choice = input("Enter your choice (1-4): ")

            if choice == "2":
                self.add_item()

            elif choice == "3":
                self.delete_item()

            elif choice == "1":
                self.show_cart()

            elif choice == "4":
                print("Printing all items in the shopping cart:")
                for item, quantity in self.cart.items():
                    print(f"{item}: {quantity}")
                break

            else:
                print("Invalid option")


# Create an instance here
shopping_cart = Cart()
shopping_cart.shopping_cart()
  

### Exercise 2 - Write a Python class which has two methods get_String and print_String. 
# get_String accept a string from the user and print_String print the string in upper case

class StringManipulator:
    def __init__(self):
        self.string = ""

    def get_String(self):
        self.string = input("Enter a string: ")

    def print_String(self):
        print("String in uppercase:", self.string.upper())


# instance here
manipulator = StringManipulator()

# Call the get_String method here
manipulator.get_String()


manipulator.print_String()
