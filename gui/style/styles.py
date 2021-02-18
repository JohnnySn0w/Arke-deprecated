from tkinter.ttk import Style

"""
Decorator that applies various styles
"""
# def implementStyles(styles):
#     style = Style()
#     styles(style)


def mainMenuStyles():
    styleRoot = Style()
    styleRoot.configure("BlkW.TButton", foreground="#666666")
    styleRoot.configure("RedW.TButton", foreground="#50AA90")
    styleRoot.configure("BluW.TButton", foreground="#4090BB")


def mainWorkspaceStyles():
    styleRoot = Style()
    styleRoot.configure("RedW.TFrame", background="white")
    styleRoot.configure("BluB.TFrame", background="black")
    styleRoot.configure("BwnW.TFrame", background="white")
