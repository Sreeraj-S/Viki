import os
import pickle

def open_Software(app):
    file = open("data\\localdata\\application.bat",'rb')
    path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs"
    software = pickle.load(file)
    file.close()
    try:
        os.startfile(software[app])
    except:
        return "Not software found"

def show_Software():
    file = open("data\\localdata\\application.bat",'rb')
    path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs"
    software = pickle.load(file)
    file.close()
    print(list(software.keys()))


if __name__ == "__main__":
    show_Software()
    open_Software("Desktop")
