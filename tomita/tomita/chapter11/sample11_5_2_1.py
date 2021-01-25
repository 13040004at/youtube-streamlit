import pickle
from chapter11.sample11_5_2 import Person

alice = Person('Alice', 23, 'F')
with open('sample11_5_2.pickle', 'wb') as f:
    pickle.dump(alice,f)
