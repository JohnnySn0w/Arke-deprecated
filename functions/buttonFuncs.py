from tkinter.tix import ExFileSelectBox
def openFile(root):
    pass

def windowSwap(root, newWindow):
    newWindow(root)

def openFile(root, pathName='~'):
    window = ExFileSelectBox(root, pathName='~')

def donothing():
    pass

def close():
    pass

def exitCheck():
    pass