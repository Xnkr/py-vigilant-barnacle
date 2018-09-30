import re


test_string = '[<em class="letter" id="infoJiga">3,402,000</em>]'
pattern = re.compile('([\d,]*)')
result = pattern.search(test_string)

if result:
	# Comma separated
	print(result)

	# Comma removed int
	# print(int(result.group(1).replace(',','')))


