import time
import tkinter.messagebox
import wmi
import tkinter
import tkinter as tk
root = tk.Tk()
root.withdraw()
f = wmi.WMI()
program = "MSIAfterburner.exe"
flag = 0
fail = 0
time.sleep(2)
while flag == 0:
    fail += 1
    print(fail)
    for process in f.Win32_Process():
        if "MSIAfterburner.exe" == process.Name:
            print("Application is Running")
            flag = 1
            exit()
            break
    if fail >= 1:
        print("not on")
        tkinter.messagebox.showwarning(title="MSI AFTERBURNER",
                                       message="Turn On Msi AfterBurner Lmao (Shits buggy, just open afterburner for like 4 seconds after pressing ok if the fans are already on)")

