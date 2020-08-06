from tkinter import *   
  
  
top = Tk()  
  
top.geometry("900x600")

b = Button(top, text = "Click", foreground = "red", background = "white", activeforeground = "yellow", activebackground = "black", pady = 40, padx = 40)

top.title("Popup")

top.configure(background ='#49A')

b.pack(side = TOP)

top.mainloop()