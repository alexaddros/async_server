import hashlib
import socket

import authorization

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('skopcovs1.fvds.ru', 9090))
clients = []

print('Start Server\n')

while True:
        data, address = server.recvfrom(1024)
        if data.decode().split("---_---")[-1] == "USERINFO":
                clients.append(address)
                nickname, password = data.decode().split("---_---")
                if nickname not in authorization.get_nicknames():
                    new_user_created = authorization.create_new(nickname,
                                                                hashlib.sha1(password.encode('utf-8')).hexdigest())
                    if new_user_created:
                        for client in clients:
                            if client == address:
                                continue
                            server.sendto(f'------------ {nickname} connected to server ------------'.encode('utf-8'),
                                          client)
                else:
                    if authorization.authorize(nickname, hashlib.sha1(password.encode('utf-8')).hexdigest()):
                        server.sendto('SUCCESS'.encode('utf-8'), address)
        else:
            for client in clients:
                    if client == address:
                        continue
                    server.sendto(data, client)
