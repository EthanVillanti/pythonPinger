import socket
import time

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
expectedSeqNum = 1

while True:
    
    # we know data payload, "seq #" + [sequence #], "timestamp" + [timestamp]
    tokens = client.recv(1024).decode('utf-8').split()
    if not tokens:
        print(f"didn't get a packet, expexting seq num {expectedSeqNum}")
        consecutiveDroppedPackets += 1
        if consecutiveDroppedPackets >= 5: 
            print("5 consecutive dropped packets. Exiting")
            break
        else:
            expectedSeqNum += 1
            continue
    
    consecutiveDroppedPackets = 0
    seqNum = tokens[2]
    timeStamp = tokens[6]
    
    if int(expectedSeqNum) == int(seqNum):
        print(f"Confirmed heartbeat {seqNum}")
        #look for latency in system 
        oneWayTime = time.time() - float(timeStamp)
        if oneWayTime >= 1.0: 
            print("Packets taking longer than one second to get to server")
            print("Potential latency issue needing investigation") 
    else: 
        print("Received different sequence number than expected")
        print(f"Received {seqNum}, expected {expectedSeqNum}") 
    expectedSeqNum += 1  