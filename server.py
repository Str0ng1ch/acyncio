import asyncio

HOST = 'localhost'
PORT = 9095


async def handle_echo(reader, writer):
    data = await reader.read(100)
    print('Полученные данные: ', data.decode())

    writer.write(data)
    await writer.drain()

    writer.close()


async def main():
    server = await asyncio.start_server(handle_echo, HOST, PORT)
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())
