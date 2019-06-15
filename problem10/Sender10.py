import  socket
recv_ip="127.0.0.1"
recv_port=4444       #you can check free udp port netstat -nulp

#  creating  udp socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

option='''
        1. Sending/Receiving text msg from both side.
        2. Sending file from sender to receiver.
        '''

print(option)

choice=int(input('choose your option :'))


while choice==1:
        msg=raw_input('Enter message : ')
        #  sending  data  to target  
        s.sendto(msg,(recv_ip,recv_port))
        data=s.recvfrom(100)
        print(data)

#while choice == 2:
##      file=raw_input('Enter name of file :')
