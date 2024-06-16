class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity=1):
        if item in self.items:
            if self.items[item] <= quantity:
                del self.items[item]
            else:
                self.items[item] -= quantity

    def get_total(self):
        return sum(item.price * quantity for item, quantity in self.items.items())

    def display_order(self):
        print("Your order:")
        for item, quantity in self.items.items():
            print(f"- {item.name} x{quantity}: Rs {item.price * quantity:.2f}")
        print(f"Total: Rs {self.get_total():.2f}")

def display_menu(menu):
    print("\nMenu:")
    for index, item in enumerate(menu, start=1):
        print(f"{index}. {item.name} - Rs {item.price:.2f}")

def main():
    menu = [
        MenuItem("Burger",200),
        MenuItem("Fries", 150),
        MenuItem("Soda", 100),
        MenuItem("Salad", 120),
        MenuItem("Pizza", 350)
    ]

    order = Order()

    while True:
        display_menu(menu)
        print("\nOptions:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View order")
        print("4. Quit")


        choice = input("Enter your choice: ")

        if choice == '1':
            item_choice = input("Enter the item number to add to your order: ")
            try:
                item_index = int(item_choice) - 1
                if 0 <= item_index < len(menu):
                    quantity = int(input("Enter the quantity: "))
                    if quantity > 0:
                        order.add_item(menu[item_index], quantity)
                        print(f"Added {quantity} x {menu[item_index].name} to your order.")
                    else:
                        print("Quantity must be positive.")
                else:
                    print("Invalid item number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '2':
            item_choice = input("Enter the item number to remove from your order: ")
            try:
                item_index = int(item_choice) - 1
                if 0 <= item_index < len(menu):
                    quantity = int(input("Enter the quantity to remove: "))
                    if quantity > 0:
                        order.remove_item(menu[item_index], quantity)
                        print(f"Removed {quantity} x {menu[item_index].name} from your order.")
                    else:
                        print("Quantity must be positive.")
                else:
                    print("Invalid item number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '3':
            order.display_order()

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")

    print("\nFinal order:")
    order.display_order()
    print("Thank you for ordering!")

if __name__ == "__main__":
    main()