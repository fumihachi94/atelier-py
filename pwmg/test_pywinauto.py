# hwllo world of pywinauto lib

import time, sys
import ctypes
from subprocess import Popen
from pywinauto import Desktop
import win32gui
import win32con
import win32process
import win32api
import win32security
from tkinter import messagebox, Button, Tk, Canvas, Label

def remove_unsupported_characters(string, encoding = 'cp932'):
    return string.encode(encoding, errors='ignore').decode(encoding)

def get_active_window_title():
    return win32gui.GetWindowText(win32gui.GetForegroundWindow())

def get_title_string(title):
    return remove_unsupported_characters(title)

def readPass(filepath):
    try:
        with open(filepath, 'r') as f:
            pwlist = f.read().split("\n")
            pwlist = list(filter(None, pwlist))
            return pwlist
    except FileNotFoundError:
        print('FileNotFoundError: The file "' + filepath + '"  is not found.')
        sys.exit('System exit [Error]')

def getExeFileName(processHandle):
    exeFileName = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
    length = ctypes.wintypes.DWORD(ctypes.wintypes.MAX_PATH)
    if ctypes.windll.Kernel32.QueryFullProcessImageNameW(processHandle, 0, exeFileName, ctypes.byref(length)):
        return exeFileName.value
    else:
        return None


# --------------------------------

pwlist = readPass("./data/pw.txt")
print(pwlist)

# Popen('test.docx', shell=True)

while True:

    win_title = get_active_window_title()
    pass_window = Desktop(backend='uia')[win_title]
  
    if 'パスワード' in win_title:

        # # Messagebox using for pw search chancel  
        # if messagebox.showinfo('Confirm', 'パスワード探索を中止しますか？')=="True":
        #     continue


        handle = ctypes.windll.user32.FindWindowW(
            0, get_title_string(win_title)
        )
        handle2 = win32gui.GetWindow( handle, win32con.GW_HWNDNEXT)	
        length = win32gui.SendMessage(handle2, win32con.WM_GETTEXTLENGTH, 0, 0)
        buff = ctypes.create_unicode_buffer(length + 1)
        win32gui.SendMessage( handle2, win32con.WM_GETTEXT, length+1, buff)
        win_title = buff.value

        pass_window = Desktop(backend='uia')[win_title]
        print(win_title)
        # print(pass_window)
    else:
        continue
    

    if pass_window[u'パスワード'].exists():
        print(u'パスワードWindow発見！')
        file_open_flg = False
        for pw in pwlist:
            if pass_window[u'OK'].exists():
                pass_window[u'パスワード'].Edit.set_edit_text(pw)
                pass_window[u'OK'].click()
                time.sleep(0.3)
                if pass_window[u'OK'].exists():
                    # handle = ctypes.windll.user32.FindWindowW(0, get_title_string(win_title))
                    pids = win32process.GetWindowThreadProcessId(handle2)
                    for pid in sorted(pids):
                        print("pids: ", pid)
                        # ph = win32api.OpenProcess(win32con.PROCESS_VM_READ | win32con.PROCESS_QUERY_INFORMATION , False, pid)
                        # print("ph: ", ph)
                        try:
                            ph = win32api.OpenProcess(win32con.PROCESS_VM_READ | win32con.PROCESS_QUERY_INFORMATION , False, pid)
                            print("ph: ", ph)
                        except:
                            print("ph:?")
                        else:
                            try:
                                mhs = win32process.EnumProcessModules(ph)
                                print("mhs: ", mhs)
                            except:
                                print("mhs:?")
                            else:
                                for mh in mhs:
                                    print("filename:", win32process.GetModuleFileNameEx(ph, mh))
                    # processModules = ctypes.windll.psapi.EnumProcessModules(hProcess[1])
                    # print("processModules: ", processModules)
                    # filename = win32process.GetModuleFileNameEx(hProcess[0], 0)
                    # print("path: ", filename)
                    pass_window[u'OK'].click()
                    win32gui.SendMessage( handle2, win32con.WM_CLOSE, 0, 0)
                else:
                    file_open_flg = True
                    break
            else:
                
                # handle = ctypes.windll.user32.FindWindowW(0, get_title_string(win_title))
                # hProcess = win32process.GetWindowThreadProcessId(handle)
                # filename = win32process.GetModuleFileNameEx(hProcess[1], 0)
                # processModules = ctypes.windll.psapi.EnumProcessModules(hProcess[1])
                # print("hProcess: ", hProcess)
                # print("path: ", processModules)
                Popen('test.docx', shell=True)
                while True:
                    pass_window = Desktop(backend='uia')[win_title]
                    if pass_window[u'パスワード'].exists():
                        break

        if file_open_flg:
            print(u'パスワードがみつかりました！：', pw)
        else:
            print(u'パスワードがみつかりません！')

            


