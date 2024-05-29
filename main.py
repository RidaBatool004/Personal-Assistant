# Importing modules and files
from tkinter import * 
from tkinter import ttk
from PIL import Image, ImageTk
import project_database
import text_to_speech
import os
import tkinter as tk

class Assistant:
    def __init__(self,root):
        self.root = root
        self.root.title("AI Personal Assistant")
        self.root.geometry("500x600+0+0")
        self.root.resizable(False,False)
        self.root.config(bg="#008080")

        # Frames
        frame = LabelFrame(self.root,padx = 5, pady = 7, borderwidth=2,relief=RAISED,border=4)
        frame.grid(row=0,column=1,padx=70,pady =20)

        # Text Label - Title
        text_label = Label(frame,text = " Nova - Personal AI Assistant ",font=("algerian", 15,"bold","italic"),bg = "#003333",fg = "white").grid(row = 0,column=0,padx=10,pady=10)

        # IMAGE
        image = Image.open("assistant.jpg")
        image = image.resize((150,150))
        self.photoimg = ImageTk.PhotoImage(image)
        img_label = Label(frame,image=self.photoimg).grid(row=1,column=0,pady=20)

        # Text Box
        self.text = tk.Text(self.root,font=("aerial",10),bg= "#009688",fg = "black")
        self.text.grid(row=2,column=0)
        self.text.place(x=120,y=310,height=100,width=300)

        # Label for Entry box
        label = Label(self.root,text = "Enter your Question",font=("aerial",10),fg="white",bg="#008080")
        label.place(x=10,y=430)

        # Entry Box
        entry_boxvar= StringVar()
        self.entry_box = Entry(self.root,justify=CENTER,textvariable=entry_boxvar)
        self.entry_box.place(x=90,y=470,height=30,width=350)
        
        #History Button
        self.button_1 = Button(self.root,text="HISTORY",font=("aerial",10),bg="#009688",fg="White",padx=40,pady=16,borderwidth=2,border=2,relief=SOLID,command=self.show_history)
        self.button_1.place(x=30,y=520)
        
        # Clear Button
        self.button_2 = Button(self.root,text="CLEAR",font=("aerial",10),bg="#009688",fg="White",padx=40,pady=16,borderwidth=2,border=2,relief=SOLID,command=self.clear)
        self.button_2.place(x=190,y=520)

        # Send Button
        self.button_3 = Button(self.root,text="SEND",font=("aerial",10),bg="#009688",fg="White",padx=40,pady=16,borderwidth=2,border=2,relief=SOLID,command=self.send)
        self.button_3.place(x=350,y=520)
# *************FUNCTIONS DECLARATION******************
    # This function is called when history button is clicked
    def show_history(self):
        history_window = Toplevel(self.root)
        history_window.title("Search History")
        history_window.geometry("500x600")
        history_window.resizable(False,False)

        history_text = Text(history_window, width=60, height=40,bg="#009688")
        history_text.pack()

        with open("search_history.txt", "r") as f:
            history_text.config(state=NORMAL)
            history_text.insert(END, f.read())
            history_text.config(state=DISABLED)
        # This function clears the search history file and updates the GUI.
        def clear_history():
            if os.path.exists("search_history.txt"):
                os.remove("search_history.txt")
                print("Search history cleared.")
                history_text.config(state=NORMAL)
                history_text.delete('1.0', tk.END)
                # Display a confirmation message
            history_text.insert(tk.END, "HISTORY has been cleared\n")
            history_text.config(state=DISABLED)
            # clear button on history window
            clear_button = Button(history_window, text="CLEAR HISTORY", command=clear_history,padx=10,pady=10,bg="#008080",borderwidth=2,border=2,relief=SOLID, font=("aerial",8),fg="white")
            clear_button.place(relx=0.7660, rely=0, anchor="nw")

     # This function is called when clear button is clicked
    def clear(self):
        self.text.delete("1.0",END)
        self.entry_box.delete("0",END)
        
     # This function is called when send botton is clicked
    def send(self,*args):
        questions = self.entry_box.get()
        answer= str(project_database.getfromprojectdb(questions))
        function = "you----->  " + questions +"\n" +"assistant--->  "+ str(project_database.getfromprojectdb(questions))+"\n"
        self.text.insert("1.0",function)
        text_to_speech.text_to_speech(answer)
        self.entry_box.delete('0',END)
        # writing question answers in search_history file 
        with open("search_history.txt", "a") as f:
            f.write(function)
            f.write("\n")

        # Event binding
        self.root.bind('<Return>',self.send)

if __name__ == "__main__":
    root = Tk()
    object = Assistant(root)
    root.mainloop()
