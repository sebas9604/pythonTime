from tkinter import *
#string concatenation
"""
youtuber = 'SebasLT'

print('Subscribe to ' + youtuber)
print('Subscribe to {}'.format(youtuber))
print(f'Subscribe to {youtuber}')"""


root = Tk()
root.geometry('300x300')
root.title('Titulo Madlib')
Label(root, text = 'Mi primer Madlib', font = 'arial 20 bold').pack()
Label(root, text = 'Selecciona:', font = 'arial 15 bold').place(x=40, y=80)

def madlib1():
    adj = input("Adjective: ")
    verb1 = input('Verb: ')
    verb2 = input('Verb: ')
    famous_person = input("Famous Person: ")

    madlib = f'Computer programming is so {adj}! It makes me so excited all the time because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!'

    print(madlib)

Button(root, text= 'The programming', font = 'arial 15', command=madlib1, bg = 'ghost white').place(x=60, y = 120)

root.mainloop()