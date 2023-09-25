# Assignment: Simple Chat Room - Server Code Implementation

# **Libraries and Imports**: 
#    - Import the required libraries and modules. 
#    You may need the below libraries for the client.
#    Feel free to use any libraries as well.
import socket
import select
import time

# **Global Variables**:
#    - IF NEEDED, Define any global variables that will be used throughout the code.

# **Function Definitions**:
#    - In this section, you will implement the functions you will use in the server side.
#    - If you will use and implement the below functions, please don't edit the namings.
#    - Feel free to add more other functions, and more variables.
#    - Make sure that names of functions and variables are meaningful.
#    - Take into consideration error handling, interrupts, client shutdown, and documentation.

def broadcast_message():
    # Broadcasts a message to all connected clients.
    pass

def run_server(serverSocket, serverPort):
    # The main server function.
    # It should handle incoming client messages,
    # manage client connections, and broadcast messages.
    pass

# **Main Code**:  
if __name__ == "__main__":
    
    serverPort = 9301  # Set the `serverPort` to the desired port number (e.g., 9301).
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Creating a UDP socket named.
    run_server(serverSocket, serverPort)  # Calling the function to start the server.
