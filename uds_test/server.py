import socket
import os, os.path

serversocket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

socketPath = '/tmp/dmicade_socket.s'

if os.path.exists(socketPath):
    os.remove(socketPath)

print('Bind:', socketPath)
serversocket.bind(socketPath)

print('Listening for connection...')
serversocket.listen(1)

while True:
    clientsocket, addr = serversocket.accept()

    print('Connected: %s, %s' % (str(clientsocket), str(addr)))

    msg = 'Message from Python Script...'
    clientsocket.send(msg.encode('ascii'))

    recMsg = clientsocket.recv(1024)
    print('[Received Message]', recMsg.decode('ascii'))

    clientsocket.close()
    break
