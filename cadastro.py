import operations
import os.path
import crypto
import csv

#_encoded = str(crypto.encode(password)) #encode password
#_encoded = operations.filter_pass(_encoded) #filter password

def save(login,password): #save login and password (users, not others) in a csv file
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

def savePass(username, password, description): #save description and password (not users)
	archive_name = username + '.csv'
	already_exists = os.path.isfile('cadastro.csv')
	_encoded = str(crypto.encode(password)) #encode password
	_encoded = operations.filter_pass(_encoded) #filter password
	if already_exists:
		table = open(archive_name, 'a')
		table.write(description + ',' + _encoded + '\n')
		table.close()
	else:
		with open(archive_name, 'a', newline='') as table:
			fieldnames = ['description', 'password']
			writer = csv.DictWriter(table, fieldnames=fieldnames)
			writer.writeheader()
			writer.writerow({'description': description, 'password': _encoded})

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


#savePass('erick',b'cavalo','netflix') OK
#operations.viewDatabase() OK
#save('erick', b'cavalo123') OK