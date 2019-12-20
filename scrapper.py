#!/usr/bin/env python3
import requests as r
import json as j
import tkinter as tk

URL = "https://codeforces.com/api/user.info?handles="
CUI = False


def get_info(user):
    req = r.get(URL + user)
    json = j.loads(req.text)
    if json['status'] != 'OK':
        return None
    data = json['result'][0]
    return data['handle'], data['rating'], data['rank'], data['maxRating'], data['maxRank']


def gui():
    def search():
        info = get_info(text.get())
        text.set('')
        if info:
            i2.config(text=info[0])
            i3.config(text=info[1])
            i4.config(text=info[2])
            i5.config(text=info[3])
            i6.config(text=info[4])
        else:
            i2.config(text="User not found")
            i3.config(text="")
            i4.config(text="")
            i5.config(text="")
            i6.config(text="")

    root = tk.Tk()

    root.title("Codeforces User Scraper")
    root.geometry("275x150")
    root.resizable(True, False)

    label1 = tk.Label(root, text=' Username ')
    label1.grid(row=0, column=0)

    text = tk.StringVar()
    entry = tk.Entry(root, text="Username", textvariable=text)
    entry.bind("<Key>", func=lambda x: search() if x.keysym == "Return" else False)
    entry.grid(row=0, column=1)

    b = tk.Button(root, text="Find", command=search)
    b.grid(row=0, column=2)

    l2 = tk.Label(root, text="Handle")
    l3 = tk.Label(root, text="Rating")
    l4 = tk.Label(root, text="Rank")
    l5 = tk.Label(root, text="Max Rating")
    l6 = tk.Label(root, text="Max Rank")

    i2 = tk.Label(root, text="None")
    i3 = tk.Label(root, text="None")
    i4 = tk.Label(root, text="None")
    i5 = tk.Label(root, text="None")
    i6 = tk.Label(root, text="None")

    l2.grid(row=1, column=0)
    l3.grid(row=2, column=0)
    l4.grid(row=3, column=0)
    l5.grid(row=4, column=0)
    l6.grid(row=5, column=0)

    i2.grid(row=1, column=1)
    i3.grid(row=2, column=1)
    i4.grid(row=3, column=1)
    i5.grid(row=4, column=1)
    i6.grid(row=5, column=1)

    root.mainloop()


def cui():
    user = input("Username: ")
    info = get_info(user)
    if info:
        print("\nHandle: %s\nRating: %s\nRank: %s\nMax Rating: %s\nMax Rank: %s" % info)
    else:
        print("User %s not found." % user)


if __name__ == '__main__':
    if CUI:
        cui()
    else:
        gui()
