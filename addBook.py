
import csv

# Data = [{'Index': '0', 'first_name': 'Darrell', 'last_name': 'Harriman', 'address': '1234 Apple Way', 'city': 'Apple Valley'}]

def read_file(path, keys, Data):
    with open(path, 'r') as csvFile:
        keys = csvFile.readline().strip().split(',')
        print("\nFile Keys: ", keys, "\n")
        reader = csv.DictReader(csvFile, fieldnames=keys)
        for row in reader:
            print("Row: ", dict(row))
            Data.append(dict(row))
        return keys

def write_file(keys, Data):
	with open('addBook.csv', 'w') as csvFile:
		writer = csv.DictWriter(csvFile, fieldnames=keys)
		writer.writeheader()
		for D in Data:
			writer.writerow(D)

def add_member(keys, Data):
    print("\nAdding Member\n")
    newMember = get_info(keys, Data)
    Data.append(newMember)

def del_member(keys, Data):
    index = search(keys, Data)
    Data.remove(Data[index])

def edit_member(keys, Data):
    print("\nSelect Member to edit: ", end='')
    mem = search(keys, Data)
    for i, k in enumerate(keys):
        print("\t" + str(i+1).ljust(4) + k)
    select = input("\nSelect value to edit (1 through " + str(len(keys)) + "): ")
    print(keys[int(select) - 1], " selected")
    newVal = input("Enter new Value: ")
    Data[mem].update({keys[int(select)-1]: newVal})

def print_membership(keys, Data):
    colWidth = colSize(keys, Data)
    print('\nResult:')
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

def search(keys, Data):
    print('\n')
    for i, k in enumerate(keys):
        print("\t" + str(i+1).ljust(4) + k)
    select = input("\nSelect search criteria (1 through " + str(len(keys)) + "): ")
    print(keys[int(select) - 1], " selected")
    find = input("Enter " + keys[int(select) - 1] + " to search for: ")
    result = []
    for D in Data:
        if(D[keys[int(select) - 1]] == find):
            result.append(D)
    print("\nFound ", len(result), " results")
    print_membership(keys, result)
    chosenResult = input("Choose result id or 0 to abort search: ")
    for i, D in enumerate(Data):
        if(D['id'] == chosenResult):
            return i
    return -1

def add_column(keys, Data):
	newKey = input("\nEnter Column Label (no Spaces): ")
	default = input("\nEnter Default Value for new column: ")
	for D in Data:
		D.update({newKey:default})
	keys.append(newKey)

def quit(keys, Data):
	save = input("Save Changes before quitting? [y,n]: ")
	if(save == 'y'):
		write_file(keys, Data)
	print("Thank You for using my Address Book\n")

def menu():
    print("\nOptions:\na = add member\nd = delete member\ne = edit member\ndc = delete column\n\
ac = add column\np = print membership\nw = write file\nq = quit\n")

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

opts = {'a': add_member, 'd': del_member, 'e': edit_member, 'dc': del_column, 'ac': add_column,\
'p': print_membership, 'w': write_file, 'q': quit}

# keys = ['Index', 'first_name', 'last_name', 'address', 'city']

keys = read_file('addBook.csv', keys, Data)


'''
Ind = max([int(k) for k in [Data[n]['id'] for n in range(len(Data))]]) + 1
newmem = [str(Ind), 'Isabelle', 'Ramos', '2345 Apple Way', 'Apple Valley']
newData = dict(zip(keys, newmem))
Data.append(newData)

Ind = max([int(k) for k in [Data[n]['id'] for n in range(len(Data))]]) + 1
newmem2 = [str(Ind), 'Frank', 'Enstien', '666 Muddy Road', 'CreepyVille']
newData = dict(zip(keys, newmem2))
Data.append(newData)
'''
print('\n\n')
'''
newData = dict(zip(keys, newmem))
Data.append(newData)
newData = dict(zip(keys, newmem2))
Data.append(newData)
'''
'''
print("Printing Data: ")
print(Data)

print('\n\n')

# opts['a'](keys, Data)


print('\n\n')
print("DATA: ", Data)
print("KEYS:", keys)
'''

# print(Data[search(keys, Data)])

print('\n\n')

# edit_member(keys, Data)

print('\n\n')

menu()
choice = ' '
while(choice != 'q'):
    print("Input Options: ", list(opts.keys()))
    choice = input("Choose Option: ")
    if choice in list(opts.keys()):
        opts[choice](keys, Data)

'''
print('\n\n')
print(Data)

print('\n\n')
# print("\nMax Index: ", max([int(k) for k in [Data[n]['Index'] for n in range(len(Data))]]))
# print('\n\n')

for d in range(len(Data)):
    print(Data[d]['id'], Data[d]['first_name'])
'''

