import pandas as pd
import os
import csv
import matplotlib.pyplot as plt
import math
import numpy as np
from sklearn.model_selection import train_test_split
def main():
    c_class= ['g1','g2','g3','g4','g5','g6']
    #seed_list = [17,50,100]
    seed =50
    train,test=[],[]

    #list_head_data = ['NUMBER', 'MAG_APER', 'MAGERR_APER', 'MAG_AUTO', 'MAGERR_AUTO', 'MAG_BEST', 'MAGERR_BEST', 'KRON_RADIUS', 'BACKGROUND', 'THRESHOLD', 'ISOAREA_IMAGE', 'ISOAREAF_IMAGE', 'ALPHAPEAK_J2000',
    #         'DELTAPEAK_J2000', 'X_IMAGE', 'Y_IMAGE', 'FWHM_IMAGE', 'FWHM_WORLD', 'ELONGATION', 'ELLIPTICITY', 'CLASS_STAR', 'FLUX_RADIUS', 'FILE_NAME','CLASS_OBJECT']
    data = pd.read_csv("Exp9Cluster6_merge_cluster7.csv",  header=0)
    data=data.drop('ALPHAPEAK_J2000_I', axis=1)
    data=data.drop('DELTAPEAK_J2000_I', axis=1)
    for c in c_class:
        datatrain, datatest = [], []
        data_each_class= data.loc[data['Cluster'] == c] 
        if (c=='g1'or c=='g2'):
            datatrain, datatest = train_test_split(data_each_class,test_size=0.4, random_state=seed, shuffle=True)
        else:
            datatrain = data_each_class.sample(n=300, replace=False, random_state=seed)
            datatest = pd.concat([data_each_class, datatrain, datatrain]).drop_duplicates(keep=False)

        #print(data['NUMBER'])
        #data = data.drop(data.index[0],axis = 0)
         
        train.append(datatrain)
        test.append(datatest)
    result_train = pd.concat(train)
    result_test = pd.concat(test)
    result_train.to_csv("train.csv",index = False) 
    result_test.to_csv("test.csv",index = False)
    return 0

if __name__ == "__main__":
    main()