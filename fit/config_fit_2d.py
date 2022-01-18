
## Variables to change

# Common use (to use with one file or several)
wspace_name = "JpsiDstar_wspace"
wspace_root = "JpsiDstar_2Dfit.root"
save_fit_2d = "JpsiDstar_2Dfit.png"
save_fit_dstar = "Dstar_component_2Dfit.png"
save_fit_jpsi = "Jpsi_component_2Dfit.png"
save_correlation_JpsiDstar = "JpsiDstar_correlation.png"

## Variables for only one file fit

# Path for the single file
data_file_path = "Data_to_fit/dstar_charmonium_2018B.root"

## Variables for several files fit

# Eras
ERAS = ['B', 'C', 'D', 'E', 'F']
# Path for the files
save_path = "/afs/cern.ch/work/m/mabarros/public/CMSSW_10_6_12/src/OniaOpenCharmRun2ULAna/fit/Data_to_fit/"
# Datasets
dataset = "Charmonium2017"
# Luminosity
lumi = "41.5 fb^{-1}"

dict_fls = {
    # Workspace name
    "wspace_name" : wspace_name,
    # root file with single file data
    "savesave_path_single_file_path" : data_file_path,
    # Root file with all parameters saved by the workspace
    "wspace_root" : wspace_root,
    # Name of the figure with the fiting
    "save_fit_2d" : save_fit_2d,
    # Dstar component of the fit
    "save_fit_dstar" : save_fit_dstar,
    # Jpsi component of the fit
    "save_fit_jpsi" : save_fit_jpsi,
    # 2D mass plot correlation
    "save_correlation_JpsiDstar" : save_correlation_JpsiDstar,
    # Eras to be used in case of huge amount of data
    "eras": ERAS,
    # Datasets to be used
    "dataset": dataset,
    # path for the several files
    "save_path" : save_path,
}

# Dict with gourmetization for plotting
colors = {"model" : 2, "signal" : 4, "background" : 3}

styles = {"model" : 1, "signal" : 1, "background" : 2}



#--------------------- Some interesting paths/files ---------------------#

### Jpsi + Dstar

## Usual file
#../output/Charmonium2018B_test/DstarJpsi_asso_charmonium_2018B.root

##  File that contains a cut on D* mass before association
# ../output/test_cut_background_2d/DstarJpsi_DstardmCut_asso_charmonium_2018B.root 