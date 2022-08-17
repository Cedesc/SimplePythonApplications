import tkinter as tk
from tkinter import ttk

# https://www.youtube.com/watch?v=pezm8hRONgs


def main():
    # create main window
    root = tk.Tk()

    # adjust main window
    root.title("The Title")
    root.geometry("400x400")
    root.minsize(width=250, height=250)
    root.maxsize(width=600, height=600)
    root.resizable(width=False, height=True)

    # create widgets
    label1 = tk.Label(root, text="Label 1", bg="green")
    label2 = ttk.Label(root, text="Label 2")  # a ttk widget is a more detached from the rest of the code
    # add widgets to main window
    label1.pack(side="top", expand=True, fill="y")  # also possible for side is "bottom", "left", "right"
    label2.pack(side="top", expand=True, fill="x")  # also possible for fill is "both"

    # start event loop
    root.mainloop()

    # code execution after closing the window
    print("window has been closed")



if __name__ == '__main__':

    main()

    # test tkinter
    # tk._test()
