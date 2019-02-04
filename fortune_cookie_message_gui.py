from random import choice
from tkinter import *
import tkinter.messagebox


class FortuneCookieFrame:
    def __init__(self, master):
        frame = Frame(master)
        frame.grid()


        # Display GUI framework
        title = Label(frame, text="Open a cookie for a fortune.")
        title.grid(row=0, columnspan=2, sticky=W)

        open_cookie = Label(frame, text="Want a Fortune Cookie? :    ")
        open_cookie.grid(row=1, column=0, sticky=W)


        self.print_button = Button(frame, text="Open", fg="blue", command=self.print_message)
        self.print_button.grid(row=1, column=1, sticky=W)

        # Fortune cookie messages
        self.fortune_message = ["Today it's up to you to create the peacefulness you long for.",
                                "A friend asks only for your time not your money.",
                                "If you refuse to accept anything but the best, you very often get it.",
                                "A smile is your passport into the hearts of others.",
                                "A good way to keep healthy is to eat more Chinese food.",
                                "Your high-minded principles spell success.",
                                "Hard work pays off in the future, laziness pays off now.",
                                "Change can hurt, but it leads a path to something better.",
                                "Enjoy the good luck a companion brings you.",
                                "People are naturally attracted to you.",
                                "A chance meeting opens new doors to success and friendship."]
        
        # Random message selected
        self.random_message = choice(self.fortune_message)


    # Message box of the fortune message
    def print_message(self):
            tkinter.messagebox.showinfo("Fortune Message", self.random_message)
            self.random_message = choice(self.fortune_message)

root = Tk()
root.title("Fortune Cookie Message")

open_fortune = FortuneCookieFrame(root)
root.mainloop()