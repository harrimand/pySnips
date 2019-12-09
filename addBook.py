
import csv

Data = [{'Index': '0', 'first_name': 'Darrell', 'last_name': 'Harriman', 'address': '1234 Apple Way', 'city': 'Apple Valley'}]

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
    print("\nOptions:\na = add member\nd = delete member\ndc = delete column\nac = add column\n\
	p = print membership\nq = quit\n")

def get_info(keys, Data):
    info = {}
    Ind = max([int(k) for k in [Data[n]['Index'] for n in range(len(Data))]]) + 1
    info['Index'] = str(Ind)
    for k in keys[1:]:
        info[k] = input("Enter " + k + ": ")
    return info

def colSize(keys, Data):
	cS = [max([len(Data[n][k]) for n in range(len(Data))]) for k in keys]
	# print("\nColumn Widths: ", cS)
	return cS

opts = {'a': add_member, 'd': del_member, 'dc': del_column, 'ac': add_column, 'p': print_membership, 'q': quit}

keys = ['Index', 'first_name', 'last_name', 'address', 'city']

newmem = ['1', 'Isabelle', 'Ramos', '2345 Apple Way', 'Apple Valley']
newmem2 = ['2', 'Frank', 'Enstien', '666 Muddy Road', 'CreepyVille']

print('\n\n')
newData = dict(zip(keys, newmem))
Data.append(newData)
newData = dict(zip(keys, newmem2))
Data.append(newData)

print(Data)

print('\n\n')

# opts['a'](keys, Data)

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
    print(Data[d]['Index'], Data[d]['first_name'])


