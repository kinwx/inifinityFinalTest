# pip install tkcalendar
# pip install mysql-connector-python

from tkinter import *
from datetime import date
from comands.index import *

from tkcalendar import *

# init class set
window = Tk()
width= window.winfo_screenwidth()
height= window.winfo_screenheight()

# setting tkinter window size
window.geometry("%dx%d" % (width, height))
window.title("infinity_test")
window.config(bg="#800000")

# layout divider in 2 parts
left_frame = Frame(window, width=278, height=650, bg="#252525")
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky=N)

right_frame = Frame(window, width=1024, height=650, bg="#252525")
right_frame.grid(row=0, column=1, padx=10, pady=10, sticky=N)

# left frame task gadgets
# title
title_task_label = Label(left_frame, text="Titúlo da Tarefa:", fg="#fff", bg="#252525", font=("Arial", 10))
title_task_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
input_title = Entry(left_frame, width=40)
input_title.grid(row=1, column=0, padx=5, pady=5, ipady=5)

# description
description_task_label = Label(left_frame, text="Descrição da Tarefa:", fg="#fff", bg="#252525", font=("Arial", 10))
description_task_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)
input_description = Text(left_frame, width=30, height=3)
input_description.grid(row=4, column=0, padx=5, pady=5)

# early date
date_task_label = Label(left_frame, text="Data de Início da Tarefa:", fg="#fff", bg="#252525", font=("Arial", 10))
date_task_label.grid(row=5, column=0, padx=5, pady=5, sticky=W)
current_date = date.today()
early_calendar = Calendar(left_frame, selectmode="day",year=current_date.year, month=current_date.month, day=current_date.day, locale="pt_BR")
early_calendar.grid(row=6, column=0, padx=5, pady=5)

# last date
end_date_task_label = Label(left_frame, text="Data de Termino da Tarefa:", fg="#fff", bg="#252525", font=("Arial", 10))
end_date_task_label.grid(row=7, column=0, padx=5, pady=5, sticky=W)
last_calendar = Calendar(left_frame, selectmode="day",year=current_date.year, month=current_date.month, day=current_date.day, locale="pt_BR", mindate=current_date)
last_calendar.grid(row=8, column=0, padx=5, pady=5)

# get infos button
button_add_task = Button(left_frame, text="Adicionar tarefa")
button_add_task.grid(row=9, column=0, padx=5, pady=10, ipadx=6, ipady=2)

# right frame - columns
to_do_column = 0
progress_column = 1
completed_column = 2

# fake padding top
topbar_frame = Frame(right_frame, width=1024, height=10, bg="#252525")
topbar_frame.grid(row=0, columnspan=3)

# columns
to_do_label = Label(right_frame, text="A fazer", relief=RAISED, bg="#252525", fg="#fff", font="bold")
to_do_label.grid(row=1, column=to_do_column, padx=5, pady=5, ipadx=10, ipady=2)
to_do_frame = Frame(right_frame, bg="red", width=300)
to_do_frame.grid(row=2, column=to_do_column, padx=5, sticky=N)

progress_label = Label(right_frame, text="Em andamento", relief=RAISED, bg="#252525", fg="#fff", font="bold")
progress_label.grid(row=1, column=progress_column, padx=5, pady=5, ipadx=10, ipady=2)
progress_frame = Frame(right_frame, bg="red", width=300)
progress_frame.grid(row=2, column=progress_column, padx=5, sticky=N)

completed_label = Label(right_frame, text="Concluído", relief=RAISED, bg="#252525", fg="#fff", font="bold")
completed_label.grid(row=1, column=completed_column, padx=5, pady=5, ipadx=10, ipady=2)
completed_frame = Frame(right_frame, bg="red", width=300)
completed_frame.grid(row=2, column=completed_column, padx=5, sticky=N)

# init load tasks
task_columns_container = ListTaskColumns(to_do_frame, progress_frame, completed_frame)
task_columns_container.loadToDoTask()
task_columns_container.loadTaskProgressOrCompleted("progress")
task_columns_container.loadTaskProgressOrCompleted("completed")

# add task action
task_container = FormTask(input_title, input_description, early_calendar, last_calendar)
button_add_task.configure(command=lambda: task_container.saveTask(to_do_frame, progress_frame, completed_frame))

window.mainloop()
