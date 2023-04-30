import random
import string
from tkinter import *

class windowdesign:
    #init class
    def __init__(self):
            root=Tk()
            root.title("Password Generator")
            root.wm_iconbitmap('favicon.ico')
            root.geometry("300x300+50+50")
            
            #checkboxes
            self.Checkbutton1 = IntVar()  
            self.Checkbutton2 = IntVar()  
            self.Checkbutton3 = IntVar()
            self.Checkbutton4= IntVar()
            
            Button1 = Checkbutton(root, text = "Uppercase Letters", 
                                variable = self.Checkbutton1,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 15)
            
            Button2 = Checkbutton(root, text = "Lowercase Letters",
                                variable = self.Checkbutton2,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 15)
            
            Button3 = Checkbutton(root, text = "Numbers",
                                variable = self.Checkbutton3,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 15)  
            
            Button4 = Checkbutton(root, text = "Special Characters",
                                variable = self.Checkbutton4,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 15)  
                
            Button1.pack()  
            Button2.pack()  
            Button3.pack()
            Button4.pack()

            #entry label
            lengthentrylabel=Label(root,text="Enter password length:")
            lengthentrylabel.pack()

            #actual entry
            self.string=IntVar()
            length=Entry(root,textvariable=self.string)
            length.pack()

            #button
            enter=Button(root,text="Generate",command=self.btn)
            enter.pack()

            #generated password
            self.pw=StringVar()
            pwlabel=Label(root, textvariable=self.pw)
            pwlabel.pack()

           
  

            root.mainloop()
   
        
    #button function
    def btn(self):
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        numbers = string.digits
        symbols = string.punctuation
        uppercasestatus= self.Checkbutton1.get()
        lowercasestatus= self.Checkbutton2.get()
        numbersstatus= self.Checkbutton3.get()
        symbolsstatus= self.Checkbutton4.get()
        value = self.string

        if lowercasestatus == 0:
            lowercase = ""
        else:
            lowercase=string.ascii_lowercase

        if uppercasestatus == 0:
            uppercase = ""
        else:
            uppercase=string.ascii_uppercase

        if symbolsstatus == 0:
            symbols = ""
        else:
            symbols=string.punctuation
        
        if numbersstatus == 0:
            numbers = ""
        else:
            numbers=string.digits

        all = lowercase + uppercase + numbers + symbols

        
        for i in range(value.get()):
            temp = ''.join([random.choice(all) for _ in range(value.get())])
            #temp = random.choice(all,value.get())
            password = "".join(temp)

        self.pw.set(password)

windowdesign()
