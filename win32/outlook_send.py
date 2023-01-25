import win32com.client

# ----------------------------------------
# Outlookオブジェクトの設定
# ----------------------------------------
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
#mail = outlook.CreateItem(0)

print("test")