# s = "abba"
# n = 2
# c = 2

# l_s = []

# for i in range(0,len(s)-n+1):
# 	temp = s[i:i+n]
# 	if temp not in l_s:
# 		l_s.append(s[i:i+n])

# print (l_s)

# # erlin and substrings
# s = 'abcd'
# l_s = []
# for n in range(1,len(s)+1):
# 	for i in range(0,len(s)-n+1):
# 		temp = s[i:i+n]
# 		if temp not in l_s:
# 			l_s.append(temp)

# print len(l_s)

# # jimmy quest
# l_n = [-1,1,2,-3,4]
# l_n_idx = [x for x in range(len(l_n))]
# l_neg_idx = [x for x in l_n_idx if l_n[x]<0]

# res_idx = []

# for i in l_n_idx:
# 	diff = []
# 	for j in l_neg_idx:
# 		diff.append(abs(i-j))
# 	res_idx.append(min(diff))
# print res_idx

# # Common prefix

# a = "sky is blue"
# b = "sky is dark"

# common_pref = ""

# for a_c,b_c in zip((a),(b)):
# 	if a_c == b_c:
# 		common_pref+=a_c
# 	else:
# 		break

# if not common_pref:
# 	print "No prefix"
# else:
# 	print common_pref

# # long number
# def bubblesort( A ,B):
# 	for i in range( len( A ) ):
# 		for k in range( len( A ) - 1, i, -1 ):
# 			if ( A[k] > A[k - 1] ):
# 			      swap( A, k, k - 1 )
# 			      swap (B, k, k-1)
# 	return A,B
 
# def swap( A, x, y ):
#   tmp = A[x]
#   A[x] = A[y]
#   A[y] = tmp

# inp_str = list(map(str,[9,5,30,3,34]))
# res = []

# inp_str = sorted(inp_str)[::-1]
# added_count = []
# max_len_items = max([len(val) for val in inp_str])

# for val in inp_str:
# 	temp = 0
# 	while len(val) < max_len_items:
# 		val += val[len(val)-1]
# 		temp += 1
# 	added_count.append(temp)
# 	res.append(val)

# res, added_count = bubblesort(res,added_count)

# for i in range(len(res)):
# 	res[i] = res[i][:len(res[i])-added_count[i]]

# print "".join(res)

# # make palin

# inp_str = "xyx/yxy/"
# xcost = 4
# ycost = 6
# tcost = 0
# len_of_str = len(inp_str)
# for i in range(len_of_str/2):
# 	if inp_str[i] == '/':
# 		if inp_str[len_of_str-i-1] == 'x':
# 			tcost += xcost
# 		else:
# 			tcost += ycost
# 	if inp_str[len_of_str-i-1] == '/':
# 		if inp_str[i] == 'x':
# 			tcost += xcost
# 		else:
# 			tcost += ycost

# print tcost


# # printing sheets

# inp = 7

# if inp%3 == 0 or inp%2 ==0:
# 	res = "yes"
# else: 
# 	res = "no"

# print res

# Remove dup char

# def remove_dup(_str):
# 	for i in range(len(_str)):
# 		while _str[i-1] == _str[i] and i < len(_str)-1:
# 			print _str[i] , 
# 			i+=1



# inp_str = "caaabbbaacdddd"

# print inp_str.replace('a','')
# remove_dup(inp_str)

