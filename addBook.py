#!/usr/bin/env python
""" file: addBook.py maintains address book stored in addBook.csv
    Author: Darrell harriman
    Email: harrimand@gmail.com
    Description:  Read addBook.csv address book table into a list of dictionaries
    Functions: Add member, Delete member, Edit member, Add column, Delete column,
        Print table, Look up member, Write table to file, Quit
    """

import csv

def read_file(path, keys, Data):
    """ Read .csv file first line to list of keys and remaining lines to list of dictionaries"""
    with open(path, 'r') as csvFile:
        keys = csvFile.readline().strip().split(',')
        print("\nFile Keys: ", keys, "\n")
        reader = csv.DictReader(csvFile, fieldnames=keys)
        for row in reader:
            print("Row: ", dict(row))
            Data.append(dict(row))
        return keys

def write_file(keys, Data):
    """Write list of keys to first line and list of dictionaries to remaining lines of file"""
    with open('addBook.csv', 'w') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=keys)
        writer.writeheader()
        for D in Data:
            writer.writerow(D)

def add_member(keys, Data):
    """Add new row with member information to list of dictionaries"""
    print("\nAdding Member\n")
    newMember = get_info(keys, Data)
    Data.append(newMember)

def del_member(keys, Data):
    """Search for row and delete selected row"""
    index = search(keys, Data)
    Data.remove(Data[index])

def edit_member(keys, Data):
    """Search for row and select value to edit"""
    print("\nSelect Member to edit: ", end='')
    mem = search(keys, Data)
    if(mem == -1):
        return
    for i, k in enumerate(keys):
        print("\t" + str(i+1).ljust(4) + k)
    select = int(input("\nSelect value to edit (1 through " + str(len(keys)) + ") or 0 to abort edit: "))
    if(select < 1 or select > len(keys)):
        return
    print(keys[int(select) - 1], " selected")
    newVal = input("Enter new Value: ")
    Data[mem].update({keys[select - 1]: newVal})

def print_membership(keys, Data):
    """Print pretty formatted table of values in list of dictionaries"""
    colWidth = colSize(keys, Data)
    print('\nResult:')
    for d in range(len(Data)):
        print('\n\t', end='')
        for i, k in enumerate(keys):
            print(Data[d][k].ljust(colWidth[i] + 2), end = ' ')
    print('\n\n')

def add_column(keys, Data):
    """Add new column with specified key at specified location in all dictionaries in list
    Function will prompt user for:
        new column label (key)
        position of new column in table
        default values for keys for all dictionaries in table. Dictionaries are updated
    """
    print("\n\t(0) ", end=' ')
    for i, k in enumerate(keys):
        print(k, "(%d)"%(i + 1), end=' ')
    newKey = input("\n\nEnter Column Label (no Spaces): ")
    default = input("\nEnter Default Value for new column: ")
    pos = input("\nSelect position for new column [0 through %d]: "% (len(keys)))
    for D in Data:
        D.update({newKey:default})
    keys.insert(int(pos), newKey)

def del_column(keys, Data):
    """Delete column selected by column label (key)"""
    print("\n\t", end=' ')
    for k in keys:
        print(k, end='  ')
    delKey = input("\n\nEnter Column Name: ")
    if (delKey in keys):
        for D in Data:
            D.pop(delKey)
        keys.remove(delKey)
    else:
        print("\nKey Not Found")

def search(keys, Data):
    """Search for dictionary according to specified string in selected key
    Prompts user for column to search (key)
    Prompts user for string or partial string to search for. (Case insensitive)
    Returns index of selected dictionary found in list of dictionaries
    """
    print('\n')
    for i, k in enumerate(keys):
        print("\t" + str(i+1).ljust(4) + k)
    select = int(input("\nSelect search criteria (1 through " + str(len(keys)) + ") Enter 0 to abort: "))
    if(select < 1 or select > len(keys)):
        return -1
    print(keys[select - 1], " selected")
    find = input("Enter " + keys[int(select) - 1] + " to search for: ")
    result = []
    for D in Data:
        if(find.upper() in D[keys[select - 1]].upper()):
            result.append(D)
    print("\nFound ", len(result), " results")
    print_membership(keys, result)
    chosenResult = input("Choose result id or 0 to abort search: ")
    for i, D in enumerate(Data):
        if(D['id'] == chosenResult):
            return i
    return -1

def look_up(keys, Data):
    """Use search function and print one line of formatted table"""
    mem = search(keys, Data)
    if(mem >= 0):
        for k in keys:
            print(Data[mem][k], end='   ')
    print('\n\n')

def quit(keys, Data):
    """Prompt user to save changes to file and Quit program"""
    save = input("Save Changes before quitting? [y,n]: ")
    if(save == 'y'):
        write_file(keys, Data)
    print("Thank You for using my Address Book\n")

def menu():
    """Display menu for user options"""
    print("\nOptions:\n\ta  = add member\n\td  = delete member\n\te  = edit member\n\tdc = delete column\n\t\
ac = add column\n\tp  = print membership\n\ts  = search\n\tw  = write file\n\tq  = quit\n")

def get_info(keys, Data):
    """Prompt user for all values to create a new dictionary and return dictionary"""
    info = {}
    Ind = max([int(k) for k in [Data[n]['id'] for n in range(len(Data))]]) + 1
    info['id'] = str(Ind)
    for k in keys[1:]:
        info[k] = input("Enter " + k + ": ")
    return info

def colSize(keys, Data):
    """Get list of maximum lengths of values for each key in all dictionaries"""
    cS = [max([len(Data[n][k]) for n in range(len(Data))]) for k in keys]
    # print("\nColumn Widths: ", cS)
    return cS

#------------------------------------------------------------------------------

Data = []
keys = []

opts = {'a': add_member, 'd': del_member, 'e': edit_member, 'dc': del_column,\
'ac': add_column, 'p': print_membership, 's': look_up, 'w': write_file, 'q': quit}

keys = read_file('addBook.csv', keys, Data)

print('\n\n')

menu()
choice = ' '
while(choice != 'q'):
    print("Input Options: ", list(opts.keys()))
    choice = input("Choose Option: ")
    if choice in list(opts.keys()):
        opts[choice](keys, Data)
    else:
        menu()

