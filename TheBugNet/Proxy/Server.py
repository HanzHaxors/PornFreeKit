import socket, time, select
from .Client import Client
from .HTTP.Request import request
from .HTTP.Packet import HTTPPacket

class ForwarderServer(object):
	packet_input_origins = list() # TODO: use set()
	channels = dict()

	def __init__(self, host, port, verbose=False, **kwargs):
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.server.bind((host, port))
		self.server.listen(200)

		self.BUFFER_SIZE = 2096
		self.forward_address = kwargs['fwd_addr'] or 'smpt.zaz.ufsk.br'
		self.forward_port = kwargs['fwd_port'] or 25

		self.verbose = verbose

	def start(self):
		print("[*] Starting forwarder server")
		self.packet_input_origins.append(self.server)
		while True:
			time.sleep(0.0001)
			selects = select.select
			input_ready, output_ready, except_ready = selects(self.packet_input_origins, [], [])

			for self.selected in input_ready:
				if self.selected == self.server:
					self.on_accept(self.forward_address, self.forward_port)
					break

				self.data = self.selected.recv(self.BUFFER_SIZE)
				if len(self.data) == 0:
					self.on_close()
					break
				else:
					self.on_recv()

	def on_accept(self, forward_address, forward_port):
		forward = Client().start(forward_address, forward_port)
		client_sock, client_address = self.server.accept()

		if forward:
			if self.verbose:
				print(f"[i] {client_address} has connected")

			self.packet_input_origins.append(client_sock)
			self.packet_input_origins.append(forward)
			self.channels[client_sock] = forward
			self.channels[forward] = client_sock
		else:
			if self.verbose:
				print(f"[!] Can't establish connection with forward server: {self.forward_address}:{self.forward_port}")
				print(f"[*] Closing connection with client {client_address}")

	def on_close(self):
		print(f"[-] {self.selected.getpeername()} has disconnected")
		self.packet_input_origins.remove(self.selected)
		self.packet_input_origins.remove(self.channels[self.selected])
		out = self.channels[self.selected]

		self.channels[out].close()

		self.channels[self.selected].close()

		del self.channels[out]
		del self.channels[self.selected]

	def on_recv(self):
		"""
		When the proxy receive a data:
		if data.from == forwarder:
			forwarder.send(data)
		else:
			data.from.send(data)
		"""
		data = self.data
		if self.verbose:
			print(f"{data}")

		self.channels[self.selected].send(data)

class Server(object):
	"""
	Real server where we will be processing images and HTTP requests
	"""
	def __init__(self, host, port, verbose=False, **kwargs):
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.settimeout(10)
		self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.server.bind((host, port))
		self.server.listen(200)

		self.BUFFER_SIZE = 4096
		self.verbose = verbose

	def start(self):
		print("[*] Starting main server")
		while True:
			try:
				connection, address = self.server.accept()
				print(f"[i] {address} connected")
				time.sleep(0.0001)
				data = connection.recv(self.BUFFER_SIZE)
				self.process_recv_bytes(connection, data)
			except Exception as e:
				print(f"\n[!] {e}\n")

	def process_recv_bytes(self, source_socket, data):
		try:
			request_obj = HTTPPacket()
			request_obj.load_from_raw_string(data)

			if self.verbose:
				print(f"[i] {request_obj.method} {request_obj.path}")

			request_response = request(
				body=request_obj.body,
				headers=request_obj.headers,
				method=request_obj.method,
				url=request_obj.path
				)
			#
			# if self.verbose:
			# 	print(f"[i] ################## Request ##################")
			# 	print(f"    {data.decode()}")
			# 	print(f"    ############ RAW Request")
			# 	print(f"    {request_response.raw_request}")
			# 	print(f"[i] #############################################")
			# 	print(f"[i] ################# Response ##################")
			# 	print(f"    {request_response.data}")
			# 	print(f"[i] #############################################")

			# source_socket.send(b"HTTP/1.1 200 OK\n")
			# source_socket.send(b"Haha: lol\n")
			# source_socket.send(b"\n")
			# source_socket.send(b"<html><h1>Hmmm.</h1></html>")

			print('' + request_response.data)

			source_socket.send(request_response.data.encode())
			source_socket.close()
		except Exception as e:
			print(e)
