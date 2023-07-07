#!/usr/bin/python

import urllib.parse,sys,os


# Getting files in local directory
directory = os.listdir()

# Header - Version Warning
print('\n' + '[+] Make sure that you are running Python3.x.x')
print('[+] This function only takes *.txt files')


# Checks to see whether there is are arguments called with this function
def check_file():
	global args
	global arguments
	global arg1
	global arg2
	args = sys.argv
	arguments = args[1:]
  
	if len(arguments) < 2 or '-h' in arguments:
		print('Usage: python3 url-enc-string.py <text_file_to_encode.txt> <encoded_file.txt>')
		sys.exit(1)
	else:
		# Assign the cli argument to variable
		arg1 = arguments[0]
		arg2 = arguments[1]


# Checking to see if *.txt file exists within our local directory
def file_exists(arg1):
  
	if arg1 in directory:
		pass
  
	else:
		print('\n' + f"Error: The file '{arg1}' does not exist in this directory")
		sys.exit(1)



def running(fil, enc_fil):
	
	fil = arg1
	tmp_fil = []
	enc_fil = arg2
	
	with open(fil,'rb') as temp:
		for line in temp.readlines():
			var = urllib.parse.quote(line)
			tmp_fil.append(var)

	with open(enc_fil,'wb') as temp:
		for line in tmp_fil:
			temp.write(line.encode())
			temp.write(b'\n')

	print('[+] All done!')

# Running functions 
check_file()
file_exists(arg1)
running(arg1,arg2)
