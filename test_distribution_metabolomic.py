import pandas as pd
import os
import random
import pickle

#Download the initial test statistics
df = pd.read_csv('metabolomics/Data/initial_tstats.csv', index_col=0)

path = os.getcwd() + '/metabolomics/Results_pickled_100k'

index = random.randrange(0, len(df)) #Gives index from 0 to (len(df)-1), better for indexing with unpickled files which are stored as lists
print(index)

pathway_list = []


#Get the permutation values for 5 randomly chosen pathway pairs
for i in range(5):
    for filename in os.listdir(path):
            if filename.startswith('Run'):
                with open(os.path.join(path, filename),'rb') as file:
                    list1 = pickle.load(file)   
                    #print(list1) 
                    #lines = file_in.readlines()
                    #pathway_stat = float(lines[0].split(',')[index])
                    pathway_list.append(list1[index])

    print(pathway_list)
    with open('metabolomics/Data/test_distribution'+str(index)+'.txt', 'w') as file:
        file.write(','.join(str(i) for i in pathway_list))


