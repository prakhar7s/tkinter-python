from tkinter import *

root = Tk()
root.title('Learning GUI')

# screen_width=root.winfo_screenwidth()
# screen_height=root.winfo_screenheight()
# print("Screen width:",screen_width)
# print("Screen height:",screen_height)

#resize tkinter window 400x200 and place at position (150,150)
root.geometry("400x200+150+150")

#exit window will close GUI window when clicked
# exitButton=Button(root,text='Exit program',command=root.destroy)
# exitButton.pack()

#to write a message on the screen
# def my_callback():
    # print("you clicked the button....")
# msg_button=Button(root,text='click here',command=my_callback)
# msg_button.pack()

# label=Label(root,text='welcome to GUI programming in python !!!')
# label.pack()
# label.config(foreground='black',background='blue',text='add colors to your life')


#create main menu bar
# menu_bar=Menu(root, background="red")
#create the submenu, tearoff indicates that menu can pop out so 0 means can't pop out
# fileMenu=Menu(menu_bar,tearoff=0)
#add commands to submenu
# fileMenu.add_command(label="stop",command=root.destroy)
# fileMenu.add_command(label="kill",command=root.destroy)
# fileMenu.add_command(label="exit",command=root.destroy)
#add the file drop menu down sub-menu in the main menu bar
# menu_bar.add_cascade(label="File",menu=fileMenu)
# root.config(menu=menu_bar)

#create empty box
entry = Entry(root)
entry.pack()

label = None
frame = None


scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set )


# print the contents of entry box in a console
def printMsg():
    mylist.insert(END, "This is line number")
    mylist.pack( side = LEFT, fill = BOTH )


    
    # global label
    # if(label is not None):
    #     label.destroy()  
    #     frame.destroy() 

    # # frame
    # frame = Frame(mylist, relief = 'sunken',bd = 1, bg = 'white')
    # frame.pack(expand = False, padx = 10, pady = 10)

    # lable = Label(frame, text = entry.get() ,width = 45, height = 10, bg = "black",fg = "white") 
    # lable.pack()

# create a button,when clicked will print the contents of the entry box
button=Button(root,text='search content',command=printMsg)
button.pack()
root.mainloop()

# canvas=Canvas(root,width=250,height=200)
# canvas.pack()
# #draw orange dashed line
# canvas.create_line(0,0,250,200,fill='orange',dash=(5,15))
# #draw yellow rectangle at (100,50)to (150,60)
# canvas.create_rectangle(100,50,150,60,fill='yellow')
# #draw oval(circle) from (30,30) to (50,50)
# canvas.create_oval(30,30,50,50,fill='green')
# root.mainloop()