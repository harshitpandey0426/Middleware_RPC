import socket

import socket

def rpc_sum(a,b):
	host = '127.0.0.1'
	port=int(input())

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
	s.connect((host,port))

	s.send(bytes("rpc_sum","utf-8"))
	resp=s.recv(1024)
	# s.send(bytes("2","utf-8"))
	# resp=s.recv(1024)
	a=str(a)
	b=str(b)

	s.send(a.encode("utf-8"))
	resp=s.recv(1024)
	s.send(b.encode("utf-8"))
	resp=s.recv(1024)
	ans=s.recv(1024)
	ans=ans.decode("utf-8")
	return ans

def rpc_sub(a,b):
	host = '127.0.0.1'
	port=int(input())

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
	s.connect((host,port))

	s.send(bytes("rpc_sub","utf-8"))
	resp=s.recv(1024)
	# s.send(bytes("2","utf-8"))
	# resp=s.recv(1024)
	a=str(a)
	b=str(b)

	s.send(a.encode("utf-8"))
	resp=s.recv(1024)
	s.send(b.encode("utf-8"))
	resp=s.recv(1024)
	ans=s.recv(1024)
	ans=ans.decode("utf-8")
	return ans

def rpc_mul(a,b):
	host = '127.0.0.1'
	port=int(input())

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
	s.connect((host,port))

	s.send(bytes("rpc_mul","utf-8"))
	resp=s.recv(1024)
	# s.send(bytes("2","utf-8"))
	# resp=s.recv(1024)
	a=str(a)
	b=str(b)

	s.send(a.encode("utf-8"))
	resp=s.recv(1024)
	s.send(b.encode("utf-8"))
	resp=s.recv(1024)
	ans=s.recv(1024)
	ans=ans.decode("utf-8")
	return ans

def rpc_div(a,b):
	host = '127.0.0.1'
	port=int(input())

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
	s.connect((host,port))

	s.send(bytes("rpc_div","utf-8"))
	resp=s.recv(1024)
	# s.send(bytes("2","utf-8"))
	# resp=s.recv(1024)
	a=str(a)
	b=str(b)

	s.send(a.encode("utf-8"))
	resp=s.recv(1024)
	s.send(b.encode("utf-8"))
	resp=s.recv(1024)
	ans=s.recv(1024)
	ans=ans.decode("utf-8")
	return ans



def main():
	# a=int(input())
	# b=int(input())  
		
	# rpc_sum(a,b)
	print("smc")
	print("divide = " ,rpc_div(20,10))
	print("multiplication = " ,rpc_mul(20,10))

if __name__ == '__main__': 
	main() 