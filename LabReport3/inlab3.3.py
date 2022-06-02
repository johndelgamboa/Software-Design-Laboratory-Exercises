def display(hashTable):
    for i in range(len(hashTable)):
        print(i, end=" ")

        for j in hashTable[i]:
            print("-->", end=" ")
            print(j, end=" ")

        print()


HashTable = [[] for _ in range(10)]


def Hashing(keyvalue):
    return keyvalue % len(HashTable)


def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)


print("")
insert(HashTable, 3, 'Python')
insert(HashTable, 17, 'Data')
insert(HashTable, 44, 'Code')
insert(HashTable, 3, 'Hash')
insert(HashTable, 25, 'Algorithm')
insert(HashTable, 25, 'Computer')
insert(HashTable, 3, 'Separate')
display(HashTable)
print("")
