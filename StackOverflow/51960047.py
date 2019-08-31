d = {'cat': 'Dog', 'Bird': 'Mouse'}
inp = 'There is a Cat,Bird'

for key,value in d.items():
  if key.lower() in inp:
    inp = inp.replace(key.lower(),value)
  if key in inp:
    inp = inp.replace(key,value)

print(inp)
'There is a Dog'