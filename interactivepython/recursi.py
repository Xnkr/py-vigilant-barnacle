
def revstr(instr):
	if len(instr) == 1:
		return instr
	else:
		return instr[len(instr)-1:]+revstr(instr[:len(instr)-1])

print revstr(list("1234"))

def palinchk(instr):
	if len(instr) <= 1:
		return True
	else:
		if instr[0] != instr[len(instr)-1]:
			return False
		else:
			return palinchk(instr[1:len(instr)-1])

rep_list = [',','/','\\','"',';',':','.','\'',' ','-']
inpstr = "Wassamassaw".lower()
for rep in rep_list:
	inpstr = inpstr.replace(rep,"")

print inpstr, palinchk(inpstr)
