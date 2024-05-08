# =========================
# frame_task = Frame(right_frame, bg="#ecf0f3", width=300, height=50)
# frame_task.grid(row=3, column=to_do_column, pady=5)

# title_label = Label(frame_task, text="Fazer compras", font=("Arial", 9, "bold"))
# title_label.grid(row=0, column=0, sticky=W)
# description_label = Label(frame_task, text="Ir ao mercado fazer compras", font=("Arial", 7), width=35, anchor=W)
# description_label.grid(row=1, column=0, sticky=W)

# early_date_label = Label(frame_task, text="Inicio: 22/01/2001")
# early_date_label.grid(row=0, column=1, sticky=E)
# last_date_label = Label(frame_task, text="Fim: 22/01/2001")
# last_date_label.grid(row=1, column=1, sticky=E)

# button_task_progress = Button(frame_task, text="Em andamento")
# button_task_progress.grid(row=2, column=0, padx=5, pady=5, sticky=W)

# button_delete_task = Button(frame_task, text="Excluir")
# button_delete_task.grid(row=2, column=1, padx=5, sticky=E)


# component progress task
# frame_task_progress = Frame(right_frame, bg="#ecf0f3", width=300, height=50)
# frame_task_progress.grid(row=3, column=progress_column, pady=5)

# variable_check = IntVar()
# check_progress = Checkbutton(frame_task_progress, text="Concluída", variable=variable_check, onvalue=1, offvalue=0, height=1, width=10, activeforeground="green")
# check_progress.grid(row=0, column=0, padx=5, pady=5, sticky=W)

# button_delete_task_progress = Button(frame_task_progress, text="Excluir")
# button_delete_task_progress.grid(row=0, column=1, padx=5, sticky=E)

# title_label_progress = Label(frame_task_progress, text="Fazer compras", font=("Arial", 9, "bold"))
# title_label_progress.grid(row=1, column=0, sticky=W)
# description_label_progress = Label(frame_task_progress, text="Ir ao mercado fazer compras", font=("Arial", 7), width=35, anchor=W)
# description_label_progress.grid(row=2, column=0, sticky=W)

# early_date_label_progress = Label(frame_task_progress, text="Inicio: 22/01/2001")
# early_date_label_progress.grid(row=1, column=1, sticky=E)
# last_date_label_progress = Label(frame_task_progress, text="Fim: 22/01/2001")
# last_date_label_progress.grid(row=2, column=1, sticky=E)

# component completed task

# frame_task_completed = Frame(right_frame, bg="#ecf0f3", width=300, height=50)
# frame_task_completed.grid(row=3, column=completed_column, pady=5)

# variable_check_completed = IntVar(value=1)
# check_completed = Checkbutton(frame_task_completed, text="Concluída",
#                               variable=variable_check_completed, onvalue=1, offvalue=0,
#                               height=1, width=10, activeforeground="green")
# check_completed.grid(row=0, column=0, padx=5, pady=5, sticky=W)

# button_delete_task_completed = Button(frame_task_completed, text="Excluir")
# button_delete_task_completed.grid(row=0, column=1, padx=5, sticky=E)

# title_label_completed = Label(frame_task_completed, text="Fazer compras", font=("Arial", 9, "bold"))
# title_label_completed.grid(row=1, column=0, sticky=W)
# description_label_completed = Label(frame_task_completed, text="Ir ao mercado fazer compras", font=("Arial", 7), width=35, anchor=W)
# description_label_completed.grid(row=2, column=0, sticky=W)

# early_date_label_completed = Label(frame_task_completed, text="Inicio: 22/01/2001")
# early_date_label_completed.grid(row=1, column=1, sticky=E)
# last_date_label_completed = Label(frame_task_completed, text="Fim: 22/01/2001")
# last_date_label_completed.grid(row=2, column=1, sticky=E)


# class Task:
#     def __init__(self, id, title, description, earlyDate, lastDate) -> None:
#         self.id = id
#         self.title = title
#         self.description = description
#         self.earlyDate = earlyDate
#         self.lastDate = lastDate


# class globalData:
#     def __init__(self) -> None:
#         self.list = [Task(0, "Fazer compras", "Ir ao mercado fazer compras", "22/01/2001", "22/01/2001")]

#     def insertTask(self, value):
#         self.list.append(value)
    
#     def loadTasks(self, master):
#         for task in self.list:
#             index = self.list.index(task)
#             print(index, task.title, task.description, task.earlyDate, task.lastDate)

#             frame_task = Frame(master, bg="#ecf0f3", width=300, height=50)
#             frame_task.grid(row=0, column=0, pady=5)

#             title_label = Label(frame_task, text=task.title, font=("Arial", 9, "bold"))
#             title_label.grid(row=0, column=0, sticky=W)
#             description_label = Label(frame_task, text=task.description, font=("Arial", 7), width=35, anchor=W)
#             description_label.grid(row=1, column=0, sticky=W)

#             early_date_label = Label(frame_task, text=f"Inicio: {task.earlyDate}")
#             early_date_label.grid(row=0, column=1, sticky=E)
#             last_date_label = Label(frame_task, text=f"Fim: {task.lastDate}")
#             last_date_label.grid(row=1, column=1, sticky=E)

#             button_task_progress = Button(frame_task, text="Em andamento")
#             button_task_progress.grid(row=2, column=0, padx=5, pady=5, sticky=W)

#             button_delete_task = Button(frame_task, text="Excluir")
#             button_delete_task.grid(row=2, column=1, padx=5, sticky=E)


# principal_data = globalData()
# principal_data.loadTasks(to_do_frame)


# frame_task = Frame(self.toDoList, bg="#ecf0f3", width=300, height=50)
# frame_task.grid(row=index, column=0, pady=5)

# title_label = Label(frame_task, text=task[1], font=("Arial", 9, "bold"))
# title_label.grid(row=0, column=0, sticky=W)
# description_label = Label(frame_task, text=task[2], font=("Arial", 7), width=35, anchor=W)
# description_label.grid(row=1, column=0, sticky=W)

# early_date_label = Label(frame_task, text=f"Inicio: {task[3]}")
# early_date_label.grid(row=0, column=1, sticky=E)
# last_date_label = Label(frame_task, text=f"Fim: {task[4]}")
# last_date_label.grid(row=1, column=1, sticky=E)

# button_task_progress = Button(frame_task, text="Em andamento", command=lambda: progressInsert(
#     frame_task, task, self.progresslist))
# button_task_progress.grid(row=2, column=0, padx=5, pady=5, sticky=W)

# button_delete_task = Button(frame_task, text="Excluir", command=lambda: deleteCurrentTask(frame_task, task[0], "tasks"))
# button_delete_task.grid(row=2, column=1, padx=5, sticky=E)

# frame_task_progress = Frame(currentMaster, bg="#ecf0f3", width=300, height=50)
# frame_task_progress.grid(row=index, column=progress_column, pady=5)

# variable_check = IntVar()
# check_progress = Checkbutton(frame_task_progress,
#     text="Concluída", variable=variable_check, onvalue=1, offvalue=0, height=1, width=10, activeforeground="green")
# check_progress.grid(row=0, column=0, padx=5, pady=5, sticky=W)

# button_delete_task_progress = Button(frame_task_progress, text="Excluir", command=lambda: deleteCurrentTask(
#     frame_task_progress, task[0], tableName))
# button_delete_task_progress.grid(row=0, column=1, padx=5, sticky=E)

# title_label_progress = Label(frame_task_progress, text=task[1], font=("Arial", 9, "bold"))
# title_label_progress.grid(row=1, column=0, sticky=W)
# description_label_progress = Label(frame_task_progress, text=task[2], font=("Arial", 7), width=35, anchor=W)
# description_label_progress.grid(row=2, column=0, sticky=W)

# early_date_label_progress = Label(frame_task_progress, text=f"Inicio: {task[3]}")
# early_date_label_progress.grid(row=1, column=1, sticky=E)
# last_date_label_progress = Label(frame_task_progress, text=f"Fim: {task[4]}")
# last_date_label_progress.grid(row=2, column=1, sticky=E)