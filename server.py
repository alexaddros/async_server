import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind (('skopcovs1.fvds.ru', 9090))

client = [] # Массив, где храним адреса клиентов
print ('Start Server\n')

while True:
        data , addres = sock.recvfrom(1024)
        if  addres not in client : 
                client.append(addres)
                print("------------")
                print("Nickname:", data.split()[0].decode("utf-8"), "\nIP:      ", addres[0])
                print("------------\n")
        for clients in client :
                if clients == addres: 
                    continue # Не отправлять данные клиенту который их прислал
                sock.sendto(data,clients)	
