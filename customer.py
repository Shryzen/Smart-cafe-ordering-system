# customer.py - Client side
from menu import menu, display_menu
import socket
import json

def place_order():
    display_menu()
    order = {}
    while True:
        item = input("Enter item name (or 'done' to finish): ").strip().title()
        if item.lower() == 'done':
            break
        if item not in menu:
            print("Item not in menu. Please try again.")
            continue
        try:
            quantity = int(input(f"How many {item}s? "))
            order[item] = quantity
        except ValueError:
            print("Please enter a valid number.")
    return order if order else None

def send_order(order):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 65432))
        s.sendall(json.dumps(order).encode())
        print("Order sent to kitchen!")

if __name__ == "__main__":
    print("Welcome to SmartCafe!")
    customer_order = place_order()
    if customer_order:
        send_order(customer_order)
