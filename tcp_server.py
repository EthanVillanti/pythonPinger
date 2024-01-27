import socket
import datetime
from random import randrange

#create server var  of type socket 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#localhost and unlikely port
server.bind(('127.0.0.1', 9999))

#listen for incoming connections
server.listen()

client, address = server.accept()
client.send("Hello Client!".encode('utf-8'))
print(f"Connected to {address}")
consecutiveDroppedPackets = 0




while True:
    
    # we know data payload, "seq #" + [sequence #], "timestamp" + [timestamp]
    tokens = client.recv(1024).decode('utf-8').split()
    
    # if we didn't get anything from the client just keep listening 
    if not tokens:
        print("Didn't get a packet")
        consecutiveDroppedPackets += 1
        if consecutiveDroppedPackets >= 5:
            break
        continue

    seqNum = tokens[2]
    if randrange(1,5) == 3:
        print("Simulated packet drop, clobbering sequence number")
        seqNum = int(seqNum) +1
    client.send(f"Ack {seqNum}".encode('utf-8'))

server.close
