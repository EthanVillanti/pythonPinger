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
counter = 1




while True:
    #randomly drop 20% of packets 
    randomNum = randrange(1,5)
    if randomNum == 3: 
        print("simulated packet drop")
        continue
    
    # we know data payload, "seq #" + [sequence #], "timestamp" + [timestamp]
    tokens = client.recv(1024).decode('utf-8').split()
    if not tokens:
        print(f"didn't get a packet, expexting seq num {counter}")
        consecutiveDroppedPackets += 1
        if consecutiveDroppedPackets >= 5: 
            print("5 consecutive dropped packets. Exiting")
            break
        else:
            counter += 1
            continue
    consecutiveDroppedPackets = 0
    seqNum = tokens[2]
    timeStamp = tokens[4]
    if int(counter) == int(seqNum):
        client.send(f"Ack {seqNum}".encode('utf-8'))
    else: 
        print("dropped packet")
        #increment droppedPackets variable? do we care about packets 
    counter += 1  
server.close