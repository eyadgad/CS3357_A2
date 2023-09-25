# Assignment: Simple Chat Room - Client Code Implementation

# **Libraries and Imports**: 
#    - Import the required libraries and modules. 
#    You may need the below libraries for the client.
#    Feel free to use any libraries as well.
import sys
import argparse
import select
import socket
import threading # u can use '_thread'

# **Global Variables**:
#    - IF NEEDED, Define any global variables that will be used throughout the code.

# **Function Definitions**:
#    - In this section, you will implement the functions you will use in the client side.
#    - If you will use and implement the below functions, please don't edit the namings.
#    - Feel free to add more other functions, and more variables.
#    - Make sure that names of functions and variables are meaningful.
#    - Take into consideration error handling, interrupts, client shutdown, and documentation.

def receive_messages():
    # Function to handle incoming messages from the server.
    pass

def send_message():
    # Function to send a message to the server.
    pass

def display_message():
    # Function to display a message from the server.
    pass

def run_client(clientSocket, clientname, serverAddr, serverPort):
    # The main client function.
    # It should handle incoming server messages, send messages to the server,
    # manage the client's connection, and gracefully exit.
    pass

# **Main Code**:  
if __name__ == "__main__":
    
    # Arguments: name address
    parser = argparse.ArgumentParser(description='argument parser')
    parser.add_argument('name')  # to use: python client.py name
    args = parser.parse_args()
    clientname = args.name
    serverAddr = '127.0.0.1'
    serverPort = 9301
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    run_client(clientSocket, clientname, serverAddr, serverPort)  # Calling the function to start the client.
