import asyncore, socket
class http_client(asyncore.dispatcher):

	def __init__(self):
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.bind(('0.0.0.0', 2222))
		self.listen(11)
		
	def handle_connect(self):
		pass
			
	def handle_close(self):
		self.close()
			
	def handle_read(self):
		self.recv(1024)
	
	def writable(self):
		return (len(self.buffer) > 0)
			
	def handle_write(self):
		sent = self.send(self.buffer)
		self.buffer = self.buffer[sent:]		
asyncore.loop()