try:
    import tkinter as tk
except:
    import tkinter as tk

root = tk.Tk()
root.geometry("300x300")

def close_window():
    root.destroy()

var = tk.StringVar()
var.set("Waiting…")

def ok_action():
    var.set("ok")

label = tk.Label(root, textvariable=var)
label.pack()

ok_btn = tk.Button(text = "OK", 
                   command = ok_action(),
                   width=14)

cancel_btn = tk.Button(text = "Cancel", 
                   command = close_window,
                   width=14)

ok_btn.pack(fill = 'x', padx=20, side = 'left')
cancel_btn.pack(fill = 'x', padx=20, side = 'left')

root.mainloop()