import json

data = {}
#print("Enter Company Name")
name = raw_input("Enter Company Name")
print(name)

data['config'] = []

data['config'].append({
    'CompanyName': name
})

with open('config.json', 'w') as outfile:
    json.dump(data, outfile)