import  socket
recv_ip="127.0.0.1"
recv_port=4444       #you can check free udp port netstat -nulp

#  creating  udp socket 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#  fitting    ip and port  with udp socket 
s.bind((recv_ip,recv_port))
while True:
#   recv  data  from  sender  
        data=s.recvfrom(100)
        print(data)
        rply=raw_input('Enter reply :')
        s.sendto(rply,data[1])


