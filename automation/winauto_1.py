from pywinauto.application import Application

app = Application().start("notepad.exe")
app.UntitledNotepad.Edit.type_keys("Work!")
app.UntitledNotepad.close()
app.Notepad.Cancel.click()
