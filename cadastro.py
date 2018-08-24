import operations
import os.path
import crypto
import csv

#_encoded = str(crypto.encode(password)) #encode password
#_encoded = operations.filter_pass(_encoded) #filter password

def save(login,password): #save login and password in a csv file
	already_exists = os.path.isfile('cadastro.csv')
	_encoded = crypto.getMD5(password)
	if already_exists:
		_id = operations.lineCounter()
		table = open('cadastro.csv', 'a')
		table.write(str(_id) + ',' + login + ',' + _encoded + '\n')
		table.close()
	else:
		with open('cadastro.csv', 'a', newline='') as table:
			fieldnames = ['id', 'login', 'password']
			writer = csv.DictWriter(table, fieldnames=fieldnames)
			writer.writeheader()
			writer.writerow({'id': '1', 'login': login, 'password': _encoded})

def verify_user(user): #verify if an user exists
	with open('cadastro.csv', 'r') as table:
		data = csv.reader(table)
		for line in data:
			aux = str(line[1])
			if aux == user:
				return True
		return False

def verify_pass(user, password):
	password = crypto.getMD5(password)
	with open('cadastro.csv', 'r') as table:
		data = csv.reader(table)
		for line in data:
			if str(line[1]) == user:
				if str(line[2]) == password:
					return True
		return False



#operations.viewDatabase()
#save('erick', b'cavalo123')