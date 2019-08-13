import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind (('', 9090))

client = [] # Массив где храним адреса клиентов
print ('Start Server')

while True:
         data , addres = sock.recvfrom(1024)
         print (addres[0], addres[1])
         if  addres not in client : 
                 client.append(addres)# Если такова клиента нету , то добавить
         for clients in client :
                 if clients == addres: 
                     continue # Не отправлять данные клиенту который их прислал
                 sock.sendto(data,clients)
