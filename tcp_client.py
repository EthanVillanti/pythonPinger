import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 9999))

#lists to store dataa
RTT = 0.0
packetsLost = 0
seqNum = 1

print(client.recv(1024).decode('utf-8'))

## HARD CODED VALUES ##
packetsToSend = 10



for i in range(packetsToSend):

    
    #send a message with seq # and timestamp 
    timeNaught = time.time()
    client.send(f"Sequence number: {i+1} timestamp {timeNaught}".encode('utf-8'))
    
    tokens = client.recv(1024).decode('utf-8').split()
    if int(tokens[1]) == (i+1):
        print(f"Sucess seq num {tokens[1]}")
        RTT += time.time() - timeNaught
    else: 
        print("failure")
        packetsLost += 1

    #wait one second between pings
    time.sleep(1)

#packet statistics
avgRTT = RTT / packetsToSend
print("Packet statistics: ")
print(f"Average RTT: {avgRTT}")
print(f"Number of packets lost: {packetsLost}")

    
#server is waiting for a message, so send one from client 
#client.send("Hello Server".encode('utf-8'))
#print(client.recv(1024).decode('utf-8'))

