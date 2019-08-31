a_list = []
with open('53137975.txt') as f_obj:
    lines = f_obj.readlines()
    for line in lines:
        for char in line:
            if char != '\n':
                a_list.append(int(char))


print(a_list)
