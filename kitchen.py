# kitchen.py - Server side
from menu import menu  # Importing the shared menu
import socket
import json
import time

def process_order(order_data):
    print("\nReceived order:")
    total = 0.0
    for item, quantity in order_data.items():
        price = menu[item] * quantity  # Using the imported menu
        print(f"{quantity}x {item} (${menu[item]:.2f} each)")
        total += price
    print(f"TOTAL: ${total:.2f}")
    time.sleep(2)  # Simulate processing time
    print("Order ready!")

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 65432))
        s.listen()
        print("Kitchen server ready...")
        while True:
            conn, addr = s.accept()
            with conn:
                data = conn.recv(1024)
                order = json.loads(data.decode())
                process_order(order)
                conn.sendall(b"Order received")

if __name__ == "__main__":
    start_server()
