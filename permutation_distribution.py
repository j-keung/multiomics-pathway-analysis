
import pandas as pd
import os
import pickle

#Download the initial test statistics
df = pd.read_csv('metabolomics/Data/initial_tstats.csv', index_col=0)

path = os.getcwd() + '/metabolomics/Results_pickled'

final_list = []

for filename in os.listdir(path):
    file_num = int(filename[3:-4])
    if file_num < 101:
        with open(os.path.join(path, filename), 'rb') as f: # open in readonly mode
            list1 = pickle.load(f)
        final_list.append(list1)



sig_edges = []
edgelist = df.index

for index,pathway_pair in enumerate(edgelist):   #test all pathways
    comparison = df.Initial_tstat[index]    #get initial test statistic
    counter = 0
    
    for list1 in final_list:  #len(final_list) = number of permutations
        if abs(list1[index]) >= comparison:   
            counter += 1
    
    p_val = (counter/len(final_list))    #divide number of tests above or equal to the test statistic by total number of tests

    if p_val < 0.01:  #for 100,000 permutations
        sig_edges.append(pathway_pair)  
        
print(len(sig_edges))

with open ('metabolomics/Data/sig_edges.txt', 'w') as file:
     file.write(';'.join(str(i) for i in sig_edges))