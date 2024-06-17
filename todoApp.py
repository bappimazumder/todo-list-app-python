import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
from tkinter import CENTER
from tkinter import *
from tkcalendar import Calendar,DateEntry

# defining the function to add tasks to the list  
def add_task():  
    # getting the string from the entry field  
    task_description = task_description_field.get()  
    task_dueDate = task_dueDate_field.get()  
    # checking whether the string is empty or not  
    if len(task_description) == 0:  
        # displaying a message box with 'Empty Field' message  
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:  
        # adding the string to the tasks list 
        task = {
            'description': task_description,
            'due_date': task_dueDate,
            'mark_as_complete':"No"
        } 
        tasks.append(task)  
        
        # calling the function to update the list  
        list_update()  
        # deleting the entry in the entry field  
        task_description_field.delete(0, 'end')
        task_dueDate_field.delete(0, 'end')

def edit_task():   
    selected_item = task_listbox.selection()[0]
    task_listbox.item(selected_item, text="blub", values=("foo", "bar"))

def mark_complete():
    selected_item = task_listbox.selection()[0]    
    task_listbox.set(selected_item, "Is Complete?","Yes")

# defining the function to update the list  
def list_update():  
    # calling the function to clear the list  
    clear_list()  
    # iterating through the strings in the list  
    for task in tasks:  
        # using the insert() method to insert the tasks in the list box        
        task_listbox.insert('', 'end', text="1", values=(task['description'],task['due_date'],task['mark_as_complete'])) 
# defining the function to delete a task from the list  
def delete_task():  
    # using the try-except method  
    try:  
        # getting the selected entry from the list box  
        selected_item = task_listbox.selection()[0]
        item_index = task_listbox.index(selected_item)
        task_listbox.delete(selected_item)
        tasks.pop(item_index)  
        # checking if the stored value is present in the tasks list  
        if selected_item in tasks:  
            # removing the task from the list  
            tasks.remove(selected_item)  
            # calling the function to update the list  
            list_update()              
    except:  
        # displaying the message box with 'No Item Selected' message for an exception  
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')
# function to delete all tasks from the list  
def delete_all_tasks():  
    # displaying a message box to ask user for confirmation  
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    # if the value turns to be True  
    if message_box == True:  
        # using while loop to iterate through the tasks list until it's empty   
        while(len(tasks) != 0):  
            # using the pop() method to pop out the elements from the list  
            tasks.pop()        
        # calling the function to update the list  
        list_update()    

# function to close the application  
def close():  
    # printing the elements from the tasks list  
    print(tasks)  
    # using the destroy() method to close the application  
    guiWindow.destroy()   

def sort_treeview(tree, col, descending):
    tasks.sort(key=lambda x: x['due_date'])    
    tasks.sort(key=lambda x: x['due_date'])
    data = [(tree.set(item, col), item) for item in tree.get_children('')]
    data.sort(reverse=descending)
    for index, (val, item) in enumerate(data):
        tree.move(item, '', index)
    tree.heading(col, command=lambda: sort_treeview(tree, col, not descending))

def clear_list():  
    for item in task_listbox.get_children():
      task_listbox.delete(item)
    # using the delete method to delete all entries from the list box  
    #task_listbox.delete(0, 'end')  

# main function  
if __name__ == "__main__":  
    # creating an object of the Tk() class  
    guiWindow = tk.Tk()  
    # setting the title of the window  
    guiWindow.title("To-Do List App")  
    # setting the geometry of the window  
    guiWindow.geometry("500x500+850+350")  
    # disabling the resizable option  
    guiWindow.resizable(0, 0)  
    # setting the background color to #FAEBD7  
    guiWindow.configure(bg = "#FAEBD7")  

    tasks = []   
    
    # defining frames using the tk.Frame() widget  
    header_frame = tk.Frame(guiWindow, bg = "powderblue")  
    functions_frame = tk.Frame(guiWindow, bg = "powderblue")  
    listbox_frame = tk.Frame(guiWindow, bg = "powderblue")  

    header_frame.pack(fill = "both")  
    functions_frame.pack(side = "left", expand = True, fill = "both")  
    listbox_frame.pack(side = "right", expand = True, fill = "both")  

    # defining a label using the ttk.Label() widget  
    header_label = ttk.Label(  
        header_frame,  
        text = "Welcome to The To-Do List",  
        font = ("Comic Sans MS", "25"),  
        background = "powderblue",  
        foreground = "#8B4513"  
    )  

    # using the pack() method to place the label in the application  
    header_label.pack(padx = 20, pady = 20)  
  
    # defining another label using the ttk.Label() widget  
    task_description_label = ttk.Label(  
        functions_frame,  
        text = "Task:",  
        font = ("Consolas", "11", "bold"),  
        background = "powderblue",  
        foreground = "#000000"  
    )  
    # using the place() method to place the label in the application  
    task_description_label.place(x = 30, y = 30)  
      
    # defining an entry field using the ttk.Entry() widget  
    task_description_field = ttk.Entry(  
        functions_frame,  
        font = ("Consolas", "12"),  
        width = 12,  
        background = "#FFF8DC",  
        foreground = "#A52A2A"  
    )  
    # using the place() method to place the entry field in the application  
    task_description_field.place(x = 105, y = 30) 


    # defining another label using the ttk.Label() widget  
    task_dueDate_label = ttk.Label(  
        functions_frame,  
        text = "Due Date:",  
        font = ("Consolas", "11", "bold"),  
        background = "powderblue",  
        foreground = "#000000"  
    )  
    # using the place() method to place the label in the application  
    task_dueDate_label.place(x = 30, y = 60)  
    
    # Add Calendar
    def get_date():
        selected_date = cal.get()
        print(f"Selected date: {selected_date}")
    
    task_dueDate_field = DateEntry(guiWindow, date_pattern="yyyy-mm-dd")
    task_dueDate_field.place(x = 105, y = 150) 
  
     # adding buttons to the application using the ttk.Button() widget  
    add_button = ttk.Button(  
        functions_frame,  
        text = "Add Task",  
        width = 24,  
        command = add_task  
    ) 
    mark_done_button = ttk.Button(  
        functions_frame,  
        text = "Mark as Complete",  
        width = 24,  
        command = mark_complete  
    )  
    del_button = ttk.Button(  
        functions_frame,  
        text = "Delete Task",  
        width = 24,  
        command = delete_task  
    )  
    del_all_button = ttk.Button(  
        functions_frame,  
        text = "Delete All Tasks",  
        width = 24,  
        command = delete_all_tasks  
    )  
    exit_button = ttk.Button(  
        functions_frame,  
        text = "Exit",  
        width = 24,  
        command = close  
    )  
 # Add a Treeview widget
    task_listbox = ttk.Treeview(guiWindow, column=("Task", "Due Date","Is Complete?"), show='headings', height=15)
    sort_button = ttk.Button(  
        functions_frame,  
        text = "Sort by Due Date",  
        width = 24,  
        command = sort_treeview(task_listbox,'Due Date',False)  
    )

    # using the place() method to set the position of the buttons in the application  
    add_button.place(x = 30, y = 120)  
    mark_done_button.place(x = 30, y = 160)
    del_button.place(x = 30, y = 200)  
    del_all_button.place(x = 30, y = 240)  
    exit_button.place(x = 30, y = 280)  

   

    task_listbox.column("# 1", anchor=CENTER,minwidth=0, width=80)
    task_listbox.heading("# 1", text="Task")
    task_listbox.column("# 2", anchor=CENTER,minwidth=0, width=80)
    task_listbox.heading("# 2", text="Due Date")
    task_listbox.column("# 3", anchor=CENTER,minwidth=0, width=80)
    task_listbox.heading("# 3", text="Is Complete?")

   
    task_listbox.pack()
    task_listbox.place(x = 250, y = 150)  

    
    # calling some functions 
    list_update()  
    
    # using the mainloop() method to run the application  
    guiWindow.mainloop()    