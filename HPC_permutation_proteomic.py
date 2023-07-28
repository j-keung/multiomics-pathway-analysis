#Load libraries 

import pandas as pd
import sspa
import scipy
import numpy as np 
import random
import pickle
import sys #to get the array job number when running an array job with the HPC


#Load dataset
df = pd.read_csv('proteomics/Data/Su_COVID_proteomics_processed_commoncases.csv', index_col=0)

#Download the reactome pathways
reactome_pathways = sspa.process_reactome('Homo sapiens', infile = 'proteomics/Data/UniProt2Reactome_All_Levels.txt', download_latest = False, filepath = None)

#Download the root pathways
root_path = pd.read_excel('proteomics/Data/Root_pathways.xlsx', header=None)
root_pathway_dict = {root_path[0][i]:root_path[1][i] for i in range(0,len(root_path))}
root_pathway_names = list(root_pathway_dict.keys())



#Make a dictionary with the WHO status for each sample
sample_dict = {sample:df["WHO_status"][sample] for sample in df.index}
sample_names = list(df.index)
random.shuffle(sample_names)

#Make a copy of the original dataframe but replace with the shuffled labels
df_shuffled = df.copy()
df_shuffled.index = sample_names

#Change the WHO status to match the shuffled label
for sample in df_shuffled.index: 
        df_shuffled.loc[sample,"WHO_status"] = sample_dict[sample]

df_mild = (df_shuffled[df_shuffled["WHO_status"] == '1-2']).iloc[:,:-2] #45 samples, remove the metadata
df_severe = (df_shuffled[(df_shuffled["WHO_status"] == '3-4') | (df_shuffled["WHO_status"] == '5-7')]).iloc[:,:-2] #83 samples




#Function to calculate the squared Spearman correlation matrix 

def squared_spearman_corr(data):
    kpca_scores = sspa.sspa_kpca(data, reactome_pathways)   
    kpca_scores = kpca_scores.drop(columns = list(set(root_pathway_names) & set(kpca_scores.columns))) #using Sara's code to drop root pathways

    spearman_results = scipy.stats.spearmanr(kpca_scores)
    squared_spearman_coef = np.square(spearman_results[0]) #correlation coefficients (spearman_results[1] gives the p-values)

    return squared_spearman_coef,list(kpca_scores.columns)




#Function to calculate the difference between two matrices and then determine the mean for each edge

def delta_squared_list(data1,data2,edgelist):
    delta_squared = (np.array(data1) - np.array(data2))

    #Mask the upper half of the dataframe (so I don't view the comparisons between the two same genes, and also the duplicate comparisons are removed)
    mask = delta_squared.copy()
    mask = np.triu(np.ones(mask.shape)).astype(bool)
    mask = np.invert(mask) #invert true and false values so the diagonal is False as well
    non_dup_delta_squared = pd.DataFrame(delta_squared, columns = edgelist, index = edgelist)
    non_dup_delta_squared = pd.DataFrame(non_dup_delta_squared).where(mask) #Replace all false values with NaN using mask

    delta_squared_list = non_dup_delta_squared.stack().reset_index()
    finallist = list(delta_squared_list[0])

    return(finallist)



spearman_mild,edgelist = squared_spearman_corr(df_mild)
spearman_severe,edgelist = squared_spearman_corr(df_severe)

output = delta_squared_list(spearman_mild,spearman_severe,edgelist)


index_num = sys.argv[1]  #this should return the array number within the array job
folder_num = sys.argv[2]

with open('proteomics/Results'+folder_num+'/Run'+index_num + '.txt', "wb") as file:  
       pickle.dump(output,file)