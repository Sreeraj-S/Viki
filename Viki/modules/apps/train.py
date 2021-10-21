import os
import pickle

def train():
    file = open("data\\localdata\\application.bat",'wb')
    path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs"
    software = {}
    errortime = 0

    for dirpath, dirnames, filenames in os.walk(path):
                for filename in filenames:
                    full_path = os.path.join(dirpath, filename)
                    try:
                        filename = filename.replace(".ini","")
                        filename = filename.replace(".lnk","")
                        full_path = full_path.replace("\\","\\\\")
                        software[filename] = full_path
                    except (OSError,):
                        errortime+=1
                        continue   
    pickle.dump(software, file)
    file.close()
    return f"Trained with {errortime} error" 

if __name__ == "__main__":
    train()