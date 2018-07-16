import json
string_block = ["work","twerk","learn"]

with open("newtest.txt","w+") as f:
    json.dump(string_block,f)

with open("newtest.txt","r") as f:
    data = json.load(f)
    print(type(data[2]))
    print(type(data))
f.close()

