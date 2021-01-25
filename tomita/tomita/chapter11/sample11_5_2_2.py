import pickle

with open('sample11_5_2.pickle', 'rb') as f:
    obj = pickle.load(f)
    print(obj)