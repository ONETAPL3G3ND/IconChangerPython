#https://github.com/ONETAPL3G3ND
import win32com.client

def change_icon(shortcut_path, icon_path):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.IconLocation = icon_path
    shortcut.Save()

# Пример использования:
shortcut_path = "C:\\Users\\User\\Desktop\\MyShortcut.lnk"
icon_path = "C:\\Path\\To\\Icon.ico"
change_icon(shortcut_path, icon_path)
