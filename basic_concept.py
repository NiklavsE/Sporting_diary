from time import gmtime, strftime

from tkinter import *
 
window = Tk()
 
window.title("Sporting diary v0.1")
 
window.geometry('410x470')
 
lbl = Label(window, text="Virsraksts")
 
lbl.grid(column=0, row=0)
 
txt = Entry(window,width=50)
 
txt.grid(column=0, row=1)

d_entry = Text(window, width=50)
d_entry.grid(column=0, row=3)

def save():
        x = 0
        heading = txt.get()
        paragraph = d_entry.get("0.1","end-1c")
        heading_output = ""
        paragraph_output = ""
        if len(heading) < 60:
                heading_output = heading
        else:
                for i in range(0,len(heading), 60):
                        for line in range(x, x+60):
                                heading_output += heading[line] 
                        heading_output += '\n'
                        
        if len(paragraph) < 100:
                paragraph_output = paragraph
        else:     
                for i in range(0,len(paragraph), 100):
                        for line in range(x, x+100):
                                paragraph_output += paragraph[line] 
                        paragraph_output += '\n'
                
        with open("text.txt", "a") as f:
                f.write('\n' + strftime("%Y-%m-%d %H:%M:%S", gmtime())+ '\n'  + str(heading_output) + '\n' + '-----------------------------' + '\n' + str(paragraph_output) + '\n')
        d_entry.delete(1.0, END)
        txt.delete(0, END) 
    
 
btn = Button(window, text="Save", command=save)
 
btn.grid(column=0, row=4)
 
window.mainloop()
