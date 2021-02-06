import socket

class Client(object):
	def __init__(self):
		self.forward = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def start(self, host, port):
		try:
			self.forward.connect((host, port))
			return self.forward
		except Exception as e:
			print(e)
			return False
