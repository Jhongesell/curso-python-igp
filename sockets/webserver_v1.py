import socket
import random
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
port = random.randint(1000, 2000)
server_address = ('localhost', port)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

body = """
<html>
<head>
  <title>An Example Page</title>
</head>
<body>
  Hello World, this is a very simple HTML document.
</body>
</html>
""".strip()

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(2048)
            print "data:"
            print >>sys.stderr, 'data: "%s"' % data.strip()
            if data.strip().startswith("GET /index.html HTTP/1.1"):
                resp = []
                resp.append("HTTP/1.1 200 OK")
                resp.append("Content-Type: text/html")
                resp.append("Content-Length: %d" % len(body))
                resp.append("Accept-Ranges: bytes")
                resp.append("Connection: close")
                resp.append("")
                resp.extend(body.split('\n'))
                resp = '\n'.join(resp)
                connection.sendall(resp)
                connection.close()

            else:
                print >>sys.stderr, 'no more data from', client_address
                break

    finally:
        # Clean up the connection
        connection.close()
