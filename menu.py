import cadastro
import os.path
import sys
import os
import time

SetColorGreen = lambda: os.system('color 0a')
pause = lambda: os.system('pause')
clear = lambda: os.system('cls')

def register(): #Register a user
	print('\t Register user\n')
	login = input('Login: ')
	already_exists = os.path.isfile('cadastro.csv')
	if already_exists:
		if cadastro.verify_user(login):
			print('\nThis login already exits! Please, try another one..\n\n')
			pause()
			clear()
			register()
	password = input('Password: ')
	pass2 = input('Confirm password: ')
	if password != pass2:
		print("\nPasswords don't match! Try Again..\n")
		pause()
		clear()
		register()
	cadastro.save(login,password)
	print('\nUser successfully registered\n\n')
	pause()
	clear()
	menu()

def user_page(username):
	print("\t Hi " + username + "!\n")
	print(" 1 - Save a password")
	print(" 2 - See my passwords")
	print(" 3 - Get a password")
	print(" 4 - Return to menu\n")
	op = int(input(" Option: "))
	if op == 1:
		clear()
		#Password(username)
	elif op == 2:
		clear()
		#seePass(username)
	elif op == 3:
		clear()
		#getPass(username)
	elif op == 4:
		clear()
		menu()
	
def login(): #login
	print('\t Login\n')
	_login = input('Login: ')
	already_exists = os.path.isfile('cadastro.csv')
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
		else:
			#Open user page (Correct password)
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