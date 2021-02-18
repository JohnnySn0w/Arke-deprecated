from tkinter.ttk import Button, Label, Separator
from tkinter import N, NS, NW
from gui.style.styles import mainMenuStyles
from gui.main.workspace import mainWorkspace

from gui.lib.buttonFuncs import openFile, windowSwap


def mainMenu(root):
    # derive height and width from screen size
    height = int(root.winfo_screenheight() / 3)
    width = int(root.winfo_screenwidth() / 3)
    root.geometry(f"{width}x{height}")
    # derive origin offset to spawn window at center of screen
    xFromLeft = int(root.winfo_screenwidth() / 2 - width / 2)
    yFromTop = int(root.winfo_screenheight() / 2 - height / 2)
    root.geometry(f"+{xFromLeft}+{yFromTop}")
    root.resizable(False, False)
    root.title("Arke - Menu")

    # configure grid
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=4)
    root.grid_rowconfigure(6, weight=1)
    # root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=2)

    mainMenuStyles()

    name = Label(root, text="ARKE", font=("", 80), style="Name.TLabel")
    name.grid(row=1, column=0, columnspan=1, padx=10, pady=5)

    redbutton = Button(
        root,
        text="New",
        style="RedW.TButton",
        command=lambda: windowSwap(root, mainWorkspace),
    )
    redbutton.grid(row=2, column=0, sticky=N)
    bluebutton = Button(root, text="Open", style="BluW.TButton", command=openFile)
    bluebutton.grid(row=3, column=0)
    bluebutton = Button(root, text="Config", style="BluW.TButton")
    bluebutton.grid(row=4, column=0)
    blackbutton = Button(
        root, text="Exit", style="BlkW.TButton", command=root.destroy
    )
    blackbutton.grid(row=5, column=0)

    # middle
    divider = Separator(root, orient="vertical")
    divider.grid(row=1, column=1, sticky=NS, rowspan=5, padx=5, pady=5)
    # right side
    name = Label(root, text="Recents", font=("", 20), style="Recents.TLabel")
    name.grid(row=1, column=2, sticky=NW, padx=5, pady=5)
