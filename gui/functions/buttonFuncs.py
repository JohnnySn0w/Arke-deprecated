from tkinter.tix import FileSelectBox
def openFile(root):
    pass

def windowSwap(root, newWindow):
    newWindow(root)

def openFile():
    window = FileSelectBox(root, pathName='~')
