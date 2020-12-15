from tkinter import *
from tkinter import messagebox
from PIL import Image
from playsound import playsound

root = Tk()
root.title("Bar Simulator")

frame = Frame(root)
frame.pack()

canvas = Canvas(frame, bg="black", width=1500, height=800)
canvas.pack()
canvas

background = PhotoImage(file='C:/Python/bar game/bar2.png')
canvas.create_image(750, 0, anchor='n', image=background)

beer = PhotoImage(file='C:/Python/bar game/beer.png')
cola = PhotoImage(file='C:/Python/bar game/cola.png')
wine = PhotoImage(file='C:/Python/bar game/wine.png')
whiskey = PhotoImage(file='C:/Python/bar game/whiskey.png')

title = Label(frame, text='Welcome to the Bar!', bg='brown', font=('arial 30 bold'))
title.place(relx=0.345, rely=0.01)
subtitle = Label(frame, text='What would you like to drink?', bg='brown', font='arial 20 bold')
subtitle.place(relx=0.35, rely=0.1)


def beer_drink():
    msg = messagebox.askquestion('Age warning', 'Are you over 18?')
    if msg == 'yes':
        messagebox.showinfo('Age warning', 'Enjoy your drink!')
        canvas.create_image(180, 458, anchor='w', image=beer)
        playsound('./sounds/beer.mp3')
    else:
        messagebox.showinfo('Age warning', 'You are to young to drink!\nWhy not drink a cola instead?')
        canvas.create_image(180, 310, anchor='w', image=cola)
        playsound('./sounds/cola.mp3')


def wine_drink():
    msg = messagebox.askquestion('Age warning', 'Are you over 18?')
    if msg == 'yes':
        messagebox.showinfo('Age warning', 'Enjoy your drink!')
        canvas.create_image(530, 450, image=wine)
        playsound('./sounds/wine.mp3')

    else:
        messagebox.showinfo('Age warning', 'You are to young to drink!\nWhy not drink a cola instead?')
        canvas.create_image(480, 310, anchor='w', image=cola)
        playsound('./sounds/cola.mp3')


def whiskey_drink():
    msg = messagebox.askquestion('Age warning', 'Are you over 18?')
    if msg == 'yes':
        messagebox.showinfo('Age warning', 'Enjoy your drink!')
        canvas.create_image(840, 495, image=whiskey)
        playsound('./sounds/whiskey.mp3')
    else:
        messagebox.showinfo('Age warning', 'You are to young to drink!\nWhy not drink a cola instead?')
        canvas.create_image(800, 310, anchor='w', image=cola)
        playsound('./sounds/cola.mp3')


def cola_drink():
    messagebox.showinfo('Drink', 'Enjoy your drink!')
    canvas.create_image(1080, 310, anchor='w', image=cola)
    playsound('./sounds/cola.mp3')


beer_button = Button(frame, text='Beer', cursor='hand2', bg='yellow', command=beer_drink, bd=5, width=10, fg='orange', font='arial 15 bold')
beer_button.place(relx=0.1, rely=0.2)
wine_button = Button(frame, text='Wine', cursor='hand2', bg='#C70039', command=wine_drink, bd=5, width=10, fg='white', font='arial 15 bold')
wine_button.place(relx=0.3, rely=0.2)
Whiskey_button = Button(frame, text='Whiskey', cursor='hand2', bg='#C96819', command=whiskey_drink, bd=7, width=10, fg='white', font='arial 15 bold')
Whiskey_button.place(relx=0.5, rely=0.2)
cola_button = Button(frame, text='Cola', cursor='hand2', bg='red', command=cola_drink, bd=6, width=10, fg='black', font='arial 15 bold')
cola_button.place(relx=0.7, rely=0.2)


root.mainloop()
