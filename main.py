import tkinter as tk
from pytube import YouTube

root = tk.Tk()
root.geometry('600x600')
root.resizable(0, 0)
root.title('YouTube Video Downloader')


def download():
    link = link_entry.get()
    video = YouTube(link)
    video_stream = video.streams.filter(
        progressive=True).order_by('resolution').desc().first()
    video_stream.download()
    tk.Label(root, text='Downloaded successfully!',
             font='arial 15').place(x=100, y=120)


label = tk.Label(root, text='YouTube Video Downloader',
                 font='san-serif 14 bold')
label.pack()

link_label = tk.Label(
    root, text='Please paste your link here', font='san-serif 16 bold')
link_label.place(x=150, y=55)

link_entry = tk.Entry(root, width=80)
link_entry.place(x=30, y=85)

download_button = tk.Button(root, text='Download', font='san-serif 16 bold',
                            bg='red', padx=2, command=download)
download_button.place(x=100, y=150)

root.mainloop()
