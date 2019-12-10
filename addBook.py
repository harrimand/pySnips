
import csv

Data = [{'Index': '0', 'first_name': 'Darrell', 'last_name': 'Harriman', 'address': '1234 Apple Way', 'city': 'Apple Valley'}]

def read_file(path, keys, Data):
    with open(path, 'r') as csvFile:
        keys = csvFile.readline().strip().split(',')
        print("\nFile Keys: ", keys, "\n")
        reader = csv.DictReader(csvFile, fieldnames=keys)
        for row in reader:
            print("Row: ", dict(row))
            Data.append(dict(row))
        return keys

def add_member(keys, Data):
    print("\nAdding Member\n")
    newMember = get_info(keys, Data)
    Data.append(newMember)

def del_member(keys, Data): # Function Not Complete Yet
    print("\nDeleting Member Function Not Complete\n")

def print_membership(keys, Data):
    colWidth = colSize(keys, Data)
    print('\nMembership:')
    for d in range(len(Data)):
        print('\n\t', end='')
        for i, k in enumerate(keys):
            print(Data[d][k].ljust(colWidth[i] + 2), end = ' ')
    print('\n\n')

def del_column(keys, Data):
	delKey = input("\nEnter Column Name: ")
	if (delKey in keys):
		for D in Data:
			D.pop(delKey)
		keys.remove(delKey)
	else:
		print("\nKey Not Found")

def add_column(keys, Data):
	newKey = input("\nEnter Column Label (no Spaces): ")
	default = input("\nEnter Default Value for new column: ")
	for D in Data:
		D.update({newKey:default})
	keys.append(newKey)

def quit(keys, Data):
    print("Thank You for using my Address Book\n")

def menu():
    print("\nOptions:\na = add member\nd = delete member\ndc = delete column\nac = add column\np = print membership\nq = quit\n")

def get_info(keys, Data):
    info = {}
    Ind = max([int(k) for k in [Data[n]['id'] for n in range(len(Data))]]) + 1
    info['id'] = str(Ind)
    for k in keys[1:]:
        info[k] = input("Enter " + k + ": ")
    return info

def colSize(keys, Data):
	cS = [max([len(Data[n][k]) for n in range(len(Data))]) for k in keys]
	# print("\nColumn Widths: ", cS)
	return cS


Data = []
keys = []
# read_file('.\\addBook.csv', keys, Data)

opts = {'a': add_member, 'd': del_member, 'dc': del_column, 'ac': add_column, 'p': print_membership, 'q': quit}

# keys = ['Index', 'first_name', 'last_name', 'address', 'city']

keys = read_file('.\\addBook.csv', keys, Data)



Ind = max([int(k) for k in [Data[n]['id'] for n in range(len(Data))]]) + 1
newmem = [str(Ind), 'Isabelle', 'Ramos', '2345 Apple Way', 'Apple Valley']
newData = dict(zip(keys, newmem))
Data.append(newData)

Ind = max([int(k) for k in [Data[n]['id'] for n in range(len(Data))]]) + 1
newmem2 = [str(Ind), 'Frank', 'Enstien', '666 Muddy Road', 'CreepyVille']
newData = dict(zip(keys, newmem2))
Data.append(newData)

print('\n\n')
'''
newData = dict(zip(keys, newmem))
Data.append(newData)
newData = dict(zip(keys, newmem2))
Data.append(newData)
'''

print("Printing Data: ")
print(Data)

print('\n\n')

# opts['a'](keys, Data)


print('\n\n')
print("DATA: ", Data)
print("KEYS:", keys)


print('\n\n')
print('\n\n')

menu()
choice = ' '
while(choice != 'q'):
    print("Input Options: ", list(opts.keys()))
    choice = input("Choose Option: ")
    if choice in list(opts.keys()):
        opts[choice](keys, Data)

print('\n\n')
print(Data)

print('\n\n')
# print("\nMax Index: ", max([int(k) for k in [Data[n]['Index'] for n in range(len(Data))]]))
# print('\n\n')

for d in range(len(Data)):
    print(Data[d]['id'], Data[d]['first_name'])

