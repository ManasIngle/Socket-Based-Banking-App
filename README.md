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

## Project Structure
- The project directory is organized as follows:
```plaintext
SocketBasedBankingApp/
├── client_ui.py       # Client-side application with GUI
├── server.py          # Server-side application handling transactions
├── README.md          # Project documentation

```
## File Descriptions

- **client_ui.py**: Contains the GUI logic for the client application, enabling user registration, balance checks, deposits, withdrawals, and fund transfers.
- **server.py**: Implements the server-side logic, managing client requests, maintaining account balances, and ensuring secure and consistent transaction processing.
- **README.md**: Provides comprehensive documentation of the project, including setup instructions, usage examples, and descriptions of features and functionality.

---
## Prerequisites

- **Python 3**: Ensure Python 3 is installed on both the client and server machines.
- **Basic Knowledge**: A foundational understanding of Python programming, particularly in socket programming and Tkinter, is recommended.
- **Network Accessibility**: Both the client and server should either be on the same network or have the server's IP address accessible to the client machine.

## Setup and Running Instructions

### Step 1: Start the Server
1. Open a terminal or command prompt on the **server machine**.
2. Navigate to the directory where the project files are located.
3. Start the server by running the script:
   ```bash
   python server.py
4. The server will start listening on the specified IP address and port (default: 192.168.1.XX:9000).

## Configuration

To change the server's IP address or port, follow these steps:

1. Open the `client_ui.py` file in a text editor.
2. Locate the line where the client connects to the server:
   ```python
   self.socket.connect(('192.168.1.XX', 9000))
3. Replace '192.168.1.XX' and 9000 with your desired server IP address and port. For example:
  ```python
  self.socket.connect(('127.0.0.1', 8080))
  ```
- '127.0.0.1': Specifies the server's IP address.
-  8080: Specifies the server's port.
---
## Example Usage

1. **Launch the Server**:
   - Run the server script:
     ```bash
     python server.py
     ```

2. **Launch the Client**:
   - Start the client GUI:
     ```bash
     python client_ui.py
     ```

3. **Register a User**:
   - Create an account by entering a unique user ID (e.g., `user123`).

4. **Perform Operations via the GUI**:
   - **Check Balance**: View the current balance of your account.
   - **Deposit Money**: Add funds to your account balance.
   - **Withdraw Money**: Withdraw funds if you have sufficient balance.
   - **Transfer Money**: Enter the recipient's ID and the amount to transfer funds to another user.

---

## Limitations

- **No Data Persistence**:
  - User balances are stored in memory and are reset when the server restarts. Incorporating a database would address this limitation.

- **Basic Error Handling**:
  - While common errors are managed, some edge cases, such as invalid input formats, may not be fully handled.

- **No Encryption**:
  - Data is transmitted in plain text, leaving it vulnerable to eavesdropping. This project is intended for educational purposes only and not for real-world use.

---

## Future Enhancements

1. **User Authentication**:
   - Implement a secure login system with usernames and passwords for enhanced security.

2. **Persistent Data Storage**:
   - Use a database, such as SQLite or PostgreSQL, to save user details and account balances across sessions.

3. **Enhanced Security**:
   - Add encryption protocols (e.g., SSL/TLS) to secure data communication between the client and server.

4. **Improved GUI Design**:
   - Modernize the interface with updated design elements and add features like a transaction history log.
