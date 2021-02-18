from tkinter.ttk import Frame, Button
from tkinter import EW, N, Tk
from gui.style.styles import mainWorkspaceStyles
from gui.window.menu import windowMenu


def mainWorkspace(oldRoot):
    oldRoot.destroy()
    root = Tk()
    # derive height and width from screen size
    height = int(root.winfo_screenheight())
    width = int(root.winfo_screenwidth())
    root.geometry(f"{width}x{height}")
    root.resizable(True, True)
    root.title("Arke - Workspace - FILENAMEHERELATER")

    # configure grid
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=6)
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(1, weight=2)

    mainWorkspaceStyles()
    topMenu = Frame(root, style="RedW.TFrame")
    topMenu.grid(row=0, column=0, sticky=N, columnspan=3)
    windowMenu(root)

    workspaceArea = Frame(root, style="BluB.TFrame")
    workspaceArea.grid(row=1, sticky=EW, columnspan=2)

    bottomStatus = Frame(root, style="BwnW.TFrame")
    bottomStatus.grid(row=2, column=0, sticky=EW, columnspan=3)
