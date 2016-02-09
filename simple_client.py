import socket


def make_request(host, port):
    sock = socket.socket()

    sock.connect((host, port))

    query_str = (
        'GET / HTTP/1.1\r\n'
        'Host: {host}\r\n'
        'Connection: close\r\n'
        '\r\n'
    ).format(host=host)

    sock.send(query_str.encode())

    msgs = []

    while True:
        msg = sock.recv(1024)
        if msg:
            msgs.append(msg)
        else:
            sock.close()
            break
    return (b''.join(msgs)).decode()

if __name__ == '__main__':
    print(make_request('voloudakis.me', 80))
