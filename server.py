from socket import *
import json
import os

class Server:
    def __init__(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind(('192.168.1.XX', 9000))  
        self.clients = {}  # Stores user data: {id: {"password": "", "balance": 0, "history": []}}
        self.load_data()

    def load_data(self):
        if os.path.exists("clients.json"):
            with open("clients.json", "r") as file:
                self.clients = json.load(file)

    def save_data(self):
        with open("clients.json", "w") as file:
            json.dump(self.clients, file)

    def listen(self):
        self.socket.listen(5)
        client, _ = self.socket.accept()
        packet = client.recv(1024).decode().strip()

        if not packet:
            client.close()
            return

        try:
            command, data = packet.split('|', 1)
            if command == 'REGISTER':
                self.handle_register(client, data)
            elif command == 'LOGIN':
                self.handle_login(client, data)
            elif command == 'DEPOSIT':
                self.handle_deposit(client, data)
            elif command == 'WITHDRAW':
                self.handle_withdraw(client, data)
            elif command == 'TRANSFER':
                self.handle_transfer(client, data)
            elif command == 'BALANCE':
                self.handle_balance(client, data)
            elif command == 'HISTORY':
                self.handle_history(client, data)
        except Exception as e:
            print("Error:", str(e))

        self.save_data()
        client.close()

    def handle_register(self, client, data):
        id, password = data.split(',')
        if id in self.clients:
            client.sendall("ID_EXISTS".encode())
        else:
            self.clients[id] = {"password": password, "balance": 0, "history": []}
            client.sendall("REGISTER_SUCCESS".encode())

    def handle_login(self, client, data):
        id, password = data.split(',')
        if id in self.clients and self.clients[id]["password"] == password:
            client.sendall("LOGIN_SUCCESS".encode())
        else:
            client.sendall("LOGIN_FAIL".encode())

    def handle_deposit(self, client, data):
        id, amount = data.split(',')
        amount = int(amount)
        self.clients[id]["balance"] += amount
        self.clients[id]["history"].append(f"Deposited ${amount}")
        client.sendall("DEPOSIT_SUCCESS".encode())

    def handle_withdraw(self, client, data):
        id, amount = data.split(',')
        amount = int(amount)
        if amount <= self.clients[id]["balance"]:
            self.clients[id]["balance"] -= amount
            self.clients[id]["history"].append(f"Withdrew ${amount}")
            client.sendall("WITHDRAW_SUCCESS".encode())
        else:
            client.sendall("INSUFFICIENT_FUNDS".encode())

    def handle_transfer(self, client, data):
        id, recipient, amount = data.split(',')
        amount = int(amount)
        if recipient not in self.clients:
            client.sendall("INVALID_RECIPIENT".encode())
        elif amount > self.clients[id]["balance"]:
            client.sendall("INSUFFICIENT_FUNDS".encode())
        else:
            self.clients[id]["balance"] -= amount
            self.clients[recipient]["balance"] += amount
            self.clients[id]["history"].append(f"Transferred ${amount} to {recipient}")
            self.clients[recipient]["history"].append(f"Received ${amount} from {id}")
            client.sendall("TRANSFER_SUCCESS".encode())

    def handle_balance(self, client, data):
        id = data
        balance = self.clients[id]["balance"]
        client.sendall(str(balance).encode())

    def handle_history(self, client, data):
        id = data
        history = "\n".join(self.clients[id]["history"])
        client.sendall(history.encode())

if __name__ == "__main__":
    server = Server()
    while True:
        server.listen()
