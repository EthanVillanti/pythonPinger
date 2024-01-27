Client and server implementation of a basic tcp pinger written in python 

Server sits in an infinite loop waiting for packets, if certain amount of time passes without receiving any pings the server will timeout. 

Client sends a customizable number of pings to the server and the two synchronize with a sequence number. Packet losses and round trip times are computed with averages presented to the user. 

Heartbeat client blasts server with a <configuratble> amount of packets
Heartbeat server listens for packets from client, warns user about potential latency issues and exits upon device dropping offline (5 consecutive dropped packets)
