
import pandas as pd
import os
import pickle

#Download the initial test statistics
df = pd.read_csv('metabolomics/Data/initial_tstats.csv', index_col=0)

path = os.getcwd() + '/metabolomics/Results_pickled_100k'

final_list = []

#for filename in os.listdir(path):
#    file_num = int(filename[3:-4])
#    if file_num < 10001:
#        with open(os.path.join(path, filename), 'rb') as file: # open in readonly mode
#            list1 = pickle.load(file)
#        final_list.append(list1)
        
        
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
        


with open ('metabolomics/Data/vals.txt', 'w') as file:
     file.write(';'.join(str(i) for i in num_vals))