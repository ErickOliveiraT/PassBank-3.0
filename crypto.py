from cryptography.fernet import Fernet
import hashlib
import sys
import os

global command #to use in prompt

def encode(text): #Encodes passwords using Fernet method
	#key = Fernet.generate_key() #To generate a new key
	key = b'JwnKxByd3IzKB1KYIrCN5HKYGfKD88T8hOaLNCb4N9Y=' #static key (for use)
	cipher_suite = Fernet(key)
	cipher_text = cipher_suite.encrypt(text)
	return cipher_text

def decode(text): #Decodes passwords using Fernet method
	key = b'JwnKxByd3IzKB1KYIrCN5HKYGfKD88T8hOaLNCb4N9Y=' #static key (for use)
	cipher_suite = Fernet(key)
	plain_text = cipher_suite.decrypt(text)
	return plain_text

def getMD5(text): #MD5 hash of users passwords
	return hashlib.md5(text.encode('utf-8')).hexdigest()

def getMD5sum(): #MD5 sum of tesseract encoder
	BLOCKSIZE = 65536
	hasher = hashlib.md5()
	with open('tesseract.exe', 'rb') as afile:
	    buf = afile.read(BLOCKSIZE)
	    while len(buf) > 0:
	        hasher.update(buf)
	        buf = afile.read(BLOCKSIZE)
	return hasher.hexdigest()

def getSHA1sum(): #SHA1 sum of tesseract encoder
	BLOCKSIZE = 65536
	hasher = hashlib.sha1()
	with open('tesseract.exe', 'rb') as afile:
	    buf = afile.read(BLOCKSIZE)
	    while len(buf) > 0:
	        hasher.update(buf)
	        buf = afile.read(BLOCKSIZE)
	return hasher.hexdigest()

def validateHash(): #check if tesseract has intentionally modified
	md5sum = getMD5sum()
	sha1sum = getSHA1sum()

	if md5sum == "a44a7466509f469a1b191f145235aabe" and sha1sum == "067acad6b66f5d4f190bc16a2da67e5359f5caeb":
		return True
	else:
		return False

def encodeDatabase(): #encode users database
	flag = validateHash()
	if flag == True:
		command = 'tesseract srpfXZckJOIMfykmRtPyibat9 '
		command += 'cadastro.csv enc_data.csv'
		os.system(command)
		command = 'del cadastro.csv'
		os.system(command)
		command = ''
	else:
		sys.exit()

def decodeDatabase(): #decodeu users database
	flag = validateHash()
	if flag == True:
		command = 'tesseract srpfXZckJOIMfykmRtPyibat9 '
		command += 'enc_data.csv cadastro.csv'
		os.system(command)
		command = 'del enc_data.csv'
		os.system(command)
		command = ''
	else:
		sys.exit()

def encodeUserDatabase(username): #encode user database of saved passwords and description
	archive_name = username + '.csv'
	command = 'tesseract srpfXZckJOIMfykmRtPyibat9 '
	command += archive_name + ' ' + 'enc_'
	command += username + '.csv'
	os.system(command)
	command = 'del ' + username + '.csv'
	os.system(command)
	command = ''

def decodeUserDatabase(username): #decode user database of saved passwords and description
	archive_name = username + '.csv'
	command = 'tesseract srpfXZckJOIMfykmRtPyibat9 '
	command += 'enc_' + username + '.csv '
	command += username + '.csv'
	os.system(command)
	command = 'del enc_' + username + '.csv'
	os.system(command)
	command = ''