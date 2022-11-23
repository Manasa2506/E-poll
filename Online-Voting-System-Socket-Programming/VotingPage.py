import tkinter as tk
import socket
from tkinter import *
from PIL import ImageTk, Image


def voteCast(root, frame1, vote, client_socket):

    for widget in frame1.winfo_children():
        widget.destroy()

    client_socket.send(vote.encode())  # 4

    message = client_socket.recv(1024)  # Success message
    print(message.decode())  # 5
    message = message.decode()
    if(message == "Successful"):
        Label(frame1, text="Vote Casted Successfully", font=(
            'Helvetica', 18, 'bold')).grid(row=1, column=1)
    else:
        Label(frame1, text="Vote Cast Failed... \nTry again",
              font=('Helvetica', 18, 'bold')).grid(row=1, column=1)

    client_socket.close()


def votingPg(root, frame1, client_socket):

    root.title("PROFESSIONAL ELECTIVE")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="SELECT THE PROFESSIONAL ELECTIVE", font=(
        'Helvetica', 18, 'bold')).grid(row=0, column=1, rowspan=1)
    Label(frame1, text="").grid(row=1, column=0)

    vote = StringVar(frame1, "-1")

    Radiobutton(frame1, text="Machine Learning", variable=vote, value="a", indicator=0, height=4,
                width=15, command=lambda: voteCast(root, frame1, "a", client_socket)).grid(row=2, column=1)

    Radiobutton(frame1, text="Data Mining", variable=vote, value="b", indicator=0, height=4,
                width=15, command=lambda: voteCast(root, frame1, "b", client_socket)).grid(row=3, column=1)

    Radiobutton(frame1, text="Data Science", variable=vote, value="c", indicator=0, height=4,
                width=15, command=lambda: voteCast(root, frame1, "c", client_socket)).grid(row=4, column=1)

    Radiobutton(frame1, text="Data Visualization", variable=vote, value="d", indicator=0, height=4,
                width=15, command=lambda: voteCast(root, frame1, "d", client_socket)).grid(row=5, column=1)

    Radiobutton(frame1, text="Data warehousing", variable=vote, value="e", indicator=0, height=4,
                width=15, command=lambda: voteCast(root, frame1, "e", client_socket)).grid(row=6, column=1)

    frame1.pack()
    root.mainloop()


if __name__ == "__main__":
    root = Tk()
    root.geometry('500x500')
    frame1 = Frame(root)
    client_socket = 'Fail'
    votingPg(root, frame1, client_socket)
