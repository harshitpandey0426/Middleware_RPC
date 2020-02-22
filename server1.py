import socket 
from _thread import *
import time
import threading 


def rpc_sum(a,b):
	return a+b


def rpc_sub(a,b):
	return a-b

def rpc_mul(a,b):
	return a*b

def rpc_div(a,b):
	return a/b
def threaded(c):
	func=c.recv(1024)
	func_name=func.decode("utf-8")
	c.send(bytes("function received","utf-8"))
	first=c.recv(1024)
	first_arg=int(first.decode("utf-8"))
	c.send(bytes("first arg received","utf-8"))
	# print(first_arg)

	second=c.recv(1024)
	second_arg=int(second.decode("utf-8"))
	c.send(bytes("second arg received","utf-8"))
	if(func_name=="rpc_sum"):
		res=rpc_sum(first_arg,second_arg)
	if(func_name=="rpc_sub"):
		res=rpc_sub(first_arg,second_arg)
	if(func_name=="rpc_mul"):
		res=rpc_mul(first_arg,second_arg)
	if(func_name=="rpc_div"):
		res=rpc_div(first_arg,second_arg)

	res=str(res)
	c.send(res.encode())



def Main(): 
	host = ""
	port=int(input())
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.bind((host, port)) 
	print("socket binded to port", port) 
	s.listen(5) 
	print("socket is listening") 

	while True:
		c, addr = s.accept()
		print('Connected to :', addr[0], ':', addr[1])

		start_new_thread(threaded, (c,)) 
	s.close()


if __name__ == '__main__': 
	Main() 