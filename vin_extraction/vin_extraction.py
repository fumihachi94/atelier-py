from logging import getLogger
import pandas as pd
import re
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import datetime

logger = getLogger(__name__)
logger.disabled = False

g_vinpd       = pd.DataFrame()
g_column_list = []
g_filepath    = ""
g_colname     = "ＶＩＮ／プレート打刻情報"

# Extract VIN list from select file
def readVIN(filepath):
    global g_vinpd, g_column_list
    n = 0
    p = r'"(.*?)"'
    data = []

    try:
        with open(filepath) as f:
            for line in f:
                if line[0] == "#":
                    continue
                else:
                    n = n+1
                    # Extract as list using regular expression
                    r = re.findall(p, line) 
                    if n == 1:
                        g_column_list = r
                        logger.info("column list:" + " ".join(g_column_list))
                    else:
                        data.append(r)

        # Create pandas data frame and delete VIN duplicate elements. 
        df = pd.DataFrame(data, columns=g_column_list).drop_duplicates()

        # columnlistbox = tk.Listbox(column_list, listvariable=tk.StringVar(value=g_column_list), height=15,selectmode="single")
        # columnlistbox.pack()

        g_vinpd   = df[g_colname].copy()
        logger.info(g_vinpd)

        # Create vin list box with scrollbar
        scroll=tk.Scrollbar(frame_list)
        scroll.pack(side=tk.RIGHT,fill="y")
        list_value = tk.StringVar(value=df[g_colname].tolist())
        Listbox = tk.Listbox(frame_list, listvariable=list_value, height=15,selectmode="extended",yscrollcommand=scroll.set)
        Listbox.pack(padx=10)
        scroll["command"]=Listbox.yview

    except FileNotFoundError as e: 
        messagebox.showerror("File error", str(e))
    except Exception as e: 
        messagebox.showerror("Exception error", str(e))

# Select reading file
def filedialog_clicked():
    global g_filepath
    iDir = os.path.abspath(os.path.dirname(__file__))
    filepath = filedialog.askopenfilename(initialdir = iDir, filetypes=[('テキストファイル', '*.txt'), ('CSVファイル', '*.csv')])
    g_filepath = filepath
    entry.set(filepath)
    
    
# Execute vin extraction
def exeVINExtraction():
    readVIN(g_filepath)

# Export to txt
def export_clicked():
    now = datetime.datetime.now()
    filename = './vinlist' + now.strftime('%Y%m%d_%H%M%S') + '.txt'
    if g_vinpd.empty:
        messagebox.showerror("Export error", "[エクスポートエラー] VIN情報を読み込んでください")
    else :
        g_vinpd.to_csv(filename, header=False, index=False)
        messagebox.showinfo("Export complete", "エクスポートが完了しました")
        logger.info('Export complete.')


# main
if __name__ == "__main__":

    # Create root tKinter module
    root = tk.Tk()
    root.title("VIN Extraction")

    # Create main frame
    frame_select = ttk.Frame(root, padding=10)
    frame_select.grid(row=0, column=1, sticky=tk.W)

    # Create "File Reference" label
    IDirLabel = ttk.Label(frame_select, text="ファイル", padding=(5, 2))
    IDirLabel.pack(side=tk.LEFT)
    
    # Create "File Reference" entry
    entry = tk.StringVar()
    IDirEntry = ttk.Entry(frame_select, textvariable=entry, width=30)
    IDirEntry.pack(side=tk.LEFT)

    # Create "File Reference" button
    IDirButton = ttk.Button(frame_select, text="参照", command=filedialog_clicked)
    IDirButton.pack(side=tk.LEFT)

    # Create operation buttom frame
    padx_exe = 10
    frame_exe = ttk.Frame(root, padding=10)
    frame_exe.grid(row=2,column=1,sticky=tk.W)

    # Create exe button
    button1 = ttk.Button(frame_exe, text="実行", command=exeVINExtraction)
    button1.pack(fill = "x", padx=padx_exe, side = "left")

    # Create export button
    button1 = ttk.Button(frame_exe, text="エクスポート", command=export_clicked)
    button1.pack(fill = "x", padx=padx_exe, side = "left")

    # Create cancel button
    button2 = ttk.Button(frame_exe, text=("閉じる"), command=quit)
    button2.pack(fill = "x", padx=padx_exe, side = "left")
    
    # Create vin list display frame
    frame_list = ttk.Frame(root, padding=10, width=200, height=100)
    frame_list.grid(row=3,column=1,sticky=tk.W)

    # column_list = ttk.Frame(root, padding=10, width=200, height=100)
    # column_list.grid(row=3,column=1,sticky=tk.W)

    root.mainloop()