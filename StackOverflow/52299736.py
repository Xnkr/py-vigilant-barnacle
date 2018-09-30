import csv

d = {}
headers = []
with open('52299736.csv') as file_obj:
    reader = csv.reader(file_obj)
    for header in next(reader):
        headers.append(header)
        d[header] = []
    for line in reader:
        for idx,element in enumerate(line):
            d[headers[idx]].append(element)

print(d)
print(d['IAGE0'][0])
print(d['IAGE15'][0])

d = {}
headers = []
with open('52299736.csv') as file_obj:
    reader = csv.DictReader(file_obj)
    for line in reader:
        for key,value in line.items():
            if key not in d:
                d[key] = [value]
            else:
                d[key].append(value)


print(d)
print(d['IAGE0'][0])
print(d['IAGE15'][0])