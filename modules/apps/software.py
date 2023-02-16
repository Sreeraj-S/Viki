import os
import pickle

file = open("data\\localdata\\application1.bat",'rb')
path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs"
applications = pickle.load(file)
software = applications['software']
uninstall = applications['uninstall']
file.close()

def open_Software(app):
    availSoftware = [i for i in software if app in i]
    if len(availSoftware)==1:
        os.startfile(software[app])
        return "opening..."
    elif len(availSoftware)==0:
        return "Not software found"
    else:
        return availSoftware

def sel_Software(availSoftware, index):
    try:
        os.startfile(software[availSoftware[index]])
        return "opening..."
    except:
        return "Choice not found"

def show_Software():
    print(list(software.keys()))
    print(list(uninstall.keys()))

if __name__ == "__main__":
    show_Software()
    open_Software("destop")
