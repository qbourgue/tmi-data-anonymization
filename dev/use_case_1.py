#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import sys


#db_age_csv = pd.read_csv('../base_de_donnees/nais2016_id.csv', usecols=['DEPDOM', 'AGEXACTM', 'AGEXACTP'], index_col='DEPDOM')

##############################################################
# PLOT BARS

def plot_means_bars(file_):
    print("######## plot_means_bars #########")
    db_age_csv = pd.read_csv(file_, usecols=['DEPDOM', 'AGEXACTM', 'AGEXACTP'], index_col='DEPDOM')
    depdom_means = db_age_csv.groupby('DEPDOM').mean()
    np_means = depdom_means.reset_index().to_numpy()
    print(np_means)
    
    ind = np.arange(1, 110) 
    x_depdom = np_means[:,0]
    y_agem = np_means[:,1]

    z_agep = np_means[:,2]
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.xlim(0, 110)
    plt.ylim(24,37)
    
    width = 0.4
    shift = 0.5*width
    rects1 = ax.bar(ind-shift, y_agem, width, color='r')
    rects2 = ax.bar(ind+shift, z_agep, width, color='b')
    
    ax.set_ylabel('Âge moyen')
    ax.set_xlabel('Départements')
    ax.set_xticks(ind)
    ax.legend( (rects1[0], rects2[0]), ('Mère', 'Père') )
    
    #plt.show()

##############################################################
# PLOT HISTOGRAM 

def plot_hist_dprt(file_, dprt_id = 69):
    db_age_csv = pd.read_csv(file_, usecols=['DEPDOM', 'AGEXACTM', 'AGEXACTP'], index_col='DEPDOM')
    depdom_grpby = db_age_csv.loc[dprt_id]
    np_dprt = depdom_grpby.to_numpy() 

    fig = plt.figure()
    ax = plt.subplot(111)  
    plt.hist(np_dprt[:,:2], label=['Mère', 'Père'])
    plt.legend(loc='upper right')
    plt.show()


##############################################################
# PLOT EXEC

if __name__ == "__main__":
    if len(sys.argv) == 1:
        file1 = '../base_de_donnes/nais2016_id.csv'
        file2 = None
    elif len(sys.argv) == 2:
        file1 = sys.argv[1]
        file2 = None
        plot_means_bars(file1)
        #plot_hist_dprt(file1, 35)
        plt.show()
    elif len(sys.argv) == 3:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        plot_means_bars(file1)
        plot_means_bars(file2)
        plt.show()
    else:
        print("0, 1 or 2 argument(s) are accepted, not more")

#plot_hist_dprt()

