import csv

def lineCounter(): #get number of lines in csv file
	table = open('cadastro.csv', 'r')
	count = 0
	for rows in table:
		count += 1
	table.close()
	return count

def viewDatabase(): #print all rows in csv file
	table = open('cadastro.csv', 'r')
	data = csv.reader(table)
	for line in data:
	    print(line)
	table.close()

def filter_pass(text): #remove ' and b from a fernet output
	filtered = ''
	for index in range(1,len(text)-1):
		if text[index] != "'":
			filtered += text[index]
		else:
			continue
	return filtered