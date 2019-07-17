def check_string(s):
    for item in s.split(','):
        if item.count('[') > 1:
            print(item, s.index(item))
            return False
    return True

bad = '[[12.12345678,12.12345678],[12.12[12.12345678,12.12345678],[12.12345678,12.12345678]]'[1:-1]
good = '[[12.12345678,12.12345678],[12.12345678,12.12345678],[12.12345678,12.12345678]]'[1:-1]

# print(check_string(bad))
# print(check_string(good))

with open('52147762.csv') as file_obj:
    lines = file_obj.readlines()
    for line in lines:
        check_string(line[1:-1])


