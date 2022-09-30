





from ast import Delete
import tkinter as tk
from tkinter import END, TOP, ttk

class Window(tk.Tk):
    
    def __init__(self,*args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.button_box=tk.Frame(self)
        self.button_box.pack(padx=10,side=tk.LEFT,expand=True,fill="y")

        languages=['c++','python','java']
        self.language=ttk.Combobox(self.button_box,values=languages)
        self.language.pack(pady=10)
        self.language.set("c++")


        self.convert=tk.Button(self.button_box,text="convert",command=self.stringify)
        self.convert.pack(pady=10,side=TOP,fill="x")
        self.style=ttk.Style(self)
        self.style.theme_use("default")


        self.itext=tk.Text(self)
        self.itext.pack(padx=10,expand=True,fill="y",side=tk.LEFT)

        self.otext=tk.Text(self)
        self.otext.pack(padx=10,expand=True,fill="y",side=tk.LEFT)
        self.otext.config(state=tk.DISABLED)

        

    def stringify(self):
        out='"'
        lang=self.language.get()
        if lang=="c++":
            for c in self.itext.get("1.0",END):
                if(c == '"'):
                    out+='\\\"'
                elif(c=='\n'):
                    out +='\\n'
                elif(c=='\t'):
                    out+='\\t'
                elif(c=='\\'):
                    out+='\\\\'
                else:
                    out+=c
            out+='"'
            self.otext.config(state=tk.NORMAL)
            self.otext.delete('1.0',END)
            self.otext.insert("1.0",out)

if __name__=="__main__":

    window=Window()
    window.mainloop()

