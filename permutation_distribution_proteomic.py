
import sys
import pandas as pd
import os
import pickle


#Download the initial test statistics
df = pd.read_csv('proteomics/Data/initial_tstats.csv', index_col=0)

#Get number of array job, which corresponds to one of the folders that contain 10k permutation values
index_num = sys.argv[1]
path = os.getcwd() + '/proteomics/Results' + str(index_num) 

final_list = []

        
for filename in os.listdir(path):
  with open(os.path.join(path, filename), 'rb') as file: # open in readonly mode
    list1 = pickle.load(file)
  final_list.append(list1)



num_vals = []  #number of permuted values above the magnitude of the test statistic
edgelist = df.index

for index,pathway_pair in enumerate(edgelist):   #test all pathways
    comparison = df.Initial_tstat[index]    #get initial test statistic
    counter = 0
    
    for list1 in final_list:  #len(final_list) = number of permutations
        if abs(list1[index]) >= comparison:   
            counter += 1
    num_vals.append(counter)
        

with open ('proteomics/Data/vals'+str(index_num)+'.txt', 'w') as file:
     file.write(';'.join(str(i) for i in num_vals))