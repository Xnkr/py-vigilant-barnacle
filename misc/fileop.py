import re

file = open('Sample.java','r')
op = open('result.java','w')

for lines in file.readlines():
	if "Throwable" in lines:
		func_name = re.search(r'void (.*) throws',lines,re.IGNORECASE)
		op.write(lines.replace("Throwable","SRKayCGCoreUIException"))
		op.write("logger.info(LogConstant.ENTER + \""+func_name.group(1)+"\"); try {  } catch (Exception e) {   logger.debug(LogConstant.EXCEPTION + \"in "+func_name.group(1)+"\"); }  logger.info(LogConstant.EXIT + \""+func_name.group(1)+"\");")
	elif "throw new PendingException()" in lines:
		op.write("")
	else:
		op.write(lines)	

file.close()
op.close()