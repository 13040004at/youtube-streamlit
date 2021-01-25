import os
import pickle

def save_file(patients):
    f = open('patient_list.bin', 'wb')
    pickle.dump(patients, f)

def load_file():
    if os.path.exists('./patient_list.bin'):
        f = open("./patient_list.bin", "rb")
        return pickle.load(f)
    else:
        return None
