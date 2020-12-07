import pickle
a=['Amit','sunny','surya']
filename="amit.pk1"
fileob=open(filename,'wb')
pickle.dump(a,fileob)
fileob.close()
