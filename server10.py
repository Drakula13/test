import asyncore, socket, collections
class async_http(asyncore.dispatcher):

	def __init__(self, port):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.bind(('0.0.0.0', port))
		self.listen(11)
		
	def handle_accept(self):
		client, addr = self.accept()
		return async_http_handler(client)
		
class async_http_handler(asyncore.dispatcher):

	def __init__(self, sock = None):
		asyncore.dispatcher.__init__(self,sock)
		self.got_request = False
		self.request_data = b""
		self.write_queue = collections.deque()
		self.responding = False
		
	def readable(self):
		return not self.got_request
		
	def handle_read(self):
		chunk = self.recv(1024)
		self.request_data += chunk
		if self == "close" | self == "Close": 
			self.close()
		
a = async_http(2222)
asyncore.loop()