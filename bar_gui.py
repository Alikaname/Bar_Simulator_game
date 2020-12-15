from tkinter import *
from tkinter import messagebox
from PIL import Image


window = Tk()
window.geometry('1500x800')
window.resizable(1, 1)
window.config()
window.title('Bar simulator')


bg = PhotoImage(file='C:/Python/bar game/bar2.png')
bg_label = Label(window, image=bg)
bg_label.place(relwidth=1, relheight=1)

# frame = Frame(window)
# frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')


canvas = Canvas(window)
canvas.place()

# canvas.create_image(anchor='n', image=bg)


beer = PhotoImage(file='C:/Python/bar game/beer.png')
beer_img = canvas.create_image(10, 10, image=beer)


# canvas.create_image(30, 30, image=beer)


title = Label(window, text='Welcome to the Bar!', bg='brown', font=('arial 30 bold'))
title.place(relx=0.345)
subtitle = Label(window, text='What would you like to drink?', bg='brown', font='arial 20 bold')
subtitle.place(relx=0.35, rely=0.1)
entry = Entry(window, bg='white')
# entry.place(relx=0.5, rely=0.5)


def alcohol():
    msg = messagebox.askquestion('Age warning', 'Are you over 18?')
    if msg == 'yes':
        messagebox.showinfo('Age warning', 'enjoy your drink!')
        # return canvas.create_image(500, 500, anchor='w', image=beer)
    else:
        messagebox.showinfo('Age warning', 'You are to old to drink!')


beer_button = Button(window, text='Beer', cursor='hand2', bg='yellow', command=alcohol, bd=5, width=10, fg='orange', font='arial 15 bold')
beer_button.place(relx=0.1, rely=0.2)
wine_button = Button(window, text='Wine', cursor='hand2', bg='#C70039', command=alcohol, bd=5, width=10, fg='white', font='arial 15 bold')
wine_button.place(relx=0.3, rely=0.2)
vodka_button = Button(window, text='Vodka', cursor='hand2', bg='blue', command=alcohol, bd=5, width=10, fg='white', font='arial 15 bold')
vodka_button.place(relx=0.5, rely=0.2)
sake_button = Button(window, text='Sake', cursor='hand2', bg='white', command=alcohol, bd=6, width=10, fg='blue', font='arial 15 bold')
sake_button.place(relx=0.7, rely=0.2)


window.mainloop()
