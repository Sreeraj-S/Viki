import os
import pickle
import time

def train():
    file = open("data\\localdata\\application1.bat",'wb')
    path = ["C:","D:","E:"]
    software = {}
    uninstall = {}
    errortime = 0
    print('Starting...')
    for i in path:
        print('Drive: ',i)
        for dirpath, dirnames, filenames in os.walk(i):
                for filename in filenames:
                    full_path = os.path.join(dirpath, filename)
                    try:
                        filename = filename.replace(".ini","").lower()
                        filename = filename.replace(".exe","").lower()
                        filename = filename.replace(".lnk","").lower()
                        full_path = full_path.replace("\\","\\\\")
                        if 'uninstall' in filename:
                            uninstall[filename] = full_path
                        else:
                            software[filename] = full_path
                    except (OSError,):
                        errortime+=1
                        continue  
    pickle.dump({'software':software,'uninstall':uninstall}, file)
    file.close()
    return f"Trained with {errortime} error" 

if __name__ == "__main__":
    train()