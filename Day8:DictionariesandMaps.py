phonebook = {}
num = int(input())
for i in range(0, num):
    entry = input()
    entry = entry.split()
    name = entry[0]
    number = entry[1]
    phonebook[entry[0]] = phonebook.get(name,number)



while 1:
    try:
        for i in range(0, num):
            name = input()
            if name in phonebook:
                print(name + "=" + str(phonebook[name]))
            else:
                print("Not found")
    except:
        break

