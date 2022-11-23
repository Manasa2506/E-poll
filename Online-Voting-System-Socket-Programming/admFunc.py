import tkinter as tk
import dframe as df
from tkinter import *
from dframe import *
from PIL import ImageTk, Image


def resetAll(root, frame1):
    df.count_reset()
    df.reset_voter_list()
    df.reset_cand_list()
    Label(frame1, text="").grid(row=10, column=0)
    msg = Message(frame1, text="Reset Complete", width=500)
    msg.grid(row=11, column=0, columnspan=5)


def showVotes(root, frame1):

    result = df.show_result()
    root.title("Votes")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Vote Count", font=('Helvetica', 18, 'bold')).grid(
        row=0, column=1, rowspan=1)
    Label(frame1, text="").grid(row=1, column=0)

    vote = StringVar(frame1, "-1")

    Label(frame1, text="Machine Learning            :       ",
          font=('Helvetica', 12, 'bold')).grid(row=2, column=1)
    Label(frame1, text=result['a'], font=(
        'Helvetica', 12, 'bold')).grid(row=2, column=2)

    Label(frame1, text="Data Mining    :          ", font=(
        'Helvetica', 12, 'bold')).grid(row=3, column=1)
    Label(frame1, text=result['b'], font=(
        'Helvetica', 12, 'bold')).grid(row=3, column=2)

    Label(frame1, text="Data Science           :          ",
          font=('Helvetica', 12, 'bold')).grid(row=4, column=1)
    Label(frame1, text=result['c'], font=(
        'Helvetica', 12, 'bold')).grid(row=4, column=2)

    Label(frame1, text=" Data VIsualisation  :          ",
          font=('Helvetica', 12, 'bold')).grid(row=5, column=1)
    Label(frame1, text=result['d'], font=(
        'Helvetica', 12, 'bold')).grid(row=5, column=2)

    Label(frame1, text=" Data Warehousing    :          ",
          font=('Helvetica', 12, 'bold')).grid(row=6, column=1)
    Label(frame1, text=result['e'], font=(
        'Helvetica', 12, 'bold')).grid(row=6, column=2)

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
    #root = Tk()
    # root.geometry('500x500')
    #frame1 = Frame(root)
    #showVotes(root, frame1)
