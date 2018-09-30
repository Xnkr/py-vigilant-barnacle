import re

rgx_list = ['Read More',
            'Read',
            'And follow us on Twitter to keep up with the latest news and and acute and primary Care.']

txt_path = 'newyorktimes_test.txt'

with open(txt_path) as new_txt_file:
    new_text = new_txt_file.read()

for rgx_match in rgx_list:
        new_text = re.sub(rgx_match, '', new_text)

#new_text.replace(txt_path, new_text)

print(new_text)