from random import randrange

def gen_ran_string(best_match, match_idx):
	char_list = list(map(chr, range(97,123))) + [' ']
	gen_list = []
	for _ in range(len(char_list)+1):
		if _ in match_idx:
			gen_list.append(best_match[_])
		else:
			gen_list.append(char_list[randrange(len(char_list))])
	return gen_list

def score_str(gen_list,goal):
	match = 0
	match_idx = []
	for idx in range(len(goal)):
		if goal[idx] == gen_list[idx]:
			match+=1
			match_idx.append(idx)
	return match, match_idx
	
goal = list("methinks it is like a weasel")
min_iter_req = 100
for _ in xrange(10):
	iter_count = 0
	max_match = 0
	best_match = gen_ran_string("",[])
	match_idx = []
	while True:
		iter_count += 1
		gen_list = gen_ran_string(best_match,match_idx)
		match, match_idx = score_str(gen_list,goal)
		if match == len(goal):
			break
		if match > max_match:
			max_match = match
			best_match = gen_list		
	if iter_count < min_iter_req:
		min_iter_req = iter_count

print "%d is the minimum iteration required when tested over 10 iterations" %(min_iter_req)