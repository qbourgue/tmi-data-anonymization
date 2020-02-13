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
    db = pd.read_csv(file_, usecols=['ID', 'ID_swap'])
    delta_Id = abs(db['ID'] - db['ID_swap']) 
    print('Time for result')
    print('Mean rank swap : ',delta_Id.mean())
    print('Max rank swap : ', delta_Id.max())
    print('Min rank swap : ', delta_Id.min())
    print('STD rank swap : ', delta_Id.std())
    print('Var rank swap : ', delta_Id.var())


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

