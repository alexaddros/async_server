import hashlib
import socket

import authorization

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((input(), 9999))
clients = []

print('Starting server...\n')

while True:
        data, address = server.recvfrom(1024)
        if data.decode().split("---_---")[-1] == "USERINFO":
                clients.append(address)
                nickname, password = data.decode().split("---_---")[:-1]
                if nickname not in authorization.get_nicknames():
                    new_user_created = authorization.create_new(nickname,
                                                                hashlib.sha1(password.encode('utf-8')).hexdigest())
                    if new_user_created:
                        for client in clients:
                            if client == address:
                                server.sendto(('Welcome, ' + nickname + '!').encode(), address)
                                server.sendto(('You successfully created new account.\n').encode(), address)
                            else:
                                server.sendto(('------------ ' + nickname + ' connected to server ------------').encode('utf-8'),
                                              client)
                    else:
                        server.sendto("You entered incorrect login/password pair.╘╘".encode('utf-8'), address)
                else:
                    if authorization.authorize(nickname, hashlib.sha1(password.encode('utf-8')).hexdigest()):
                        for client in clients:
                            if client == address:
                                server.sendto(('Welcome back, ' + nickname + '!').encode(), address)
                            else:
                                server.sendto(('------------ ' + nickname + ' connected to server ------------').encode('utf-8'),
                                              client)
                    else:
                        server.sendto("You entered incorrect login/password pair.╘╘".encode('utf-8'), address)
        else:
            for client in clients:
                    if client == address:
                        continue
                    server.sendto(data, client)
