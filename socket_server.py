# import socket
#
# # Create a TCP/IP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # Bind the socket to the port
# server_address = ('localhost', 5000)
# print('starting up on {} port {}'.format(*server_address))
# sock.bind(server_address)
#
# # Listen for incoming connections
# sock.listen(1)
#
# while True:
#     # Wait for a connection
#     print('waiting for a connection')
#     connection, client_address = sock.accept()
#     try:
#         print('connection from', client_address)
#
#         # Receive the data in small chunks and retransmit it
#         while True:
#             data = connection.recv(16)
#             print('received {!r}'.format(data))
#             if data:
#                 print('sending data back to the client')
#                 connection.sendall(data)
#             else:
#                 print('no data from', client_address)
#                 break
#
#     finally:
#         # Clean up the connection
#         connection.close()


from pure_flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, path="/v1/socket.io")

if __name__ == '__main__':
    socketio.run(app, port=8000)
