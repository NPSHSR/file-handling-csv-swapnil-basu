import pickle

def store():
    with open('Myfile.bin', 'wb') as f:
        emp = ['Rahul', 25, 'Manger']
        pickle.dump(emp)

