

records = {}

n = int(input())

for i in range(0,n):
    entry = str(input()).split(" ")
    name = entry[0]
    phonenumber = int(entry[1])
    records[name]= phonenumber

for i in range(0,n):
    x =str(input())
    if x in records:
        print(x + '=' + str(records[name]))
else :
    print("Not found")
