import shutil 
import re

  
# Copy src to dst. (cp src dst) 
file1=open("client1.py","r")

file2=open("client_stub.py","r")
file3=open("copy_client.py","r+")
lines1=file1.readlines()
lines2=file2.readlines()

for line2 in lines2:
	file3.write(line2)

for line1 in lines1:
	file3.write(line1)







# with open("client_stub.py", "r") as file:
# 	data2=file.read()
# print(data2)


# with open("client1.py", "r") as file:
# 	data=file.readlines()

# 	for line in data:
# 		x = re.findall("rpc.", line)

# 		if(len(x)>0):
# 			function=line
# 			# func=function[1]
# 			# print(function)
# 			# print(function[1])

# file2.writelines(data1)
# file2.writelines(data2)
# print(data2)



# print(data2)

# 
# file3.writelines(data2)


# file3=open("client_stub.py","w+")
# file3.writelines(function)



			# for i in range(len(function[1])):
			# 	if (function[1][i]=='('):
			# 		string_arg=
			# 		argument=function[1].split
			



		#if(x[0]=="rpc"):

			#print(dsk)


#print(x)
#print(x)