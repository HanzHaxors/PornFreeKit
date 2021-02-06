class HTTPPacket(object):
	def __init__(self):
		...

	def load_from_raw_string(self, raw_string):
		self.raw_array = raw_array = raw_string.decode().split('\r\n')

		self.request = request = raw_array[0]
		self.method = method = request.split(' ')[0]
		self.path = path = request.split(' ')[1]
		self.protocol = protocol = request.split(' ')[2]
		self.headers = headers = dict()
		self.body = body = str()

		for header in raw_array[1:]:
			if header == '': # Headers and Body separator
				break
			else:
				headers[
					header.split(':')[0].strip()
					] = header.split(':')[1].strip()

		self.body = body = raw_array[-1]
