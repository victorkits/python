# import asyncio
#
# import socketio
#
# sio = socketio.AsyncClient()
#
#
# @sio.event
# async def connect():
#     print('connection established')
#
#
# @sio.event
# async def my_message(data):
#     print('message received with ', data)
#     await sio.emit('my response', {'response': 'my response'})
#
#
# @sio.event
# async def disconnect():
#     print('disconnected from server')
#
#
# async def main():
#     await sio.connect('http://localhost:8000/api/v1/socket.io')
#     await sio.wait()
#
#
# if __name__ == '__main__':
#     asyncio.run(main())



import socketio

sio = socketio.Client()


@sio.event
def connect():
    print('connection established')
    sid = sio.sid
    server_sid = sio.get_sid()
    print(f'client_sid = {sid}, server_sid = {server_sid}')


@sio.event
def my_message(data):
    print('message received with ', data)
    sid = sio.sid
    server_sid = sio.get_sid()



# @sio.on('my_message')
# def on_message(data):
#     print(f'I received a message!{data}')


@sio.event
def disconnect():
    print('disconnected from server')


def main():

    sio.connect(url='http://localhost:8000', socketio_path="/api/v1/socket.io")
    sio.wait()

if __name__ == '__main__':
    main()