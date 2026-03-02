# menu.py
menu = {
    "Coffee": 5.0,
    "Tea": 3.0,
    "Sandwich": 7.5,
    "Burger": 8.0,
    "Cake": 4.5
}
def display_menu():
    print("\n=== SmartCafe Menu ===")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")
    print("=====================")
