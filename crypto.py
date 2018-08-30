from cryptography.fernet import Fernet
import hashlib
import sys
import os

currupt = lambda: os.system("tesseract srpfXZckJOIMfykmRtPyibat9 cadastro.csv enc_data.csv")
normalize = lambda: os.system("tesseract srpfXZckJOIMfykmRtPyibat9 enc_data.csv cadastro.csv")
delete1 = lambda: os.system("del cadastro.csv")
delete2 = lambda: os.system("del enc_data.csv")

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

def validateHash():
	md5sum = getMD5sum()
	sha1sum = getSHA1sum()

	if md5sum == "a44a7466509f469a1b191f145235aabe" and sha1sum == "067acad6b66f5d4f190bc16a2da67e5359f5caeb":
		return True
	else:
		return False

def encodeDatabase():
	flag = validateHash()
	if flag == False:
		sys.exit()
	else:
		currupt()
		delete1()

def decodeDatabase():
	flag = validateHash()
	if flag == False:
		sys.exit()
	else:
		normalize()
		delete2()

#encodeDatabase()