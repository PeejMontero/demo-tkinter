from tkinter import *
import sys
import getopt

# Fun program to test python3's tkinter
# At any point, try pressing a directional button

class staticvars():
  prog = 0
  toggler = 0
#  file = "files/thumbs.png"

def toggle(n):
  if n == 1:
    return 1
  else:
    return 0
  
def motion(event):
  print("Mouse position: (%s %s)" % (event.x, event.y))
  return
  
def clearpage(master):
  for widget in master.winfo_children()[1:]:
    widget.destroy()

  return
  
def clearpagefull(master):
  for widget in master.winfo_children()[0:]:
    widget.destroy()

  return
  
def leftKey(event):
  mystr = "Left key pressed"
  msg = Message(master, text = mystr, width=400, anchor=W)
  msg.config(bg="white", font= ("calibri", 12))
  msg.pack(fill=X)

def rightKey(event):
  mystr = "Right key pressed"
  msg = Message(master, text = mystr, width=400, anchor=W)
  msg.config(bg="white", font= ("calibri", 12))
  msg.pack(fill=X)

def upKey(event):
  mystr = "Up key pressed"
  msg = Message(master, text = mystr, width=400, anchor=W)
  msg.config(bg="white", font= ("calibri", 12))
  msg.pack(fill=X)

def downKey(event):
  mystr = "Down key pressed"
  msg = Message(master, text = mystr, width=400, anchor=W)
  msg.config(bg="white", font= ("calibri", 12))
  msg.pack(fill=X)
  
def blankpage(event):
  #This clears the widget
  clearpage(master)
  
  nextpage.config(text="Clear")
  
  nextpage.bind("<Button-1>", blankpage)
  
def blankpage2(event):
  #This clears the widget
  clearpage(master)
  nextpage.bind("<Button-1", page5)

def page1(event):
  nextpage.config(text="Next")
  mystr = "One Upon a time there was a guy named Peej."
  msg = Message(master, text=mystr, width=400, anchor=W)
  msg.config(bg="white", font=("calibri", 12))
  msg.pack(fill=X)
  
  nextpage.bind("<Button-1>", page2)
  
  master.mainloop()
  
def page2(event):
  mystr = "He wanted to learn how to use tkinter."
  msg = Message(master, text = mystr, width = 400, anchor = W)
  msg.config(bg = "white", font = ("calibri", 12))
  msg.pack(fill=X)

  nextpage.bind("<Button-1>", page3)

  master.mainloop()

def page3(event):
  mystr = "The End."
  msg = Message(master, text = mystr, width = 400, anchor = W)
  msg.config(bg = "white", font = ("calibri", 12))
  msg.pack(fill=X)

  nextpage.bind("<Button-1>", blankpage)

  master.mainloop()

def page4(event):
  mystr = "Good job you made it."
  msg = Message(master, text = mystr, width = 400, anchor = W)
  msg.config(bg = "white", font = ("calibri", 12))
  nextpage.bind("<Button-1>", blankpage)
  msg.pack(fill=X)

  logo = PhotoImage(file=staticvars.file)
  thumbs = Label(master, image=logo).pack()

  nextpage.bind("<Button-1>", keyboardlistenerl)

  master.mainloop()

def keyboardlistenerl(event):
  clearpage(master)

if __name__ == "__main__":
  master = Tk()
  master.minsize(width=400, height=400)
  master.maxsize(width=400, height=400)
  master.config(bg="white")
  
  nextpage = Button(master, text="Start")
  nextpage.config(bg="blue", fg="white")

  nextpage.bind("<Button-1>", page1)
  nextpage.pack(side=BOTTOM)

  master.bind("<Left>", leftKey)
  master.bind("<Right>", rightKey)
  master.bind("<Up>", upKey)
  master.bind("<Down>", downKey)
  master.mainloop()

