def bit_wise_and(n1,n2):
	n1_str = list(str(n1))[2:]
	n2_str = list(str(n2))[2:]
	result = ['0','b']
	n1_bit_len = len(n1_str)
	n2_bit_len = len(n2_str)
	if n1_bit_len!=n2_bit_len:
		if n1_bit_len>n2_bit_len:
			for i in range(n1_bit_len-n2_bit_len):
				n2_str.insert(2,'0')
		else:
			for i in range(n2_bit_len-n1_bit_len):
				n1_str.insert(2,'0')
	for a,b in zip(n1_str,n2_str):
		if a == '1' and b == '1':
			result.append('1')
		else:
			result.append('0')
	result_str = "".join(result)
	return bin(int(result_str,2))

print bit_wise_and(bin(10),bin(12))