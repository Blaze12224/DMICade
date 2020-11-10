import socket

clientsocket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

socketPath = '/tmp/dmicade_socket.s'

print('Connecting:', socketPath)
clientsocket.connect(socketPath)
print('Connected!')

msg = clientsocket.recv(1024)

print('[Received Message]', msg.decode('ascii'))

msgPayload = "test123 test"
clientsocket.send(msgPayload.encode('ascii'))

clientsocket.close()
