
import pandas as pd
import os
import random
import pickle


#Download the initial test statistics
df = pd.read_csv('integrated/Data/initial_tstats.csv', index_col=0)



index = random.randrange(0, len(df)) #Gives index from 0 to (len(df)-1), better for indexing with unpickled files which are stored as lists
pathway_list = []

for i in range(1,11): #go through each of the 10 folders that have 10k in
    path = os.getcwd() + '/integrated/Results' + str(i)
    
    for filename in os.listdir(path):
        with open(os.path.join(path, filename), 'rb') as f: # open in readonly mode
            list1 = pickle.load(f)
        pathway_list.append(list1[index])

with open('integrated/Data/test_distribution'+str(index)+'.txt', 'w') as file:
    file.write(','.join(str(i) for i in pathway_list))






