from tkinter.ttk import dr

'''
might wanna remake this, it seems like it's almost functional anyways
'''
class DragManager():
    def add_dragable(self, widget):
        widget.bind("<ButtonPress-1>", self.on_start)
        widget.bind("<B1-Motion>", self.on_drag)
        widget.bind("<ButtonRelease-1>", self.on_drop)
        widget.configure(cursor="hand1")

    def _on_start(self, event):
        # you could use this method to create a floating window
        # that represents what is being dragged.
        pass

    def _on_drag(self, event):
        # you could use this method to move a floating window that
        # represents what you're dragging
        pass

    def _on_drop(self, event):
        # find the widget under the cursor
        x,y = event.widget.winfo_pointerxy()
        target = event.widget.winfo_containing(x,y)
        try:
            target.configure(image=event.widget.cget("image"))
        except:
            pass
