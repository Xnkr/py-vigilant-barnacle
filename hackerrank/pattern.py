""" 
+--+--+
-  -  -
-  -  -
+--+--+
-  -  -
-  -  -
+--+--+

"""

# for i in range(7):
# 	for j in range(7):
# 		if i in [0,3,6] and j in [0,3,6]:
# 			print "+",
# 		elif i in [0,3,6] or j in [0,3,6]:
# 			print "-",
# 		else:
# 			print " ",
# 	print

def distance(x1,y1,x2,y2):
	return ((x2-x1)**2 + (y2-y1)**2)**0.5

center = (40,40)
for i in range(100):
	for j in range(100):
		dist = distance(i,j,center[0],center[1])
		if dist<=30:
			print "+",
		else:
			print " ",
	print