import pickle

data = {'members': {'Alice', 'Bob', 'Charlie'}}
with open('sample11_5_1.pickle', 'wb') as f:
    pickle.dump(data,f)