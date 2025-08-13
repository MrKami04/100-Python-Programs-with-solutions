# Restaurant Project

menu = {              # Menu data: item with price
    "Burger": 350,"Pizza": 800,"Pasta": 500,"Fries": 200,"Coffee": 150
}

discounts = {                # Discounts: name with percentage
    "Student": 10, "Senior Citizen": 15, "Weekend Special": 5
}
order_history = []  # Order history list

def welcome():     # Function to display welcome message
   print("------❤ Welcome to Pasta La Vista, Baby! ❤------")
   print("We are happy to serve you!\n")
   
def call_waiter():    # Function to call waiter
    choice = input("Type 'call' to call the waiter: ").strip().lower()
    if choice == "call":
        print("Waiter is on the way!\n")

def display_menu():    # Function to display menu
    print("----- Menu -----")
    for item, price in menu.items():
        print(f"{item}: Rs {price}")
    print()

def take_order():    # Function to take order from customer
    order_list = []
    while True:
        item = input("Enter item name to order (or 'done' to finish): ").title()
        if item == "Done":
            break
        elif item in menu:
            order_list.append(item)
            print(f"{item} added to order.\n")
        else:
            print("Item not found. Please choose from the menu.\n")
    return order_list

def calculate_bill(order_list):    # Function to calculate bill
    return sum(menu[item] for item in order_list)

def apply_discount(bill):    # Function to apply discount
    print("\nAvailable Discounts:")
    for d, p in discounts.items():
        print(f"{d}: {p}% off")
    choice = input("Enter discount name (or press Enter for none): ").title()
    if choice in discounts:
        bill -= bill * (discounts[choice] / 100)
    return bill

def give_tip():          # Function for tip
    try:
        tip = float(input("Enter tip amount for waiter: Rs "))
        return tip
    except ValueError:
        print("Invalid amount. No tip added.")
        return 0

def payment_method():    # Function for payment method
    methods = ["Cash", "Card", "Online"]
    print("\nPayment Methods:", ", ".join(methods))
    choice = input("Choose payment method: ").title()
    if choice in methods:
        print(f"Payment will be processed via {choice}.")
    else:
        print("Invalid choice. Defaulting to Cash.")

def save_order(name, order_list, total_amount):    # Function to store order in history
    order_data = {
        "Customer Name": name,
        "Items": order_list,
        "Total Paid": total_amount
    }
    order_history.append(order_data)


def get_feedback():    # Function to collect customer feedback
    feedback = input("\nPlease share your feedback: ")
    print("Thank you for your feedback!")

# Function to display order history (for admin use)
def show_order_history():
    print("\n--- Order History ---")
    for idx, order in enumerate(order_history, start=1):
        print(f"Order {idx}: {order['Customer Name']} - Items: {order['Items']} - Paid: Rs {order['Total Paid']}")

# Main program
def restaurant_system():
    welcome()
    name = input("Enter your name: ")
    call_waiter()
    display_menu()
    order_list = take_order()

    if not order_list:
        print("No items ordered. Goodbye!")
        return

    bill = calculate_bill(order_list)
    print(f"\nYour total before discount: Rs {bill}")

    bill = apply_discount(bill)
    print(f"Bill after discount: Rs {bill}")

    tip = give_tip()
    total_payable = bill + tip
    print(f"\nFinal Amount (including tip): Rs {total_payable}")

    payment_method()
    save_order(name, order_list, total_payable)
    get_feedback()

    print("\nThank you for visiting Pasta La Vista, Baby! Have a great day!")

# Run the system
restaurant_system()

# (Optional) View history for testing
# show_order_history()
