#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import sys
###
# matplotlib options

font = {'family' : 'normal',
        'size'   : 24}

plt.rc('font', **font)

##############################################################
# PLOT BARS

def plot_means_bars(file_, file_anon):
    print("######## plot_means_bars #########")
    db_age_csv = pd.read_csv(file_, usecols=['DEPDOM', 'AGEXACTM', 'AGEXACTP'], index_col='DEPDOM', dtype={'DEPDOM': object})
    anon_db_age_csv = pd.read_csv(file_anon, usecols=['DEPDOM', 'AGEXACTM', 'AGEXACTP'], index_col='DEPDOM', dtype={'DEPDOM': object})

    depdom_means = db_age_csv.groupby('DEPDOM').mean()
    anon_depdom_means = anon_db_age_csv.groupby('DEPDOM').mean()

    departements = ['22', '29', '35', '56', '75', '77', '78', '91', '92', '93', '94', '95', '974', '975', '976', '977']
    np_means = depdom_means.loc[departements].reset_index().to_numpy()
    anon_np_means = anon_depdom_means.loc[departements].reset_index().to_numpy()
    
    # x_depdom = np_means[:,0]
    # print(x_depdom)
    y_agem = np_means[:,1]
    print(y_agem)
    z_agem_anon = anon_np_means[:,1]
    print(z_agem_anon)
    
    y_agep = np_means[:,2]
    z_agep_anon = anon_np_means[:,2]

    plot_age_dep(departements, y_agem, z_agem_anon, 'de la mère')
    plot_age_dep(departements, y_agep, z_agep_anon, 'du père')
    plt.show()

def plot_age_dep(departements, y_age, z_age_anon, parent_str):
    ind = np.arange(1, len(departements)+1)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ##plt.xlim(0, 17)
    plt.ylim(26,38)
    
    width = 0.4
    shift = 0.5*width
    rects1 = ax.bar(ind-shift, y_age, width, color='yellowgreen')
    rects2 = ax.bar(ind+shift, z_age_anon, width, color='deepskyblue')
    
    ax.set_xlabel('Départements', fontsize=24)
    ax.set_ylabel('Âge', fontsize=24)
    #ax.set_xticks(ind.tolist(), x_depdom.tolist())
    plt.xticks(ind.tolist(), departements)
    ax.legend( (rects1[0], rects2[0]), ('Données originales', 'Données anonymisées') )
    title = 'Âge moyen ' + parent_str + ' en fonction du département'
    plt.title(title, fontsize=24)


# PLOT EXEC

if __name__ == "__main__":
    if len(sys.argv) == 1:
        file1 = '../base_de_donnes/nais2016_id.csv'
        file2 = None
    elif len(sys.argv) == 2:
        file1 = sys.argv[1]
        file2 = None
        plot_means_bars(file1, file2)
        #plot_hist_dprt(file1, 35)
        plt.show()
    elif len(sys.argv) == 3:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        plot_means_bars(file1, file2)
        plt.show()
    else:
        print("0, 1 or 2 argument(s) are accepted, not more")

#plot_hist_dprt()

