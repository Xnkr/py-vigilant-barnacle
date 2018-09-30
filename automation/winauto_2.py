from pywinauto.application import Application
import pywinauto
from random import randint


# app = Application().start("C:\\Users\\Shankar\\Documents\\Visual Studio 2015\\Projects\\AppToTest\\AppToTest\\bin\\Release\\AppToTest.exe")

# for _ in range(1,10):
# 	app.Form1.Edit3.SetEditText('')
# 	app.Form1.Edit2.SetEditText('')
# 	num = randint(1,100)
# 	app.Form1.Edit3.type_keys(num)
# 	numo = num
# 	num = randint(1,100)
# 	app.Form1.Edit2.type_keys(num)
# 	app.Form1.AddButton.click()
# 	res = app.Form1.Edit0.WindowText()
# 	if int(res) == numo + num:
# 		print numo, num, int(res)
# app.Form1.close()

app = Application(backend='uia').start("C:\\Users\\Shankar\\Documents\\Visual Studio 2015\\Projects\\WpfApplication2\\WpfApplication2\\bin\\Debug\\WpfApplication2.exe")

print app.window(auto_id='button', control_type='Button').print_control_identifiers()
