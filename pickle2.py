import pickle

filename="amit.pk1"
fileob=open(filename,'rb')
b=pickle.load(fileob)
print(b)
