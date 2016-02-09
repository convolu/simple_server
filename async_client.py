import asyncio


@asyncio.coroutine
def make_request(host, port):
    reader, writer = yield from asyncio.open_connection(host, port)

    query_str = (
        'GET / HTTP/1.1\r\n'
        'Host: {host}\r\n'
        'Connection: close\r\n'
        '\r\n'
    ).format(host=host)

    writer.write(query_str.encode())

    yield from writer.drain()

    msgs = []
    while True:
        msg = yield from reader.read(1024)
        if msg:
            msgs.append(msg)
        else:
            break
    print((b''.join(msgs)).decode())

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [
        asyncio.ensure_future(make_request('voloudakis.me', 80))
    ]
    loop.run_until_complete(asyncio.wait(tasks))
