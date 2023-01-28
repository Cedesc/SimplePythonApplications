from tkinter import Tk, StringVar, Entry
from pyperclip import copy


def main():

    # clear the entry content and clipboard, destroy the whole window
    def clear_and_destroy() -> None:
        entry_content.set("")
        copy('')
        win.destroy()


    # define a function to show the entered password
    def decrypt() -> None:

        # get the input
        pw = entry_content.get()
        # cast to bytes
        pw_bytes = bytes(pw, "UTF-8")

        # if input is empty, clear clipboard and destroy the window
        if pw_bytes == b'':
            clear_and_destroy()
            return
        else:
            # stretch the input minimum to the length of the data
            while len(pw_bytes) < len(data):
                pw_bytes *= 2

            # decrypt
            result: str = bytes(a ^ b for (a, b) in zip(pw_bytes, data)).decode('utf-8')
            # copy to clipboard
            copy(result)
            # clear content of entry
            entry_content.set("")

    # read and save the data
    with open('dataForGetMaster.txt') as f:
        data: bytes = bytes(f.readlines()[0], "UTF-8")

    # create an instance of tkinter window
    win = Tk()

    # set the size of the window
    win.geometry("300x100")

    # add an entry widget for accepting user password
    entry_content = StringVar()
    entry = Entry(win, width=40, textvariable=entry_content, show="*")
    entry.pack(pady=10)
    # autofocus on entry
    entry.focus()

    # bind "Return" to the function
    win.bind("<Return>", lambda _: decrypt())
    # bind "Escape" to destroying the window
    win.bind("<Escape>", lambda _: clear_and_destroy())

    # "overwrite" the red x button for closing the window
    win.protocol("WM_DELETE_WINDOW", clear_and_destroy)

    win.mainloop()


if __name__ == '__main__':
    main()
