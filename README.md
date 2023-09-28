
# CS3357A Assignment #2: Building Two Chatroom Applications Using TCP and UDP

This repository contains the code and instructions for CS3357A Assignment #2, where you will implement two chatroom applications in Python using both TCP and UDP protocols.

## Assignment Overview

### Task Description

In this assignment, you will build two chatroom applications: one using TCP and the other using UDP. Each application will consist of both a server and a client component. 

**TCP Chatroom:**
- The TCP chat server should accept incoming connections from multiple clients.
- It should receive and broadcast messages to all connected clients.
- The server should manage client connections and disconnections gracefully.

**UDP Chatroom:**
- The UDP chat server should accept incoming messages from multiple clients.
- It should broadcast received messages to all connected clients.
- The server should also handle client join and leave events.

### Directory Structure

This repository is organized as follows:

- `tcp_server.py`: Contains the code for the TCP chat server.
- `tcp_client.py`: Contains the code for the TCP chat client.
- `udp_server.py`: Contains the code for the UDP chat server.
- `udp_client.py`: Contains the code for the UDP chat client.
- `README.md`: This file, containing assignment instructions and usage guidelines.

## Instructions

To complete this assignment, follow these steps:

1. **TCP Server and Client Implementation**:
   - Open `tcp_server.py` and `tcp_client.py`.
   - Implement the required server and client functions as per the provided guidelines.
   - Ensure proper error handling and graceful shutdown for both server and client.

2. **UDP Server and Client Implementation**:
   - Open `udp_server.py` and `udp_client.py`.
   - Implement the required server and client functions based on the provided guidelines.
   - Ensure error handling and graceful exit for both server and client.

3. **Testing**:
   - Test your TCP and UDP chat servers and clients by running them locally.
   - Ensure that the servers can handle multiple client connections (TCP) and messages broadcasting (UDP).

## Usage

### TCP Chatroom

**Server Usage:**

```bash
python tcp_server.py
```

**Client Usage:**

```bash
python tcp_client.py <client_name>
```

Replace `<client_name>` with your desired username.

### UDP Chatroom

**Server Usage:**

```bash
python udp_server.py
```

**Client Usage:**

```bash
python udp_client.py <client_name>
```

Replace `<client_name>` with your desired username.

## Contact

If you encounter any issues or have questions, please contact [Your Name] at [your_email@example.com].
```

Replace `[Your Name]` and `[your_email@example.com]` with your name and email address for inquiries related to the assignment.

Make sure to include this updated README in your GitHub repository for clear instructions and information about your assignment.
