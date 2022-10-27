import asyncio

HOST = 'localhost'
PORT = 9095


async def tcp_echo_client(host, port):
    reader, writer = await asyncio.open_connection(host, port)
    message = 'Hello, world'

    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print('Данные: ', data.decode())
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_echo_client(HOST, PORT))
