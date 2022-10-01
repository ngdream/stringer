
import tkinter as tk
from tkinter import END, TOP, ttk
class Window(tk.Tk):
    
    def __init__(self,*args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.button_box=tk.Frame(self)
        self.button_box.pack(padx=10,side=tk.LEFT,expand=True,fill="y")
        self.is_multiline=tk.IntVar()

        languages=['c++','python']
        self.language=ttk.Combobox(self.button_box,values=languages)
        self.language.pack(pady=10)
        self.language.set("c++")
        self.multiline=tk.Checkbutton(self.button_box,variable=self.is_multiline,onvalue=1,offvalue=0,text="multiline")
        self.multiline.pack(padx=10)

        self.convert=tk.Button(self.button_box,text="convert",command=self.stringify)
        self.convert.pack(pady=10,side=TOP,fill="x")
        self.style=ttk.Style(self)
        self.style.theme_use("default")
        

        self.itext=tk.Text(self,font=)
        self.itext.pack(padx=10,expand=True,fill="y",side=tk.LEFT)
        

        self.otext=tk.Text(self)
        self.otext.pack(padx=10,expand=True,fill="y",side=tk.LEFT)
        self.otext.config(state=tk.DISABLED)

        

    def stringify(self):
        i =self.itext.get("1.0",END)[0:-1]
        lang=self.language.get()
        out=str
        if lang=="c++":
            out='"'
            for c in  i :
                if(c == '"'):
                    out+='\\\"'
                elif(c=='\n'):
                    out +='\\n'
                    if(self.is_multiline.get()==1):
                        out+='"\n"'
                elif(c=='\t'):
                    out+='\\t'
                elif(c=='\\'):
                    out+='\\\\'
                else:
                    out+=c
            out+='"'
        elif lang=="python":
            if self.is_multiline.get()==1:
                out='\"\"\"'+i+'\"\"\"'
            else:
                out='"'
                for c in  i :
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
        self.otext.config(state=tk.DISABLED)


if __name__=="__main__":

    window=Window()
    window.mainloop()

