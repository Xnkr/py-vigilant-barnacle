import re

def is_like(text,pattern):
    if '%' in pattern:
        pattern = pattern.replace('%','.*?')
    if re.match(pattern,text):
        return True
    return False
        

a = "This is another text here"
b = "This%another%here"
print(is_like(a,b))
a = "Thisis sometext"
b = "This % text"
print(is_like(a,b))
a = "Thisis sometext"
b = "This%text"
print(is_like(a,b))
a = "This is some text"
b = "This text"
print(is_like(a,b))
a = "This is some text yo"
b = "%text%"
print(is_like(a,b))