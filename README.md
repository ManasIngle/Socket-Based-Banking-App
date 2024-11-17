# SocketBasedBankingApp

**SocketBasedBankingApp** is a basic client-server banking application developed using Python. It demonstrates the use of socket programming for network communication and Tkinter for building a simple graphical user interface (GUI). The application provides a set of fundamental banking operations like checking balance, depositing funds, withdrawing money, and transferring funds between users. 

This project is tailored for educational purposes and is an ideal starting point for beginners to learn about networking and GUI design in Python.

---

## Features

### User Registration
- Users can register with a unique ID.
- The application assigns a balance of `0` upon registration, and the user can then start making transactions.

### Check Balance
- Users can view their current account balance through a simple button click in the GUI.

### Deposit Money
- The application allows users to deposit funds into their account.
- The deposited amount is added to the current balance.

### Withdraw Money
- Users can withdraw funds from their account.
- The application checks if the user has sufficient balance before allowing the withdrawal.

### Transfer Money
- Users can transfer funds to another registered user.
- The application verifies both the sender’s balance and the recipient’s ID before completing the transfer.

### Simple GUI
- The client interface is designed using Tkinter, providing an intuitive and user-friendly experience with minimalistic buttons and input fields for easy navigation.

---

## Technologies Used
- **Python 3**: The main programming language used for both the server and client.
- **Socket Programming**: Enables network communication between the client and server using TCP sockets.
- **Tkinter**: A built-in Python library for creating graphical user interfaces, used here for the client-side application.
- **Threading**: Allows the server to handle multiple client connections simultaneously without blocking.

---

## Project Structure
├── client_ui.py       # Client-side application with GUI
├── server.py          # Server-side application handling transactions
├── README.md          # Project documentation

