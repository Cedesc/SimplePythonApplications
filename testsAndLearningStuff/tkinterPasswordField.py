from tkinter import *
from tkinter import ttk


def main():

    # Create an instance of tkinter frame or window
    win = Tk()

    # Set the size of the window
    win.geometry("200x100")

    # Define a function to show the entered password
    def show(_):
        p = password.get()
        ttk.Label(win, text="Your Password is: " + str(p)).pack()

    password = StringVar()

    # Add an Entry widget for accepting User Password
    entry = Entry(win, width=25, textvariable=password, show="*")
    entry.pack(pady=10)

    # Use Return Key for triggering the password showing
    win.bind("<Return>", show)

    win.mainloop()


if __name__ == '__main__':
    main()
