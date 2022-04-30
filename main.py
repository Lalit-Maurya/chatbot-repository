import tkinter as tk
from chatbot import get_response

root = tk.Tk()
root.geometry('484x603')
root.configure(background = 'black')
root.resizable(False, False)

background = tk.PhotoImage(file = 'utils/gradient.png')
background_label = tk.Label(root, image = background)
background_label.place(x = -3, y = 0)

def chatbot_window():

    chatbot_win = tk.Toplevel(root)
    chatbot_win.geometry('690x850')
    chatbot_win.title('Chatbot')
    chatbot_win.resizable(False, False)

    def submit():
        input = user_input_label.get()

        user_input_label.delete(0,tk.END)

        if input == '':
            chat_history_listbox.insert(tk.END,  f'Bot : Please enter something into the entry box')
            return

        chat_history_listbox.insert(tk.END, f'You : {input}')
        chat_history_listbox.insert(tk.END, f'Bot : {get_response(input)}')

    user_input_label = tk.Entry(chatbot_win, width=100)
    user_input_label.place(x = 10, y = 10)

    submit_button = tk.Button(chatbot_win, text = 'Submit', command = submit, font = ('Courier New',9, 'bold'))
    submit_button.place(x = 616, y = 5)

    scroll = tk.Scrollbar(chatbot_win)
    scroll.pack(side = tk.RIGHT, fill = tk.Y)

    chat_history_listbox = tk.Listbox(chatbot_win, yscrollcommand=scroll.set,height=50, width=109)
    chat_history_listbox.place(x = 10, y = 35)

    scroll.config(command = chat_history_listbox.yview)

def close_window():
    root.destroy()

title_label = tk.Label(root, text = 'Capstone Project', font = ('DejaVu Sans', 45), bg= 'black', fg = 'white')
title_label.pack(pady=10)

chatbot_button = tk.Button(root, text = 'Chatbot', font = ('DejaVu Sans', 25), bg = 'black', fg = 'white', command=chatbot_window, relief = tk.FLAT)
chatbot_button.pack(pady=50)


exit_button = tk.Button(root, text = 'Exit',font = ('DejaVu Sans', 25), bg = 'black', fg = 'white', command = close_window, relief = tk.FLAT)
exit_button.pack()

root.mainloop()
