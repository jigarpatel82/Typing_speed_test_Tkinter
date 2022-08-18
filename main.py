import random
from tkinter import *

# Creating list of words from para
para = "this is a simple paragraph that is meant to be nice and easy to type which is why there will be mommas no " \
            "periods or any capital letters so i guess this means that it cannot really be considered a paragraph but " \
            "just a series of run on sentences this should help you get faster at typing as im trying not " \
            "to use too many difficult words in it although i think that i might start making it hard by including some " \
            "more difficult letters typing pretty quickly so forgive me for any mistakes i think that i will not " \
            "just tell you a story about the time i went to the zoo and found"
test_para = para.split(' ')

# Creating Tkinter window
window = Tk()
window.title('Typing Test')
window.geometry('550x400')
window.configure(pady=70, bg='#445552')

# Global variables
test_label = None
user_entry = None
timer_label = None
timer_time = 60
word_count = 0
wrong_count = 0


# FUNCTIONS
def get_test_word():
    """Get the word to test user against from list of words"""
    return random.choice(test_para)

def layout():
    """Layout of the tkinter window"""
    instructions = 'Type the word as shown into the input field.\n' \
                   'After finished, press spacebar to move to another word.\nPress Start button to start timer\n' \
                   'HAPPY TYPING!'
    instructions_label = Label(frame, text=instructions, bg='#A799B7', font=("Courier New", 15))
    instructions_label.grid(column=0, row=0)
    global test_label
    test_label = Label(frame, text=get_test_word(), bg='#445552', font=("Courier", 30))
    test_label.grid(column=0, row=2)
    global user_entry
    user_entry = Entry(frame, bg='#A799B7', bd=5, width=40)
    user_entry.focus_set()
    user_entry.grid(column=0, row=3)
    btn = Button(frame, text='Start', command=update_timer, borderwidth=0)
    btn.grid(column=0, row=4)
    window.bind('<space>', lambda i: check_input(i))

def remove_label_text():
    """Removing test label text"""
    global test_label
    test_label.config(text='')

def check_input(event):
    """Check input of the test label text against user text"""
    global test_label
    test_label_text = test_label.cget('text')
    global user_entry
    user_text = user_entry.get()
    print(f'label text: {test_label_text}')
    print(user_text)
    print(f'event char: {event.char}')
    if test_label_text == user_text.strip():
        print('Text matched')
        global word_count
        word_count += 1
        user_entry.delete(0, END)
        remove_label_text()
        layout()
    else:
        print(test_label_text)
        global wrong_count
        wrong_count += 1
        remove_label_text()
        layout()

def update_timer():
    """Shows timer on screen"""
    global timer_time
    if timer_time > 0:
        timer_time -= 1
        global timer_label
        timer_label = Label(frame, text=f'00:{timer_time}', font=("Courier New", 20), bg='#445552')
        timer_label.grid(row=1, column=0)
        window.after(1000, update_timer)
    elif timer_time == 0:
        score()

def score():
    global timer_label
    timer_label.config(text='')
    timer_label.config(text=f'Your wpm is {word_count} and you got {wrong_count} words wrong', bg='#445552', font=("Ariel", 15))

# Creating canvas and labelframe
canvas1 = Canvas(window)
canvas1.pack()
frame = LabelFrame(canvas1, text='Typing Speed Test', bg='#445552', font=("Ariel", 20, 'bold'))
frame.pack()

# Run layout function to set up elements on screen
layout()
window.bind('<space>', lambda i: check_input(i))

window.mainloop()

