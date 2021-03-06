import cadastro
import os.path
import crypto
import sys
import os

SetColorGreen = lambda: os.system('color 0a')
pause = lambda: os.system('pause')
clear = lambda: os.system('cls')

def register(): #Register a user
	print('\t Register user\n')
	login = input(' Login: ')
	if login == 'data':
		print("\n Your user can't be 'data'...\n\n")
		pause()
		clear()
		register()
	already_exists = os.path.isfile('enc_data.csv')
	if already_exists:
		if cadastro.verify_user(login):
			print('\nThis login already exits! Please, try another one..\n\n')
			pause()
			clear()
			register()
	password = input(' Password: ')
	pass2 = input(' Confirm password: ')
	if password != pass2:
		print("\n Passwords don't match! Try Again..\n")
		pause()
		clear()
		register()
	cadastro.save(login,password)
	print('\n User successfully registered\n\n')
	pause()
	clear()
	menu()

def registerPassword(username):
	print('\t Register Password\n')
	description = input(" Description: ")
	password = input(" Password: ")
	cadastro.savePass(username, bytes(password, 'utf-8'), description)
	print('\n Password save successfully\n\n')
	pause()
	clear()
	user_page(username)

def getPass(username):
	print('\t Get Password\n')
	description = input(' Description: ')
	returned = cadastro.searchPass(username, description)
	if returned == False:
		print(' There is no password with this description!\n\n')
		pause()
		clear()
		user_page(username)
	else:
		clear()
		print('\t Get Password\n')
		print(' Description: ' + description)
		print(' Password: ' + returned + '\n\n')
		pause()
		clear()
		user_page(username)

def user_page(username):
	print("\t Hi " + username + "!\n")
	print(" 1 - Save a password")
	print(" 2 - See my passwords")
	print(" 3 - Get a password")
	print(" 4 - Logout\n")
	op = int(input(" Option: "))
	if op == 2:
		clear()
		print('\t See my Passwords\n')
		flag = cadastro.seePasswords(username)
		if flag == True:
			print('\n')
			pause()
			clear()
			user_page(username)
		else:
			print(' There is no saved passwords for this user!\n')
			pause()
			clear()
			user_page(username)
	elif op == 1:
		clear()
		registerPassword(username)
	elif op == 3:
		clear()
		getPass(username)
	elif op == 4:
		clear()
		menu()
	
def login(): #login
	print('\t Login\n')
	_login = input('Login: ')
	already_exists = os.path.isfile('enc_data.csv')
	if already_exists:
		if cadastro.verify_user(_login) == False:
			print("\nThis user doesn't exist. Please, try another one..\n\n")
			pause()
			clear()
			login()
		password = input('Password: ')
		if cadastro.verify_pass(_login, password) == False:
			print('\nIncorrect login or password\n\n')
			pause()
			clear()
			login()
		else: #Open user page (Correct password)
			clear()
			user_page(_login)
	else:
		print('\nThere are no registered users\n\n')
		pause()
		clear()
		menu()

def menu(): #interface
	SetColorGreen()
	print('\t PassBank 3.0 by Cripto S.a\n')
	print(' 1 - Login')
	print(' 2 - Register user')
	print(' 3 - Exit\n')
	option = int(input(' Option: '))
	if option == 2:
		clear()
		register()
	elif option == 1:
		clear()
		login()
	elif option == 3:
		sys.exit()

menu()