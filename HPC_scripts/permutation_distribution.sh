#!/bin/bash
#PBS -lwalltime=08:00:00 
#PBS -lselect=1:ncpus=1:mem=100gb:cpu_type=rome
#PBS -J 1-10
#PBS -o /rds/general/user/jmk122/home/MSc/project_2/metabolomics/logs_project2/  
#PBS -e /rds/general/user/jmk122/home/MSc/project_2/metabolomics/logs_project2/   



cd $PBS_O_WORKDIR

Logfile="debug2.out"

module load anaconda3/personal
source activate project_2   

echo "Task started at " `date` > $Logfile  2>&1 
echo "Using Python" `python --version` >> $Logfile  2>&1 

python permutation_distribution_all.py $PBS_ARRAY_INDEX

echo "Task finished at " `date` >> $Logfile  2>&1 