import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from random import randint

# widgets
# frame
# setting relief='flat'
# .bind(<Button-1> 2 3)
# entries
# .get() method
# label.config
# .bind('<Button-1>',callback)
# messagebox.showinfo('Search Result','this is the result')


# callback functions
def handleextract():
    data = text.get('1.0', 'end-1c')
    res = dictfile(data)
    if res:
        window2(res)


def handleupload():
    dirr = filedialog.askopenfilename(
        title='Open Text File', filetypes=(('Text Files', '*.txt'),))
# reading and inserting the text from the file into the text view
    with open(dirr, 'r+') as file:
        data = file.read()
        text.insert('1.0', data)


def dictfile(stringdata):
    res = {}
    index = 0
    data = stringdata.replace('\n', ' ').split(' ')
    keys = set(data)
    if('' in keys):
        keys.remove('')
    for k in keys:
        res[k] = [0, 0]
        res[k][1] = index
        index += 1
        for it in data:
            if(k == it):
                res[k][0] += 1
    print(res)
    return res


def handleclearinput():
    text.delete('1.0', 'end-1c')


# second window
def window2(data):
    window = tkinter.Tk()
    window.title('Search Result')
    window.geometry('700x700')
    window.resizable(0, 0)
    window.configure(bg='black')

    def handlesearch():
        searchword = entry1.get()
        print(searchword)

        words = data.keys()
        print(words)

        if searchword in words:
            count = data[searchword][0]
            messagebox.showinfo(
                'Search Result', f'{searchword} appears {count} times in this text')

        if searchword and searchword not in words:
            messagebox.showinfo(
                'Search Result', f'{searchword} does not appears in this text')

    # input label
    label = tkinter.Label(window, text='Search for a word', font=(
        'helvetica Bold', '15'), width='100', relief='flat', bg='white')
    label.pack(ipady='5')

    # entry for search
    entry1 = tkinter.Entry(window, width=100, borderwidth='0')
    entry1.pack(
        ipady='10', pady='10')

    # search button
    btn3 = tkinter.Button(window, text='Search', width='15', bg='white', fg='black', command=handlesearch, font=(
        'Helvetica Bold', '10'), activebackground='white', activeforeground='black', relief='flat')
    btn3.pack(ipady='10', ipadx='20')

    # table for displaying words
    tv = ttk.Treeview(
        window,
        columns=(1, 2, ),
        show='headings',
        height=30
    )
    tv.pack(pady='20')
    tv.heading(1, text='Word')
    tv.heading(2, text='Occurance')

    for word, lst in data.items():
        tv.insert(parent='', index=lst[1], iid=lst[1], values=(
            word, lst[0]))


# windows setup
window = tkinter.Tk()
window.title('Word Search Project Work')
window.geometry('700x700')
window.resizable(0, 0)
window.configure(bg='black')


# entries
# entry1 = tkinter.Entry(window, width=100, borderwidth='0').pack(
#     ipady='50', pady='30')


# labels
label = tkinter.Label(window, text='Enter Your Text Or Select A File', font=(
    'helvetica Bold', '15'), width='100', relief='flat', bg='white')
label.pack(ipady='5')

# text input
text = tkinter.Text(window, width=75, height=15, wrap='word')
text.pack(ipady='50', pady='20')

# buttons

# extraction handler
btn1 = tkinter.Button(window, text='Search Words', width='15', bg='white', fg='black', command=handleextract, font=(
    'Helvetica Bold', '10'), activebackground='white', activeforeground='black', relief='flat')
btn1.pack(ipady='10', ipadx='20')

# file  uploader
btn2 = tkinter.Button(window, text='Upload Textfile', width='15', bg='white', fg='black', command=handleupload, font=(
    'Helvetica Bold', '10'), activebackground='white', activeforeground='black', relief='flat')
btn2.pack(ipady='10', ipadx='20', pady='20')

# input clearer
btn3 = tkinter.Button(window, text='Clear Input', width='15', bg='white', fg='black', command=handleclearinput, font=(
    'Helvetica Bold', '10'), activebackground='white', activeforeground='black', relief='flat')
btn3.pack(ipady='10', ipadx='20')


# running the app
window.mainloop()
