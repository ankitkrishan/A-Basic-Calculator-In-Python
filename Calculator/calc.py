import tkinter
mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry("227x350")
mainWindow["padx"] = 8
mainWindow["bg"] = "red"
text = tkinter.Text(mainWindow, height=4, width=25)
text.grid(row=0, column=0, sticky="nw")
text.config(borderwidth=3, relief="ridge")
text["bg"] = "light blue"
def buttonClick(num: str):
    if num == "C":
        text.delete(1.0, tkinter.END)
    elif num == "=":
        result = eval(text.get(1.0, tkinter.END))
        text.delete(1.0, tkinter.END)
        text.insert(tkinter.END, result)
    else:
        text.insert(tkinter.END, num)
l = ["C", "CE", "7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", "0", "=", "/"]
frame = tkinter.Frame(mainWindow)
frame.grid(row=3, column=0, sticky="nsew")
tkinter.Button(frame, text=l[0], height=2, width = 5, borderwidth=5, command=lambda: buttonClick("C"), bg="orange").grid(row=0, column=0, sticky="nsw")
tkinter.Button(frame, text=l[1], height=2, width = 5, borderwidth=5, command=lambda: buttonClick("C"), bg="orange").grid(row=0, column=1, sticky="nsw")
count = 0
r = 1
c = 0
for i in range(2, len(l)):
    if count == 4:
        count = 0
        c = 0
        r += 1
    tkinter.Button(frame, text=l[i], height=2, width = 5, borderwidth=5, command=lambda i=i: buttonClick(l[i])).grid(row=r, column=c)
    c+=1
    count+=1
mainWindow.mainloop()
