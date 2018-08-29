from cryptography.fernet import Fernet
import hashlib

def encode(text):
	#key = Fernet.generate_key() #To generate a new key
	key = b'JwnKxByd3IzKB1KYIrCN5HKYGfKD88T8hOaLNCb4N9Y=' #static key (for use)
	cipher_suite = Fernet(key)
	cipher_text = cipher_suite.encrypt(text)
	return cipher_text

def decode(text):
	key = b'JwnKxByd3IzKB1KYIrCN5HKYGfKD88T8hOaLNCb4N9Y=' #static key (for use)
	cipher_suite = Fernet(key)
	plain_text = cipher_suite.decrypt(text)
	return plain_text

def getMD5(text):
	return hashlib.md5(text.encode('utf-8')).hexdigest()

#to = 'gAAAAABbhsIVE1t22SWPTNxE2IulifIHTpG0W_6PVO1WWPjYfNQQSEWOPYpNemOcx1aaAFdPeNsAqEomLG_OdoXBIq_P0lJ2SQ=='
#plain = decode(bytes(to,'utf-8'))
#print(plain)