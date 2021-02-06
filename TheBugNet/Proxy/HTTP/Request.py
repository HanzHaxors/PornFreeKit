import socket
import urllib.parse as parse
import urllib.parse as urlparse
from .Response import Response

HTTP_VERSION = 1.1
CRLF = "\r\n\r\n"


def receive_all(sock, chunk_size=4096):
	chunks = []
	chunk = sock.recv(int(chunk_size))
	try:
		while chunk:
			chunks.append(chunk)
			chunk = sock.recv(int(chunk_size))
	except:
		...

	return ''.join([s.decode() for s in chunks])

def request(url, **kw):
	kw.setdefault('method', "GET")
	kw.setdefault('timeout', 1)
	kw.setdefault('chunk_size', 4096)
	kw.setdefault('http_version', HTTP_VERSION)
	kw.setdefault('headers', { 'Accept': '*/*' })
	kw.setdefault('body', '')

	parsedHeaders = ''
	for key, value in kw.get('headers').items():
		parsedHeaders += f"{key}: {value}\r\n"

	parsedHeaders = parsedHeaders[:-2]

	socket.setdefaulttimeout(kw['timeout'])

	url = urlparse.urlparse(url)
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(kw.get('timeout'))
	sock.connect((url.netloc, url.port or 80))
	msg = '{0} {1} HTTP/{2}\r\n{3}{4}{5}'
	msg = msg.format(
					kw.get('method'),
					url.path or '/',
                    kw.get('http_version'),
					parsedHeaders,
					CRLF,
					'\n\n' + kw.get('body') if kw.get('body') else ''
					).encode()

	sock.sendall(msg)

	data = receive_all(sock, chunk_size=kw.get('chunk_size'))
	sock.shutdown(socket.SHUT_RDWR)
	sock.close()

	data = data
	headers = data.split(CRLF, 1)[0]
	request_line = headers.split('\n')[0]
	response_code = request_line.split()[1]
	headers = headers.replace(request_line, '')
	body = data.replace(headers, '').replace(request_line, '')

	response = Response(data=data,
						headers=headers,
						response_code=response_code,
						body=body,
						raw_request=msg)
	return response
