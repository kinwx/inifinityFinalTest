from services.index import con
from tkinter import *
from time import sleep

to_do_column = 0
progress_column = 1
completed_column = 2

def deleteCurrentTask(currentFrame, taskId, tableName):
    currentFrame.destroy()
    con.deleteTask(tableName, taskId)
    

def progressInsert(currentFrame, task, progressMaster, completedMaster):
    currentFrame.destroy()
    con.insertInTable("progress", *task)
    con.deleteTask("tasks", task[0])

    sleep(.5)
    tasks = con.getTasks("progress")
    currentTask = tasks[-1]
    index = tasks.index(currentTask)

    createCheckBoxTaskComponent(progressMaster, index, currentTask, "progress", completedMaster, False)
    

def completedInsert(currentFrame, task, completedMaster, previousMaster):
    currentFrame.destroy()
    con.insertInTable("completed", *task)
    con.deleteTask("progress", task[0])

    sleep(.5)
    tasks = con.getTasks("completed")
    currentTask = tasks[-1]
    index = tasks.index(currentTask)

    createCheckBoxTaskComponent(completedMaster, index, currentTask, "completed", previousMaster, True)
    

def createTaskComponent(master, indexRow, task, progressMaster, completedMaster):
    frame_task = Frame(master, bg="#ecf0f3", width=300, height=50)
    frame_task.grid(row=indexRow, column=0, pady=5)

    title_label = Label(frame_task, text=task[1], font=("Arial", 9, "bold"))
    title_label.grid(row=0, column=0, sticky=W)
    description_label = Label(frame_task, text=task[2], font=("Arial", 7), width=35, anchor=W)
    description_label.grid(row=1, column=0, sticky=W)

    early_date_label = Label(frame_task, text=f"Inicio: {task[3]}")
    early_date_label.grid(row=0, column=1, sticky=E)
    last_date_label = Label(frame_task, text=f"Fim: {task[4]}")
    last_date_label.grid(row=1, column=1, sticky=E)

    button_task_progress = Button(frame_task, text="Em andamento", command=lambda: progressInsert(
        frame_task, task, progressMaster, completedMaster))
    button_task_progress.grid(row=2, column=0, padx=5, pady=5, sticky=W)

    button_delete_task = Button(frame_task, text="Excluir", command=lambda: deleteCurrentTask(frame_task, task[0], "tasks"))
    button_delete_task.grid(row=2, column=1, padx=5, sticky=E)

def createCheckBoxTaskComponent(currentMaster, indexRow, task, belongTableName, nextMaster, check):
    frame_task_checkbox = Frame(currentMaster, bg="#ecf0f3", width=300, height=50)
    frame_task_checkbox.grid(row=indexRow, column=progress_column, pady=5)

    if(not check):
        variable_check = IntVar()
        check_button = Checkbutton(frame_task_checkbox, text="Concluída",activeforeground="green",
            variable=variable_check, onvalue=1, offvalue=0, height=1, width=10,
            command=lambda: completedInsert(frame_task_checkbox, task, nextMaster, currentMaster))
        check_button.grid(row=0, column=0, padx=5, sticky=W)

    button_delete_task = Button(frame_task_checkbox, text="Excluir", command=lambda: deleteCurrentTask(
        frame_task_checkbox, task[0], belongTableName))
    button_delete_task.grid(row=0, column=1, padx=5, pady=5, sticky=E)

    title_label_checkbox = Label(frame_task_checkbox, text=task[1], font=("Arial", 9, "bold"))
    title_label_checkbox.grid(row=1, column=0, sticky=W)
    description_label_checkbox = Label(frame_task_checkbox, text=task[2], font=("Arial", 7), width=35, anchor=W)
    description_label_checkbox.grid(row=2, column=0, sticky=W)

    early_date_label_progress = Label(frame_task_checkbox, text=f"Inicio: {task[3]}")
    early_date_label_progress.grid(row=1, column=1, sticky=E)
    last_date_label_progress = Label(frame_task_checkbox, text=f"Fim: {task[4]}")
    last_date_label_progress.grid(row=2, column=1, sticky=E)


class ListTaskColumns:
    def __init__(self, toDoListMaster, progressListMaster, completedListMaster) -> None:
        self.toDoListMaster = toDoListMaster
        self.progresslistMaster = progressListMaster
        self.completedListMaster = completedListMaster

    def loadToDoTask(self):
        try:
            tasks = con.getTasks("tasks")
            for task in tasks:
                index = tasks.index(task)

                createTaskComponent(self.toDoListMaster, index, task, self.progresslistMaster, self.completedListMaster)
        except:
            print("error")

    def loadTaskProgressOrCompleted(self, tableName):
        try:
            tasks = con.getTasks(tableName)
            masters = {
                "current": self.progresslistMaster,
                "next" : self.completedListMaster,
                "check": False
            } if tableName == "progress" else {
                "current": self.completedListMaster,
                "next": self.progresslistMaster,
                "check": True
            }
            for task in tasks:
                index = tasks.index(task)

                createCheckBoxTaskComponent(masters["current"], index, task, tableName, masters["next"], masters["check"])

        except:
            print("error")


class FormTask:
    def __init__(self, entryTitle, entryDescription, earlyDate, lastDate):
        self.entryTitle = entryTitle
        self.entryDescription = entryDescription
        self.earlyDate = earlyDate
        self.lastDate = lastDate

    def saveTask(self, toDoMaster, progressMaster, completedMaster):
        title = self.entryTitle.get()
        if(not title):
            return
        
        description = self.entryDescription.get('1.0', 'end-1c')
        early_date = self.earlyDate.get_date()
        last_date = self.lastDate.get_date()

        self.entryTitle.delete(0, "end")
        self.entryDescription.delete("1.0", "end")

        con.insertTask(title, description, early_date, last_date)
        sleep(1)
        self.loadNewTask(toDoMaster, progressMaster, completedMaster)
    
    def loadNewTask(self, master, progressMaster, completedMaster):
        try:
            tasks = con.getTasks("tasks")
            task = tasks[-1]
            index = tasks.index(task)

            createTaskComponent(master, index, task, progressMaster, completedMaster)

        except:
            print("error ao carregar última task.")