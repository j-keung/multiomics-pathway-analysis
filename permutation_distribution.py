
import pandas as pd
import os


#Download the initial test statistics
df = pd.read_csv('metabolomics/Data/initial_tstats.csv', index_col=0)

path = os.getcwd() + '/metabolomics/Results'

edgelist = df.index


pathway_list = []
sig_edges = []

for index,pathway_pair in enumerate(edgelist[:5]):   #test all pathways
    for filename in os.listdir(path):
        if filename != 'initial_tstats.csv':
            with open(os.path.join(path, filename)) as file_in:    
                lines = file_in.readlines()
                pathway_stat = float(lines[0].split(',')[index])
                pathway_list.append(pathway_stat)
    
    print(pathway_list, pathway_pair)

    comparison = df.Initial_tstat[index]    #get initial test statistic
    print(comparison)
    counter = 0
    
    for num in pathway_list:  #len(pathway_list) = number of permutations
        if abs(num) >= comparison:   
            counter += 1
    
    print(counter)
    p_val = (counter/len(pathway_list))    #divide number of tests above or equal to the test statistic by total number of tests

    if p_val < 0.01:  #for 100,000 permutations
        sig_edges.append(pathway_pair)  

    pathway_list = []

print(sig_edges)

with open ('metabolomics/Data/sig_edges.txt', 'w') as file:
     file.write(','.join(str(i) for i in sig_edges))