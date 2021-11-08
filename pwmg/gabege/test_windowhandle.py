import ctypes
import win32gui
import win32con
from datetime import datetime
from win32gui import GetWindowText, GetForegroundWindow

from tkinter import Button, Tk, Canvas, Label

def remove_unsupported_characters(string, encoding = 'cp932'):
    return string.encode(encoding, errors='ignore').decode(encoding)

def get_active_window_title():
    return GetWindowText(GetForegroundWindow())

def get_title_string(title):
    return remove_unsupported_characters(title)


class GetWindowHandle(Canvas):
    # コンストラクタ
    def __init__(self, master):
        # 親クラスのコンストラクタ
        super().__init__(master, bg="white")

        # パスワード入力するためのウィンドウハンドルNo
        self.handlenum = ""

        self.wt=Label(self, 
            text='パスワード入力ウィンドウを選択してください',
            bg="white", font=("",15))
        self.wt.grid(row=0, column=0, columnspan=2, ipady=1, sticky="news")

        # Window Handlw1 表示用
        self.wh=Label(self, bg="white", font=("",15))
        self.wh.grid(row=1, column=0, columnspan=2, sticky="news")

        self.ok_btn=Button(self, text = "OK",     command = self.master.destroy)
        self.cl_btn=Button(self, text = "Cancel", command = self.master.destroy)
        self.ok_btn.grid(row=2, column=0, columnspan=1, sticky="news")
        self.cl_btn.grid(row=2, column=1, columnspan=1, sticky="news")

        
    # 表示を更新
    def update(self):

        win_title = get_active_window_title()
        handle = ctypes.windll.user32.FindWindowW(
                0, get_title_string(win_title)
            )

        self.wh.configure(text='Window Handle: '+hex(handle))

        if win_title.lower() in ['パスワード' ,'password', 'pass word']:
            self.handlenum = hex(handle)
            print("ok : " + self.handlenum)
            cid = win32gui.GetDlgCtrlID(handle)
            cls = win32gui.GetClassName(handle)
            length = win32gui.SendMessage(handle, win32con.WM_GETTEXTLENGTH, 0, 0)
            buff = ctypes.create_unicode_buffer(length + 1)
            win32gui.SendMessage( handle, win32con.WM_GETTEXT, length+1, buff)
            print(cid, cls, buff.value)

            hchild = win32gui.GetWindow( handle, win32con.GW_CHILD)	
            length = win32gui.SendMessage(hchild, win32con.WM_GETTEXTLENGTH, 0, 0)
            buff = ctypes.create_unicode_buffer(length + 1)
            win32gui.SendMessage( hchild, win32con.WM_GETTEXT, length+1, buff)
            print(buff.value)

            # ctypes.windll.user32.SendMessageW(handle, win32con.WM_CHAR, 0x61, 0)


            handle2 = win32gui.GetWindow( handle, win32con.GW_HWNDNEXT)	
            length = win32gui.SendMessage(handle2, win32con.WM_GETTEXTLENGTH, 0, 0)
            buff = ctypes.create_unicode_buffer(length + 1)
            win32gui.SendMessage( handle2, win32con.WM_GETTEXT, length+1, buff)
            print(buff.value)


            hWnd_child = get_hwnd_search_control(handle, 0,0, "OK")
            print( "ターゲットのハンドル", hex(hWnd_child))

            result = win32gui.PostMessage( handle, win32con.BM_CLICK, 0, 0)
            print(result)

            rect = win32gui.GetWindowRect(handle)
            print("ターゲットの位置：", rect)
            txt  = win32gui.GetWindowText(
                
            )
            print("ターゲットのテキスト：", txt)



        # 200ms周期で再表示
        self.master.after(200, self.update)

# 単独処理の場合
def main():
    # メインウィンドウ作成
    root=Tk()

    # メインウィンドウタイトル
    root.title("window select")

    # メインウィンドウサイズ
    root.geometry("512x384")

    # 常に最前面に表示
    root.attributes("-topmost", True)

    # メインウィンドウの背景色
    root.configure(bg="white")

    # Clock クラスのインスタンスを生成
    win_handle=GetWindowHandle(root)

    # 画面に配置
    win_handle.pack(expand=1)

    # update メソッド呼び出し
    win_handle.update()

    # メインループ
    root.mainloop()



def get_hwnd_search_control(hWnd, target_control_id, target_control_class, target_control_title):
	try:
		htarget = 0
	
		if hWnd != 0 :
			# チェック情報取得
			cid = win32gui.GetDlgCtrlID( hWnd)
			cls = win32gui.GetClassName( hWnd)
			
			# ターゲットテキスト取得
			length = win32gui.SendMessage(hWnd, win32con.WM_GETTEXTLENGTH, 0, 0)
			buff = ctypes.create_unicode_buffer(length + 1)
			win32gui.SendMessage( hWnd, win32con.WM_GETTEXT, length+1, buff)

			# チェック
			if win32gui.IsWindowVisible(hWnd) :
				if target_control_id == 0 or target_control_id == cid:
					if target_control_class == 0 or target_control_class == cls :
						if target_control_title == "" or target_control_title == buff.value:
							# ターゲット確認
							htarget = hWnd
						
			# 渡されたハンドルがNGの場合、その子およびその階層をチェック
			if htarget == 0 :
				hChild = win32gui.GetWindow( hWnd, win32con.GW_CHILD)
				while (hChild):
					htmp = get_hwnd_search_control( hChild, target_control_id, target_control_class, target_control_title)
					if htmp != 0 :
						htarget = htmp
						break
				
					hChild = win32gui.GetWindow( hChild, win32con.GW_HWNDNEXT)	
		else:
			htarget = 0

		return htarget
		
	except Exception as err:
		# 取得失敗
		print("【ERROR】get_hwnd_search_control【ERROR】")
		print (err)
		return 0






if __name__ == "__main__":
    main()
