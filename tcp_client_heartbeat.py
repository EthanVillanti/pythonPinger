import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 9999))

print(client.recv(1024).decode('utf-8'))

#We don't care about RTT or dropped pings, just blast server with packets 
seqNum = 1

while True: 
    timeStamp = time.time()
    time.sleep(1)
    client.send(f"Heartbeat number {seqNum} from client time {timeStamp}".encode('utf-8'))
    seqNum += 1
    if seqNum > 3:
        break 
