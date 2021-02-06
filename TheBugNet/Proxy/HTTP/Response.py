class Response(object):
	def __init__(self, **kwargs):
		self.response_code = kwargs['response_code']
		self.body = kwargs['body']
		self.headers = kwargs['headers']
		self.data = kwargs['data']
		self.raw_request = None if not kwargs['raw_request'] else kwargs['raw_request']

	def __str__(self):
		return self.data
