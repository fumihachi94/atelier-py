import tkinter as tk

def createInputwindow(rect):
    '''
    rect : [left, top, right, bottom]
    '''
    # Get window position
    window_position = str(rect[2]-rect[0])+"x"+str(rect[3]-rect[1])+"+"+str(rect[0])+"+"+str(rect[1])
    # Create window
    root = tk.Tk()
    # Set window configration
    root.title("パスワード")
    root.geometry(window_position)
    # Set Label
    lbl = tk.Label(text='パスワードを入力してください')
    lbl.place(x=5, y=5)
    # テキストボックス
    txt = tk.Entry(width=20)
    txt.place(x=90, y=70)
    root.mainloop()



if __name__ == "__main__":
    rect = (2674, 315, 2930, 470)
    createInputwindow(rect)