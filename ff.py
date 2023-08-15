import tkinter
import pyshorteners


def shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(longurl_entry.get())
    print(shorturl_entry.insert(0, short_url))


root = tkinter.Tk()
root.title("URL Shortener")
root.geometry("300x150")

big_label_font=("Helvetica",16,"bold")

longurl_label = tkinter.Label(root,font=big_label_font, text="Enter Long URL")
longurl_entry = tkinter.Entry(root)
shorturl_label = tkinter.Label(root,font=big_label_font, text="Output shortened URL")
shorturl_entry = tkinter.Entry(root)
shorten_button = tkinter.Button(root, text="Shorten URL", command=shorten)

longurl_label.pack()
longurl_entry.pack()
shorturl_label.pack()
shorturl_entry.pack()
shorten_button.pack()

root.mainloop()

