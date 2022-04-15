from cgitb import text
from msilib.schema import ComboBox
from tkinter import font, messagebox , Label,Tk,ttk
from time import strftime
from pygame import mixer

window = Tk()
window.config(bg='black')
window.geometry('300x300')
window.title('Alarma')
window.minsize(width=500, height=250)
mixer.init()

list_hour = []
list_min = []
list_sec = []

for i in range (0,24):
    list_hour.append(i)

for i in range (0,60):
    list_min.append(i)

for i in range (0,60):
    list_sec.append(i)

text1 = Label(window, text= 'Hora', bg= 'black', fg= 'blue', font= ('Arial',12, 'bold'))
text1.grid(row=1, column=0, padx =5, pady=5)
text2 = Label(window, text= 'Minutos', bg= 'black', fg= 'blue', font= ('Arial',12, 'bold'))
text2.grid(row=1, column=1, padx =5, pady=5)
text3 = Label(window, text= 'Segundos', bg= 'black', fg= 'blue', font= ('Arial',12, 'bold'))
text3.grid(row=1, column=2, padx =5, pady=5)

combobox1= ttk.Combobox(window, values=list_hour, style= "TCombobox", justify='center', width='12', font='Arial')
combobox1.grid(row=2, column=0, padx=15, pady=5)
combobox1.current(0)
combobox2= ttk.Combobox(window, values = list_min, style= "TCombobox", justify='center', width='12', font='Arial')
combobox2.grid(row=2, column=1, padx=15, pady=5)
combobox2.current(0)
combobox3= ttk.Combobox(window, values = list_sec, style= "TCombobox", justify='center', width='12', font='Arial')
combobox3.grid(row=2, column=2, padx=15, pady=5)
combobox3.current(0)

style=ttk.Style()
style.theme_create('combostyle', parent='alt', settings = {'TCombobox':
                                            {'configure': 
                                                {'selectbackground': 'red',
                                                    'fieldbackground': 'gold',
                                                        'background': 'blue'
                                                }}})
style.theme_use('combostyle')

window.option_add('*TCombobox*Listbox*Background', 'white')
window.option_add('*TCombobox*Listbox*Foreground', 'black')
window.option_add('*TCombobox*Listbox*selectBackground', 'green2')
window.option_add('*TCombobox*Listbox*selectForeground', 'black')

alarm = Label(window, fg='blue2', bg='black', font=('RadioLand', 20))
alarm.grid(column=0, row=3, sticky="nsew", ipadx=5, ipady=20)
repeat = Label(window, fg='white', bg='black', text='Repetir', font='Arial')
repeat.grid(column=1, row=3, ipadx=5, ipady=20)
quantity= ttk.Combobox(window, values = (1,2,3,4,5), justify='center', width='8', font='Arial')
quantity.grid(row=3, column=2, padx=5, pady=5)
quantity.current(0)

def get_time():
    x_hour = combobox1.get()
    x_min = combobox2.get()
    x_sec = combobox3.get()

    hour = strftime('%H')
    min = strftime('%M')
    sec = strftime('%S')

    hour_fin = (hour + ' : ' + min+ ' : '+ sec )
    text_hour.config(text=hour_fin, font = ('Radioland', 25))

    hour_alarm = x_hour +' : ' + x_min + ' : ' + x_sec
    alarm['text']= hour_alarm

    #condition
    if int(hour) == int(x_hour):
        if int(min) == int(x_min):
            if int(sec) == int(x_sec):
                mixer.music.load("audio.mp3")
                mixer.music.play(loops= int(quantity.get()))
                messagebox.showinfo(message=hour_alarm, tittle="Alarma")

    text_hour.after(100, get_time)

text_hour = Label(window, fg= 'green2', bg='black')
text_hour.grid(columnspan=3, row=0, sticky="nsew", ipadx=5, ipady=20)

get_time()
window.mainloop()


