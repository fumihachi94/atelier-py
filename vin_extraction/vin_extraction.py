import pandas as pd
import re
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

g_filepath = "./sampledata.txt"
g_vinlist  = []
g_vinpd    = pd.DataFrame()
g_colname  = "ＶＩＮ／プレート打刻情報"

def readVIN(filepath):
    global g_vinlist, g_vinpd
    n = 0
    p = r'"(.*?)"'
    data = []

    with open(filepath) as f:
        for line in f:
            if line[0] == "#":
                continue
            else:
                n = n+1
                # 正規表現でlistとして抽出
                r = re.findall(p, line) 
                if n == 1:
                    column_list = r
                else:
                    data.append(r)
            # if n > 3: break

        # Create pandas data frame and delete VIN duplicate elements. 
        df = pd.DataFrame(data, columns=column_list).drop_duplicates()
        print(df[g_colname])

        g_vinpd   = df[g_colname].copy()
        g_vinlist = df[g_colname].tolist()
        list_value = tk.StringVar(value=g_vinlist)
        Listbox = tk.Listbox(frame_list, listvariable=list_value, height=15)
        Listbox.pack(padx=10)


# ファイル指定
def filedialog_clicked():
    global g_filepath
    iDir = os.path.abspath(os.path.dirname(__file__))
    filepath = filedialog.askopenfilename(initialdir = iDir)
    g_filepath = filepath
    entry1.set(filepath)
    
    
# 実行
def exeVINExtraction():
    readVIN(g_filepath)

# エクスポート
def export_clicked():
    g_vinpd.to_csv('./test.csv', header=True)
    print("Export完了")





if __name__ == "__main__":

    # rootの作成
    root = tk.Tk()
    root.title("VIN Extraction")

    # Frameの作成
    frame_select = ttk.Frame(root, padding=10)
    frame_select.grid(row=0, column=1, sticky=tk.W)

    # 「ファイル参照」ラベルの作成
    IDirLabel = ttk.Label(frame_select, text="ファイル", padding=(5, 2))
    IDirLabel.pack(side=tk.LEFT)
    
    # 「ファイル参照」エントリーの作成
    entry1 = tk.StringVar()
    IDirEntry = ttk.Entry(frame_select, textvariable=entry1, width=30)
    IDirEntry.pack(side=tk.LEFT)

    # 「フォルダ参照」ボタンの作成
    IDirButton = ttk.Button(frame_select, text="参照", command=filedialog_clicked)
    IDirButton.pack(side=tk.LEFT)

    # Frameの作成
    padx_exe = 10
    frame_exe = ttk.Frame(root, padding=10)
    frame_exe.grid(row=2,column=1,sticky=tk.W)

    # 実行ボタンの設置
    button1 = ttk.Button(frame_exe, text="実行", command=exeVINExtraction)
    button1.pack(fill = "x", padx=padx_exe, side = "left")

    # 実行ボタンの設置
    button1 = ttk.Button(frame_exe, text="エクスポート", command=export_clicked)
    button1.pack(fill = "x", padx=padx_exe, side = "left")

    # キャンセルボタンの設置
    button2 = ttk.Button(frame_exe, text=("閉じる"), command=quit)
    button2.pack(fill = "x", padx=padx_exe, side = "left")
    
    # Frameの作成
    frame_list = ttk.Frame(root, padding=10, width=200, height=100)
    frame_list.grid(row=3,column=1,sticky=tk.W)

    # VIN Listの作成
    # list_value = tk.StringVar(value=g_vinlist)
    # Listbox = tk.Listbox(frame_list, listvariable=list_value, height=15)
    # Listbox.pack(padx=10)
    


    root.mainloop()