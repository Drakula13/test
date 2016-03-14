#TCP echo сервер на Python (параллельные запросы 11 пользователей)
import asyncore, socket
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
		
	def handle_read(self):
		data = self.recv(1024)
		if data == "close": 
			self.close()
		else: 
			self.send(data)
			
a = async_http(2222)
asyncore.loop()