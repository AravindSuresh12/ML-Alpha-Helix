# ML-Alpha-Helix

Predicting whether a Residue in a Protein can be a part of an Alpha-Helix or not based on the Residue Position- A Binary Classifier Approach. 
Part of coursework that I had done for BTRY6381 associated with Cornell University. 

Copyright (c) 2023 Aravind Sureshbabu.  
Robert Frederick Smith School of Chemical and Biomolecular Engineering.  
Cornell University, Ithaca NY 14850.  


Version 1.1

1) Made the ML model with 36 parameters for a given UniProt ID. (17 Amino Acids + 18 parameters + 1 UniProtID) 
2) The Precison recall of the model is 0.94 and the AUC is 0.84 
3) The predicting capability still needs further refining based on the top 15 parameter selection and further feature engineering


System requirements

1) Need Python 3.9 and above.. for scikit-learn 

How to use

Just run TestingFile.py and enter in a proper UniProt ID that corresponds to a protein. The results of 0 correspond to the amino acid not being a part of the alpha helix and 1 being the fact that amino acid is a part of an alpha helix.

Jupyter files (ipynb) in terms of TestingFile.ipynb and Finals.ipynb to get an interactive feel. Three ML models were compared with one another (Logistic Regression, RFC and DTC) and the best model was chosen based on precision, and f1 scores. Hyperparameter tuning was performed for the best chosen model

Future updates

1) Will include a detailed report that explains the whys of the process in the form of a report
2) Including a interactive cgi bin that also shows it in a webpage. 
3) Further fine tuning of the model to account for various sec and tert structure predictions
4) Updating README files
