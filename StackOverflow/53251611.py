def main():
    try:
        user_number = str(input('Enter a phone number (XXX-XXX-XXXX): ')).upper()
        converted_number = check_number(user_number)
        print('The phone number is:',converted_number)
    except Exception as err:
        print(err)

def check_number(user_number):
    try:
        r = []
        for char in user_number:
            if char.isalpha():
                result = convert_to_num(char)
                r.append(str(result))
            else:
                r.append(char)
        return "".join(r)
    except Exception as err:
        print(err)

def convert_to_num(char):
    if char in ['A','B','C']:
        char = 2
    elif char in ['D','E','F']:
        char = 3
    elif char in ['G','H','I']:
        char = 4
    elif char in ['J','K','L']:
        char = 5
    elif char in ['M','N','O']:
        char = 6
    elif char in ['P','Q','R','S']:
        char = 7
    elif char in ['T','U','V']:
        char = 8
    elif char in ['W','X','Y','Z']:
        char = 9
    return char
main()