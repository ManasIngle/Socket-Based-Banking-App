from socket import *
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog


class BankingGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Banking Application")
        self.root.geometry("400x600")
        self.root.configure(bg='#e0f7fa')
        self.client = None
        self.setup_login_screen()

    def setup_login_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        login_frame = tk.Frame(self.root, bg='#80deea')
        login_frame.pack(pady=50)

        tk.Label(login_frame, text="Banking System Login", font=('Arial', 20, 'bold'), bg='#80deea').pack(pady=10)
        tk.Label(login_frame, text="Enter your ID:", bg='#80deea').pack(pady=5)
        self.id_entry = tk.Entry(login_frame)
        self.id_entry.pack(pady=5)

        tk.Label(login_frame, text="Enter your Password:", bg='#80deea').pack(pady=5)
        self.password_entry = tk.Entry(login_frame, show='*')
        self.password_entry.pack(pady=5)

        tk.Button(login_frame, text="Login", command=self.login, bg='#00796b', fg='white').pack(pady=10)
        tk.Button(login_frame, text="Register", command=self.register, bg='#00796b', fg='white').pack(pady=10)

    def login(self):
        id_num = self.id_entry.get()
        password = self.password_entry.get()
        self.client = Client()
        self.client.connect()
        msg = f"LOGIN|{id_num},{password}"
        self.client.socket.send(msg.encode())
        response = self.client.socket.recv(1024).decode()
        self.client.socket.close()

        if response == "LOGIN_SUCCESS":
            self.client.id = id_num
            self.setup_main_screen()
        else:
            messagebox.showerror("Error", "Invalid ID or Password")

    def register(self):
        id_num = self.id_entry.get()
        password = self.password_entry.get()
        self.client = Client()
        self.client.connect()
        msg = f"REGISTER|{id_num},{password}"
        self.client.socket.send(msg.encode())
        response = self.client.socket.recv(1024).decode()
        self.client.socket.close()

        if response == "REGISTER_SUCCESS":
            messagebox.showinfo("Success", "Registration successful!")
        else:
            messagebox.showerror("Error", "ID already exists")

    def setup_main_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        main_frame = tk.Frame(self.root, bg='#b2ebf2')
        main_frame.pack(pady=20)

        tk.Label(main_frame, text=f"Welcome, {self.client.id}", font=('Arial', 20, 'bold'), bg='#b2ebf2').pack(pady=10)

        tk.Button(main_frame, text="Check Balance", command=self.check_balance, bg='#00796b', fg='white', width=20).pack(pady=5)
        tk.Button(main_frame, text="Deposit", command=self.deposit, bg='#00796b', fg='white', width=20).pack(pady=5)
        tk.Button(main_frame, text="Withdraw", command=self.withdraw, bg='#00796b', fg='white', width=20).pack(pady=5)
        tk.Button(main_frame, text="Transfer", command=self.transfer, bg='#00796b', fg='white', width=20).pack(pady=5)
        tk.Button(main_frame, text="View History", command=self.view_history, bg='#00796b', fg='white', width=20).pack(pady=5)
        tk.Button(main_frame, text="Logout", command=self.setup_login_screen, bg='#00796b', fg='white', width=20).pack(pady=20)

    def check_balance(self):
        self.client.connect()
        msg = f"BALANCE|{self.client.id}"
        self.client.socket.send(msg.encode())
        balance = self.client.socket.recv(1024).decode()
        self.client.socket.close()
        messagebox.showinfo("Balance", f"Your current balance is: ${balance}")

    def deposit(self):
        amount = tk.simpledialog.askstring("Deposit", "Enter deposit amount:")
        if amount and amount.isdigit():
            self.client.connect()
            msg = f"DEPOSIT|{self.client.id},{amount}"
            self.client.socket.send(msg.encode())
            response = self.client.socket.recv(1024).decode()
            self.client.socket.close()
            if response == "DEPOSIT_SUCCESS":
                messagebox.showinfo("Success", "Deposit successful!")
            else:
                messagebox.showerror("Error", "Deposit failed")

    def withdraw(self):
        amount = tk.simpledialog.askstring("Withdraw", "Enter withdrawal amount:")
        if amount and amount.isdigit():
            self.client.connect()
            msg = f"WITHDRAW|{self.client.id},{amount}"
            self.client.socket.send(msg.encode())
            response = self.client.socket.recv(1024).decode()
            self.client.socket.close()
            if response == "WITHDRAW_SUCCESS":
                messagebox.showinfo("Success", "Withdrawal successful!")
            else:
                messagebox.showerror("Error", "Insufficient funds")

    def transfer(self):
        recipient = tk.simpledialog.askstring("Transfer", "Enter recipient ID:")
        amount = tk.simpledialog.askstring("Transfer", "Enter amount to transfer:")
        if recipient and amount and amount.isdigit():
            self.client.connect()
            msg = f"TRANSFER|{self.client.id},{recipient},{amount}"
            self.client.socket.send(msg.encode())
            response = self.client.socket.recv(1024).decode()
            self.client.socket.close()
            if response == "TRANSFER_SUCCESS":
                messagebox.showinfo("Success", "Transfer successful!")
            elif response == "INVALID_RECIPIENT":
                messagebox.showerror("Error", "Invalid recipient ID")
            else:
                messagebox.showerror("Error", "Insufficient funds")

    def view_history(self):
        self.client.connect()
        msg = f"HISTORY|{self.client.id}"
        self.client.socket.send(msg.encode())
        history = self.client.socket.recv(1024).decode()
        self.client.socket.close()
        messagebox.showinfo("Transaction History", history if history else "No transaction history available")

class Client:
    def __init__(self):
        self.socket = socket(AF_INET, SOCK_STREAM)

    def connect(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.connect(('192.168.1.XX', 9000))

if __name__ == "__main__":
    app = BankingGUI()
    app.root.mainloop()
