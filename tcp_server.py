# Assignment: TCP Simple Chat Room - TCP Server Code Implementation

# **Libraries and Imports**: 
#    - Import the required libraries and modules. 
#    You may need socket, threading, select, time libraries for the client.
#    Feel free to use any libraries as well.

# **Global Variables**:
#    - IF NEEDED, Define any global variables that will be used throughout the code.

# **Function Definitions**:
#    - In this section, you will implement the functions you will use in the server side.
#    - Feel free to add more other functions, and more variables.
#    - Make sure that names of functions and variables are meaningful.
def run(serverSocket, serverPort):
    # The main server function.
    pass

# **Main Code**:  
if __name__ == "__main__":
    server_port = 9301
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# Creating a TCP socket.
    server_socket.bind(('127.0.0.1', server_port))
    server_socket.listen(5) # set max no. of clients
    clients = [] #list to add the connected client sockets , feel free to adjust it to other place

    run(server_socket,server_port)# Calling the function to start the server.
