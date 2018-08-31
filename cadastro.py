import operations
import os.path
import crypto
import csv

def save(login,password): #save login and password (users, not others) in a csv file
    already_exists = os.path.isfile('enc_data.csv')
    _encoded = crypto.getMD5(password)
    if already_exists:
        crypto.decodeDatabase()
        _id = operations.lineCounter()
        table = open('cadastro.csv', 'a')
        table.write(str(_id) + ',' + login + ',' + _encoded + '\n')
        table.close()
        crypto.encodeDatabase()
    else:
        with open('cadastro.csv', 'a', newline='') as table:
            fieldnames = ['id', 'login', 'password']
            writer = csv.DictWriter(table, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'id': '1', 'login': login, 'password': _encoded})
        crypto.encodeDatabase()

def savePass(username, password, description): #save description and password (not users)
    archive_name = 'enc_' + username + '.csv'
    already_exists = os.path.isfile(archive_name)
    _encoded = str(crypto.encode(password)) #encode password
    _encoded = operations.filter_pass(_encoded) #filter password
    if already_exists:
        crypto.decodeUserDatabase(username)
        archive_name = username + '.csv'
        table = open(archive_name, 'a')
        table.write(description + ',' + _encoded + '\n')
        table.close()
        crypto.encodeUserDatabase(username)
    else:
        archive_name = username + '.csv'
        with open(archive_name, 'a', newline='') as table:
            fieldnames = ['description', 'password']
            writer = csv.DictWriter(table, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'description': description, 'password': _encoded})
        crypto.encodeUserDatabase(username)

def seePasswords(username): #list every registered password of an user
    archive_name = 'enc_' + username + '.csv'
    already_exists = os.path.isfile(archive_name)
    if already_exists:
        crypto.decodeUserDatabase(username)
        archive_name = username + '.csv'
        with open(archive_name, 'r') as table:
            data = csv.reader(table)
            next(data) #don't wanna fist line
            for line in data:
                description = line[0] #get description from .csv
                password = line[1] #get encoded password from .csv
                password = bytes(password,'utf-8') #converting to bytes
                password = str(crypto.decode(password)) #decoding password
                password = operations.filter_pass(password) #filtering password
                print(' ' + description + ' - ' + password)
        crypto.encodeUserDatabase(username)
        return True
    else:
        return False

def searchPass(username, description): #search a password by its description
    archive_name = 'enc_' + username + '.csv'
    already_exists = os.path.isfile(archive_name)
    if already_exists:
        crypto.decodeUserDatabase(username)
        archive_name = username + '.csv'
        flag = False
        with open(archive_name, 'r') as table:
            data = csv.reader(table)
            for line in data:
                if line[0] == description: 
                    password = bytes(line[1],'utf-8') #converting password to bytes
                    password = str(crypto.decode(password)) #decoding password
                    password = operations.filter_pass(password) #filtering password
                    flag = True
                    break
        crypto.encodeUserDatabase(username)
        if flag == True:
            return password
        else:
            return False
    else:
        return False

def verify_user(user): #verify if an user exists
    crypto.decodeDatabase()
    flag = False
    with open('cadastro.csv', 'r') as table:
        data = csv.reader(table)
        for line in data:
            aux = str(line[1])
            if aux == user:
                flag = True
                break
    crypto.encodeDatabase()
    return flag

def verify_pass(user, password): #verify if a password is correct
    crypto.decodeDatabase()
    password = crypto.getMD5(password)
    flag = False
    with open('cadastro.csv', 'r') as table:
        data = csv.reader(table)
        for line in data:
            if str(line[1]) == user:
                if str(line[2]) == password:
                    flag = True
                    break
    crypto.encodeDatabase()
    return flag