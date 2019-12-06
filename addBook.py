
import csv

Data = [{'Index': '0', 'first_name': 'Darrell', 'last_name': 'Harriman', 'address': '1234 Apple Way', 'city': 'Apple Valley'}]

def add_member(keys, Data):
    print("\nAdding Member\n")
    newMember = get_info(keys, Data)
    Data.append(newMember)

def del_member(keys, Data): # Function Not Complete Yet
    print("\nDeleting Member Function Not Complete\n")

def print_membership(keys, Data):
    print('\nMembership:\n')
    for d in range(len(Data)):
        for k in keys:
            print(Data[d][k].ljust(20), end = ' ')
        print('')
    print('\n')

def quit(keys, Data):
    print("Thank You for using my Address Book\n")

def menu():
    print("\nOptions:\na = add member\nd = delete member\np = print membership\nq = quit\n")


def get_info(keys, Data):
    info = {}
    Ind = max([int(k) for k in [Data[n]['Index'] for n in range(len(Data))]]) + 1
    info['Index'] = str(Ind)
    for k in keys[1:]:
        info[k] = input("Enter " + k + ": ")
    return info


opts = {'a': add_member, 'd': del_member, 'p': print_membership, 'q': quit}

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
    choice = input("Choose Option a, d, p or q: ")
    if choice in opts.keys():
        opts[choice](keys, Data)

print('\n\n')
print(Data)

print('\n\n')
# print("\nMax Index: ", max([int(k) for k in [Data[n]['Index'] for n in range(len(Data))]]))
# print('\n\n')

for d in range(len(Data)):
    print(Data[d]['Index'], Data[d]['first_name'])


