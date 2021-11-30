import socket
# import threading
""" threading module is to speed up our server"""

class web_server_tcpHttp:
    def __init__(self, host_ip, port) -> None:
        """ We need to get the host-ip for our tcp server and port number."""
        self.host_ip = host_ip
        self.port = port
    
    def main(self):
        """ this is the main class function to run the start_server function of class and it's just calling function without calling directly."""
        self.start_server()

    def start_server(self):
        """ In start_server class, we will use the host-ip,port which was input by the user to create TCP server. """
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((self.host_ip, self.port))
        server.listen(1)
        print(f'Server is listening on ip:{self.host_ip}-port:{self.port}')
        print(f'server listening ip is - http://{self.host_ip}:{self.port}')
        while True:
            connectionSocket, address= server.accept()
            try:
                # request_handler = threading.Thread(target = self.send_http_request, args = (connectionSocket, ))
                # request_handler.start()
                """ here, if we want to speed up, we need to open comment above two code line and just need to comment below code line. And aslo need to open comment the threading module"""
                self.send_http_request(connectionSocket)
            except KeyboardInterrupt:
                connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
                connectionSocket.send("<html><head></head><body><h1>404 Not Found.</h1></body></html>")
                connectionSocket.close()

    def send_http_request(self, connection):
        """ this function will send our HTML code with HTTP request."""
        request = connection.recv(1024)
        """here, we need to send HTTP as byte. Following code line is to say that will we use HTTP 1.1 and 200 response"""
        connection.send(b"HTTP/1.1 200 OK\r\n\r\n")
        """following line is HTML code and we will link the bootstrap latest version 5.1.3 for semantic UI."""
        connection.send(b"<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'><meta http-equiv='X-UA-Compatible' content='IE=edge'><meta name='viewport' content='width=device-width, initial-scale=1.0'><!-- Bootstrap CSS --><link href='https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3' crossorigin='anonymous'><title>Document</title></head><body><marquee behavior='scroll' direction='left'><h4 style='color:navy;'>Hello: This is from TCP server http request. :-)</h4></marquee><h5 style='color: teal; text-align:center;'>Successfully Sent HTTP request from TCP server</h5></body></html>")
        connection.close()
        
if __name__ == '__main__':
    server = web_server_tcpHttp('localhost', 9999)
    server.main()
