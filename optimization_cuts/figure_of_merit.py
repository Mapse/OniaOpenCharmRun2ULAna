import pandas as pd
import matplotlib.pyplot as plt

import config_fit_2d as config

import mplhep as hep
plt.style.use(hep.style.CMS)

def plot_fom(csv_file, x=config.case, type=config.type):

    '''
    This function is used to plot the figure of merit (FOM) in function of 
    a specfic cut.

    Parameters:
    
    csv_file (str): name of the csv file that contains the parameters. It is
    given in the config_fit_2d config file

    x (list): It contains all cuts for each FOM. It is given in the config file.
    Note that you should provide it in the right order!!

    type (str): The cut in study. Also given in the config file

    '''
    # Reads the csv file with pandas
    df = pd.read_csv(csv_file)

    # Create a subplots
    fig, ax = plt.subplots()

    # Xlabel
    ax.xaxis.set_label_coords(0.90, -0.055)
    ax.set_xlabel(type, fontsize = 22)
    
    # Ylabel
    ax.yaxis.set_label_coords(-0.09, 0.86)
    ax.set_ylabel(r'$S/\sqrt{(S + B)}$', fontsize = 22)
    ax.set_ylim(0, 10)
    
    # CMS format
    hfont = {'fontname':'Helvetica'}    
    plt.text(0.13, 0.89, "CMS", fontdict=hfont,  fontweight='bold', transform=plt.gcf().transFigure)
    plt.text(0.23, 0.89, "Preliminary", fontdict=hfont, style='italic',fontsize = 22, transform=plt.gcf().transFigure)
      
    plt.grid()

    y = df['FOM']
    yerror = df['FOM_err']
    x = x

    plt.errorbar(x, y, yerror, marker='D', markersize=10, linestyle='')

    plt.savefig('fom/' + type + '.png')

def chi2_ndf_fom_dstar(csv_file, type=config.type):

    '''
    This function is used to plot the figure of merit (FOM) in function of 
    a chi square of dstar fit.

    Parameters:
    
    csv_file (str): name of the csv file that contains the parameters. It is
    given in the config_fit_2d config file

    '''
    # Reads the csv file with pandas
    df = pd.read_csv(csv_file)

    # Create a subplots
    fig, ax = plt.subplots()

    # Xlabel
    ax.xaxis.set_label_coords(0.90, -0.055)
    ax.set_xlabel(type, fontsize = 22)
    
    # Ylabel
    ax.yaxis.set_label_coords(-0.09, 0.86)
    ax.set_ylabel(r'$S/\sqrt{(S + B)}$', fontsize = 22)
    ax.set_xlabel(r'$\chi^2/n.d.f - D^*$ fit', fontsize = 22)
    ax.set_ylim(0, 10)
    
    # CMS format
    hfont = {'fontname':'Helvetica'}    
    plt.text(0.13, 0.89, "CMS", fontdict=hfont,  fontweight='bold', transform=plt.gcf().transFigure)
    plt.text(0.23, 0.89, "Preliminary", fontdict=hfont, style='italic',fontsize = 22, transform=plt.gcf().transFigure)
      
    plt.grid()

    y = df['FOM']
    yerror = df['FOM_err']
    x = df['chi_square_dstar']

    plt.errorbar(x, y, yerror, marker='D', markersize=10, linestyle='')

    plt.savefig('fom/' + type +'fom_vs_chiSquareNDOF_dstar_fit.png')  

if __name__ == '__main__':

    plot_fom(config.csv_name)
    chi2_ndf_fom_dstar(config.csv_name)