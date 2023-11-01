
This repository contains the scripts for a MSc project, undertaken with the supervision of Pr. Timothy Ebbels and Cecilia Wieder.

### Aims
Converting single omics data into pathway scores facilitates the biological interpretation and data integration process of multi-omics data, allows comparison of different disease or treatment groups, and provides a more holistic view of the biological processes underlying disease. Using single sample pathway analysis, pathway scores for individual samples can be calculated to study inter-pathway associations and construct pathway level networks. This project aimed to assess the effectiveness of a pathway level differential network approach constructed using permutation testing. 

### Methods
The differential network approach was compared against a ‘naïve difference’ network approach, formed by taking the difference in edges between two condition-specific correlation networks. Using a COVID-19 dataset, differentially abundant pathway associations were identified between groups split into a mild and severe phenotype. 

The scripts in this repository analyse the proteomic and metabolomic datasets from a recent paper by Su et al. studying COVID, which can be accessed at:
Multi-Omics Resolves a Sharp Disease-State Shift between Mild and Moderate COVID-19 (Su et al., 2020)
DOI: 10.1016/j.cell.2020.10.037

The method for conversion to pathway scores was conducted using the sspa package, developed by Wieder et al.:
Single sample pathway analysis in metabolomics: performance evaluation and application (Wieder et al., 2022)
DOI: 10.1186/s12859-022-05005-1
