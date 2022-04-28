
## Main dict

cases={'Charmonium_2017_D0Dstar_dlSig1p0' : [{'fit_parameters' : {'mean_jpsi' : [3.09355, 3.05, 3.15], 'sigma_gauss' : [0.04, 0.000001, 1], 'sigma_cb' : [0.02, 0.000001, 1],
                                                                  'frac_gauss_jpsi' : [0.4, 0.0001, 1.0],  'frac_cb' : [0.6, 0.0001, 1.0], 'alpha' : 1.4, 'n' : 8.8,
                                                                  'exp_coef' : [-3.2, -7, 1], 'frac_exp' : [0.4, 0.0, 1.0], 'dstar_mean' : [0.145495, 0.142, 0.158],
                                                                  'dstar_sigma_1' : [0.00508973, 0.0001, 0.01], 'dstar_sigma_2' : [0.000456236, 0.0001, 0.01], 'gauss1_frac' : [0.3, 0, 1], 
                                                                  'gauss2_frac' : [0.3, 0, 1], 'p0' : [0.0004, -0.0003, 0.0009], 'p1' : [4.5, 4.4, 4.8], 'p2' : [0.15, 0.12, 0.18],}},
                                            {'files' : ['Charmonium_2017_D0Dstar_dlSig1p0_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_dlSig1p0_2Dfit.root',
                                                        'fit_plots/Charmonium_2017_D0Dstar_dlSig1p0_2Dfit.png', 'fit_plots/Dstar_component_2Dfit_dlSig1p0.png',
                                                        'fit_plots/Jpsi_component_2Dfit_dlSig1p0.png', 'fit_plots/Charmonium_2017_D0Dstar_dlSig1p0_correlation_dlSig1p0.png',
                                                        'data_root_files/Charmonium_2017_D0Dstar_dlSig1p0.root']}],} 


# Luminosity
lumi = "x fb^{-1}"

# Chi square
nparm_jpsi = 6
nparm_dstar = 8

# Dict with gourmetization for plotting
colors = {"model" : 2, "signal" : 4, "background" : 3}

styles = {"model" : 1, "signal" : 1, "background" : 2}

###################################### Config for yields and fom ######################################
yield_files = ['fit_root_files/Charmonium_2017_D0Dstar_cosphi0p990_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_cosphi0p985_wspace', 
               'fit_root_files/Charmonium_2017_D0Dstar_cosphi0p980_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_cosphi0p975_wspace',
               'fit_root_files/Charmonium_2017_D0Dstar_cosphi0p950_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_cosphi0p900_wspace',
               'fit_root_files/Charmonium_2017_D0Dstar_cosphi0p850_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_cosphi0p800_wspace',
               'fit_root_files/Charmonium_2017_D0Dstar_cosphi0p750_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_cosphi0p500_wspace',]
csv_name = 'fom/Charmonium_2017_D0Dstar_cosphi.csv'

case = [0.990, 0.985, 0.980, 0.975, 0.950, 0.900, 0.850, 0.800, 0.750, 0.500]

type = 'copshi'



##########################################################################################################################################################################################################################################
############################################################################################# Good configs ###############################################################################################################################
##########################################################################################################################################################################################################################################

########################################################################################### pt ###########################################################################################

cases_pt4={'Charmonium_2017_D0Dstar_pt4' : [{'fit_parameters' : {'mean_jpsi' : [3.09355, 3.05, 3.15], 'sigma_gauss' : [0.04, 0.000001, 1], 'sigma_cb' : [0.02, 0.000001, 1],
                                                                  'frac_gauss_jpsi' : [0.4, 0.0001, 1.0],  'frac_cb' : [0.6, 0.0001, 1.0], 'alpha' : 1.4, 'n' : 8.8,
                                                                  'exp_coef' : [-3.2, -7, 1], 'frac_exp' : [0.4, 0.0, 1.0], 'dstar_mean' : [0.145495, 0.142, 0.158],
                                                                  'dstar_sigma_1' : [0.00508973, 0.0001, 0.01], 'dstar_sigma_2' : [0.000456236, 0.0001, 0.01], 'gauss1_frac' : [0.3, 0, 1], 
                                                                  'gauss2_frac' : [0.3, 0, 1], 'p0' : [0.0004, -0.0003, 0.0009], 'p1' : [4.5, 4.4, 4.8], 'p2' : [0.15, 0.12, 0.18],}},
                                            {'files' : ['Charmonium_2017_D0Dstar_pt4_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_pt4_2Dfit.root',
                                                        'fit_plots/Charmonium_2017_D0Dstar_pt4_2Dfit.png', 'fit_plots/Dstar_component_2Dfit_pt4.png',
                                                        'fit_plots/Jpsi_component_2Dfit_pt4.png', 'fit_plots/Charmonium_2017_D0Dstar_pt4_correlation_pt4.png',
                                                        'data_root_files/Charmonium_2017_D0Dstar_pt4.root']}],} 

cases_pt4={'Charmonium_2017_D0Dstar_pt4' : [{'fit_parameters' : {'mean_jpsi' : [3.09355, 3.05, 3.15], 'sigma_gauss' : [0.04, 0.000001, 1], 'sigma_cb' : [0.02, 0.000001, 1],
                                                                  'frac_gauss_jpsi' : [0.4, 0.0001, 1.0],  'frac_cb' : [0.6, 0.0001, 1.0], 'alpha' : 1.4, 'n' : 8.8,
                                                                  'exp_coef' : [-3.2, -7, 1], 'frac_exp' : [0.4, 0.0, 1.0], 'dstar_mean' : [0.145495, 0.142, 0.158],
                                                                  'dstar_sigma_1' : [0.00508973, 0.0001, 0.01], 'dstar_sigma_2' : [0.000456236, 0.0001, 0.01], 'gauss1_frac' : [0.3, 0, 1], 
                                                                  'gauss2_frac' : [0.3, 0, 1], 'p0' : [0.0004, -0.0003, 0.0009], 'p1' : [4.5, 4.4, 4.8], 'p2' : [0.15, 0.12, 0.18],}},
                                            {'files' : ['Charmonium_2017_D0Dstar_pt4_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_pt4_2Dfit.root',
                                                        'fit_plots/Charmonium_2017_D0Dstar_pt4_2Dfit.png', 'fit_plots/Dstar_component_2Dfit_pt4.png',
                                                        'fit_plots/Jpsi_component_2Dfit_pt4.png', 'fit_plots/Charmonium_2017_D0Dstar_pt4_correlation_pt4.png',
                                                        'data_root_files/Charmonium_2017_D0Dstar_pt4.root']}],} 


cases_pt4={'Charmonium_2017_D0Dstar_pt4' : [{'fit_parameters' : {'mean_jpsi' : [3.09355, 3.05, 3.15], 'sigma_gauss' : [0.04, 0.000001, 1], 'sigma_cb' : [0.02, 0.000001, 1],
                                                                  'frac_gauss_jpsi' : [0.4, 0.0001, 1.0],  'frac_cb' : [0.6, 0.0001, 1.0], 'alpha' : 1.4, 'n' : 8.8,
                                                                  'exp_coef' : [-3.2, -7, 1], 'frac_exp' : [0.4, 0.0, 1.0], 'dstar_mean' : [0.145495, 0.142, 0.158],
                                                                  'dstar_sigma_1' : [0.00508973, 0.0001, 0.01], 'dstar_sigma_2' : [0.000456236, 0.0001, 0.01], 'gauss1_frac' : [0.3, 0, 1], 
                                                                  'gauss2_frac' : [0.3, 0, 1], 'p0' : [0.0004, -0.0003, 0.0009], 'p1' : [4.5, 4.4, 4.8], 'p2' : [0.15, 0.12, 0.18],}},
                                            {'files' : ['Charmonium_2017_D0Dstar_pt4_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_pt4_2Dfit.root',
                                                        'fit_plots/Charmonium_2017_D0Dstar_pt4_2Dfit.png', 'fit_plots/Dstar_component_2Dfit_pt4.png',
                                                        'fit_plots/Jpsi_component_2Dfit_pt4.png', 'fit_plots/Charmonium_2017_D0Dstar_pt4_correlation_pt4.png',
                                                        'data_root_files/Charmonium_2017_D0Dstar_pt4.root']}],} 

cases_pt4={'Charmonium_2017_D0Dstar_pt4' : [{'fit_parameters' : {'mean_jpsi' : [3.09355, 3.05, 3.15], 'sigma_gauss' : [0.04, 0.000001, 1], 'sigma_cb' : [0.02, 0.000001, 1],
                                                                  'frac_gauss_jpsi' : [0.4, 0.0001, 1.0],  'frac_cb' : [0.6, 0.0001, 1.0], 'alpha' : 1.4, 'n' : 8.8,
                                                                  'exp_coef' : [-3.2, -7, 1], 'frac_exp' : [0.4, 0.0, 1.0], 'dstar_mean' : [0.145495, 0.142, 0.158],
                                                                  'dstar_sigma_1' : [0.00508973, 0.0001, 0.01], 'dstar_sigma_2' : [0.000456236, 0.0001, 0.01], 'gauss1_frac' : [0.3, 0, 1], 
                                                                  'gauss2_frac' : [0.3, 0, 1], 'p0' : [0.0004, -0.0003, 0.0009], 'p1' : [4.5, 4.4, 4.8], 'p2' : [0.15, 0.12, 0.18],}},
                                            {'files' : ['Charmonium_2017_D0Dstar_pt4_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_pt4_2Dfit.root',
                                                        'fit_plots/Charmonium_2017_D0Dstar_pt4_2Dfit.png', 'fit_plots/Dstar_component_2Dfit_pt4.png',
                                                        'fit_plots/Jpsi_component_2Dfit_pt4.png', 'fit_plots/Charmonium_2017_D0Dstar_pt4_correlation_pt4.png',
                                                        'data_root_files/Charmonium_2017_D0Dstar_pt4.root']}],} 



########################################################################################### cos phi ###########################################################################################

cases_cosphi0p990={'Charmonium_2017_D0Dstar_cosphi0p990' : [{'fit_parameters' : {'mean_jpsi' : [3.09355, 3.05, 3.15], 'sigma_gauss' : [0.04, 0.000001, 1], 'sigma_cb' : [0.02, 0.000001, 1],
                                                                  'frac_gauss_jpsi' : [0.4, 0.0001, 1.0],  'frac_cb' : [0.6, 0.0001, 1.0], 'alpha' : 1.4, 'n' : 8.8,
                                                                  'exp_coef' : [-3.2, -7, 1], 'frac_exp' : [0.4, 0.0, 1.0], 'dstar_mean' : [0.145495, 0.142, 0.158],
                                                                  'dstar_sigma_1' : [0.00508973, 0.0001, 0.01], 'dstar_sigma_2' : [0.000456236, 0.0001, 0.01], 'gauss1_frac' : [0.3, 0, 1], 
                                                                  'gauss2_frac' : [0.3, 0, 1], 'p0' : [0.0004, -0.0003, 0.0009], 'p1' : [4.5, 4.4, 4.8], 'p2' : [0.15, 0.12, 0.18],}},
                                            {'files' : ['Charmonium_2017_D0Dstar_cosphi0p990_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_cosphi0p990_2Dfit.root',
                                                        'fit_plots/Charmonium_2017_D0Dstar_cosphi0p990_2Dfit.png', 'fit_plots/Dstar_component_2Dfit_cosphi0p990.png',
                                                        'fit_plots/Jpsi_component_2Dfit_cosphi0p990.png', 'fit_plots/Charmonium_2017_D0Dstar_cosphi0p990_correlation_cosphi0p990.png',
                                                        'data_root_files/Charmonium_2017_D0Dstar_cosphi0p990.root']}],} 

cases_cosphi0p985={'Charmonium_2017_D0Dstar_cosphi0p985' : [{'fit_parameters' : {'mean_jpsi' : [3.09355, 3.05, 3.15], 'sigma_gauss' : [0.04, 0.000001, 1], 'sigma_cb' : [0.02, 0.000001, 1],
                                                                  'frac_gauss_jpsi' : [0.4, 0.0001, 1.0],  'frac_cb' : [0.6, 0.0001, 1.0], 'alpha' : 2.8, 'n' : 8.8,
                                                                  'exp_coef' : [-3.2, -7, 1], 'frac_exp' : [0.4, 0.0, 1.0], 'dstar_mean' : [0.145495, 0.142, 0.158],
                                                                  'dstar_sigma_1' : [0.00508973, 0.0001, 0.01], 'dstar_sigma_2' : [0.000456236, 0.0001, 0.01], 'gauss1_frac' : [0.3, 0, 1], 
                                                                  'gauss2_frac' : [0.3, 0, 1], 'p0' : [0.0004, -0.0003, 0.0009], 'p1' : [4.5, 4.4, 4.8], 'p2' : [0.15, 0.12, 0.18],}},
                                            {'files' : ['Charmonium_2017_D0Dstar_cosphi0p985_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_cosphi0p985_2Dfit.root',
                                                        'fit_plots/Charmonium_2017_D0Dstar_cosphi0p985_2Dfit.png', 'fit_plots/Dstar_component_2Dfit_cosphi0p985.png',
                                                        'fit_plots/Jpsi_component_2Dfit_cosphi0p985.png', 'fit_plots/Charmonium_2017_D0Dstar_cosphi0p985_correlation_cosphi0p985.png',
                                                        'data_root_files/Charmonium_2017_D0Dstar_cosphi0p985.root']}],} 

cases_cosphi0p980={'Charmonium_2017_D0Dstar_cosphi0p980' : [{'fit_parameters' : {'mean_jpsi' : [3.09355, 3.05, 3.15], 'sigma_gauss' : [0.04, 0.000001, 1], 'sigma_cb' : [0.02, 0.000001, 1],
                                                                  'frac_gauss_jpsi' : [0.4, 0.0001, 1.0],  'frac_cb' : [0.6, 0.0001, 1.0], 'alpha' : 1.4, 'n' : 8.8,
                                                                  'exp_coef' : [-3.2, -7, 1], 'frac_exp' : [0.4, 0.0, 1.0], 'dstar_mean' : [0.145495, 0.142, 0.158],
                                                                  'dstar_sigma_1' : [0.00508973, 0.0001, 0.01], 'dstar_sigma_2' : [0.000456236, 0.0001, 0.01], 'gauss1_frac' : [0.3, 0, 1], 
                                                                  'gauss2_frac' : [0.3, 0, 1], 'p0' : [0.0004, -0.0003, 0.0009], 'p1' : [4.5, 4.4, 4.8], 'p2' : [0.15, 0.12, 0.18],}},
                                            {'files' : ['Charmonium_2017_D0Dstar_cosphi0p980_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_cosphi0p980_2Dfit.root',
                                                        'fit_plots/Charmonium_2017_D0Dstar_cosphi0p980_2Dfit.png', 'fit_plots/Dstar_component_2Dfit_cosphi0p980.png',
                                                        'fit_plots/Jpsi_component_2Dfit_cosphi0p980.png', 'fit_plots/Charmonium_2017_D0Dstar_cosphi0p980_correlation_cosphi0p980.png',
                                                        'data_root_files/Charmonium_2017_D0Dstar_cosphi0p980.root']}],} 

cases_cosphi0p975={'Charmonium_2017_D0Dstar_cosphi0p975' : [{'fit_parameters' : {'mean_jpsi' : [3.09355, 3.05, 3.15], 'sigma_gauss' : [0.04, 0.000001, 1], 'sigma_cb' : [0.02, 0.000001, 1],
                                                                  'frac_gauss_jpsi' : [0.4, 0.0001, 1.0],  'frac_cb' : [0.6, 0.0001, 1.0], 'alpha' : 4.1, 'n' : 8.8,
                                                                  'exp_coef' : [-3.2, -7, 1], 'frac_exp' : [0.4, 0.0, 1.0], 'dstar_mean' : [0.145495, 0.142, 0.158],
                                                                  'dstar_sigma_1' : [0.00508973, 0.0001, 0.01], 'dstar_sigma_2' : [0.000456236, 0.0001, 0.01], 'gauss1_frac' : [0.3, 0, 1], 
                                                                  'gauss2_frac' : [0.3, 0, 1], 'p0' : [0.0004, -0.0003, 0.0009], 'p1' : [4.5, 4.4, 4.8], 'p2' : [0.15, 0.12, 0.18],}},
                                            {'files' : ['Charmonium_2017_D0Dstar_cosphi0p975_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_cosphi0p975_2Dfit.root',
                                                        'fit_plots/Charmonium_2017_D0Dstar_cosphi0p975_2Dfit.png', 'fit_plots/Dstar_component_2Dfit_cosphi0p975.png',
                                                        'fit_plots/Jpsi_component_2Dfit_cosphi0p975.png', 'fit_plots/Charmonium_2017_D0Dstar_cosphi0p975_correlation_cosphi0p975.png',
                                                        'data_root_files/Charmonium_2017_D0Dstar_cosphi0p975.root']}],} 

cases_cosphi0p950={'Charmonium_2017_D0Dstar_cosphi0p950' : [{'fit_parameters' : {'mean_jpsi' : [3.09355, 3.05, 3.15], 'sigma_gauss' : [0.04, 0.000001, 1], 'sigma_cb' : [0.02, 0.000001, 1],
                                                                  'frac_gauss_jpsi' : [0.4, 0.0001, 1.0],  'frac_cb' : [0.6, 0.0001, 1.0], 'alpha' : 4.1, 'n' : 8.8,
                                                                  'exp_coef' : [-3.2, -7, 1], 'frac_exp' : [0.4, 0.0, 1.0], 'dstar_mean' : [0.145495, 0.142, 0.158],
                                                                  'dstar_sigma_1' : [0.00508973, 0.0001, 0.01], 'dstar_sigma_2' : [0.000456236, 0.0001, 0.01], 'gauss1_frac' : [0.3, 0, 1], 
                                                                  'gauss2_frac' : [0.3, 0, 1], 'p0' : [0.0004, -0.0003, 0.0009], 'p1' : [4.5, 4.4, 4.8], 'p2' : [0.15, 0.12, 0.18],}},
                                            {'files' : ['Charmonium_2017_D0Dstar_cosphi0p950_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_cosphi0p950_2Dfit.root',
                                                        'fit_plots/Charmonium_2017_D0Dstar_cosphi0p950_2Dfit.png', 'fit_plots/Dstar_component_2Dfit_cosphi0p950.png',
                                                        'fit_plots/Jpsi_component_2Dfit_cosphi0p950.png', 'fit_plots/Charmonium_2017_D0Dstar_cosphi0p950_correlation_cosphi0p950.png',
                                                        'data_root_files/Charmonium_2017_D0Dstar_cosphi0p950.root']}],} 

cases_cosphi0p900={'Charmonium_2017_D0Dstar_cosphi0p900' : [{'fit_parameters' : {'mean_jpsi' : [3.09355, 3.05, 3.15], 'sigma_gauss' : [0.04, 0.000001, 1], 'sigma_cb' : [0.02, 0.000001, 1],
                                                                  'frac_gauss_jpsi' : [0.4, 0.0001, 1.0],  'frac_cb' : [0.6, 0.0001, 1.0], 'alpha' : 4.1, 'n' : 8.8,
                                                                  'exp_coef' : [-3.2, -7, 1], 'frac_exp' : [0.4, 0.0, 1.0], 'dstar_mean' : [0.145495, 0.142, 0.158],
                                                                  'dstar_sigma_1' : [0.00508973, 0.0001, 0.01], 'dstar_sigma_2' : [0.000456236, 0.0001, 0.01], 'gauss1_frac' : [0.3, 0, 1], 
                                                                  'gauss2_frac' : [0.3, 0, 1], 'p0' : [0.001, -11, 21], 'p1' : [4.5, 4.4, 4.8], 'p2' : [0.15, 0.12, 0.18],}},
                                            {'files' : ['Charmonium_2017_D0Dstar_cosphi0p900_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_cosphi0p900_2Dfit.root', #[0.0004, -0.0003, 0.0009]
                                                        'fit_plots/Charmonium_2017_D0Dstar_cosphi0p900_2Dfit.png', 'fit_plots/Dstar_component_2Dfit_cosphi0p900.png',
                                                        'fit_plots/Jpsi_component_2Dfit_cosphi0p900.png', 'fit_plots/Charmonium_2017_D0Dstar_cosphi0p900_correlation_cosphi0p900.png',
                                                        'data_root_files/Charmonium_2017_D0Dstar_cosphi0p900.root']}],}  
cases_cosphi0p500={'Charmonium_2017_D0Dstar_cosphi0p500' : [{'fit_parameters' : {'mean_jpsi' : [3.09355, 3.05, 3.15], 'sigma_gauss' : [0.04, 0.000001, 1], 'sigma_cb' : [0.02, 0.000001, 1],
                                                                  'frac_gauss_jpsi' : [0.4, 0.0001, 1.0],  'frac_cb' : [0.6, 0.0001, 1.0], 'alpha' : 4.1, 'n' : 8.8,
                                                                  'exp_coef' : [-3.2, -7, 1], 'frac_exp' : [0.4, 0.0, 1.0], 'dstar_mean' : [0.145495, 0.142, 0.158],
                                                                  'dstar_sigma_1' : [0.00508973, 0.0001, 0.01], 'dstar_sigma_2' : [0.000456236, 0.0001, 0.01], 'gauss1_frac' : [0.3, 0, 1], 
                                                                  'gauss2_frac' : [0.3, 0, 1], 'p0' : [0.0004, -0.0003, 0.0009], 'p1' : [4.5, 4.4, 4.8], 'p2' : [0.15, 0.12, 0.18],}},
                                            {'files' : ['Charmonium_2017_D0Dstar_cosphi0p500_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_cosphi0p500_2Dfit.root', 
                                                        'fit_plots/Charmonium_2017_D0Dstar_cosphi0p500_2Dfit.png', 'fit_plots/Dstar_component_2Dfit_cosphi0p500.png',
                                                        'fit_plots/Jpsi_component_2Dfit_cosphi0p500.png', 'fit_plots/Charmonium_2017_D0Dstar_cosphi0p500_correlation_cosphi0p500.png',
                                                        'data_root_files/Charmonium_2017_D0Dstar_cosphi0p500.root']}],}  

cases_cosphi0p750={'Charmonium_2017_D0Dstar_cosphi0p750' : [{'fit_parameters' : {'mean_jpsi' : [3.09355, 3.05, 3.15], 'sigma_gauss' : [0.04, 0.000001, 1], 'sigma_cb' : [0.02, 0.000001, 1],
                                                                  'frac_gauss_jpsi' : [0.4, 0.0001, 1.0],  'frac_cb' : [0.6, 0.0001, 1.0], 'alpha' : 4.1, 'n' : 8.8,
                                                                  'exp_coef' : [-3.2, -7, 1], 'frac_exp' : [0.4, 0.0, 1.0], 'dstar_mean' : [0.145495, 0.142, 0.158],
                                                                  'dstar_sigma_1' : [0.00508973, 0.0001, 0.01], 'dstar_sigma_2' : [0.000456236, 0.0001, 0.01], 'gauss1_frac' : [0.3, 0, 1], 
                                                                  'gauss2_frac' : [0.3, 0, 1], 'p0' : [0.0004, -0.0003, 0.0009], 'p1' : [4.5, 4.4, 4.8], 'p2' : [0.15, 0.12, 0.18],}},
                                            {'files' : ['Charmonium_2017_D0Dstar_cosphi0p750_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_cosphi0p750_2Dfit.root', 
                                                        'fit_plots/Charmonium_2017_D0Dstar_cosphi0p750_2Dfit.png', 'fit_plots/Dstar_component_2Dfit_cosphi0p750.png',
                                                        'fit_plots/Jpsi_component_2Dfit_cosphi0p750.png', 'fit_plots/Charmonium_2017_D0Dstar_cosphi0p750_correlation_cosphi0p750.png',
                                                        'data_root_files/Charmonium_2017_D0Dstar_cosphi0p750.root']}],} 
cases_cosphi0p850={'Charmonium_2017_D0Dstar_cosphi0p850' : [{'fit_parameters' : {'mean_jpsi' : [3.09355, 3.05, 3.15], 'sigma_gauss' : [0.04, 0.000001, 1], 'sigma_cb' : [0.02, 0.000001, 1],
                                                                  'frac_gauss_jpsi' : [0.4, 0.0001, 1.0],  'frac_cb' : [0.6, 0.0001, 1.0], 'alpha' : 4.1, 'n' : 8.8,
                                                                  'exp_coef' : [-3.2, -7, 1], 'frac_exp' : [0.4, 0.0, 1.0], 'dstar_mean' : [0.145495, 0.142, 0.158],
                                                                  'dstar_sigma_1' : [0.00508973, 0.0001, 0.01], 'dstar_sigma_2' : [0.000456236, 0.0001, 0.01], 'gauss1_frac' : [0.3, 0, 1], 
                                                                  'gauss2_frac' : [0.3, 0, 1], 'p0' : [0.00099, -0.0003, 0.00099], 'p1' : [4.5, 4.4, 4.8], 'p2' : [0.15, 0.12, 0.18],}},
                                            {'files' : ['Charmonium_2017_D0Dstar_cosphi0p850_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_cosphi0p850_2Dfit.root', 
                                                        'fit_plots/Charmonium_2017_D0Dstar_cosphi0p850_2Dfit.png', 'fit_plots/Dstar_component_2Dfit_cosphi0p850.png',
                                                        'fit_plots/Jpsi_component_2Dfit_cosphi0p850.png', 'fit_plots/Charmonium_2017_D0Dstar_cosphi0p850_correlation_cosphi0p850.png',
                                                        'data_root_files/Charmonium_2017_D0Dstar_cosphi0p850.root']}],}      

'''
yield_files = ['fit_root_files/Charmonium_2017_D0Dstar_cosphi0p990_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_cosphi0p985_wspace', 
               'fit_root_files/Charmonium_2017_D0Dstar_cosphi0p980_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_cosphi0p975_wspace',
               'fit_root_files/Charmonium_2017_D0Dstar_cosphi0p950_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_cosphi0p900_wspace',
               'fit_root_files/Charmonium_2017_D0Dstar_cosphi0p850_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_cosphi0p800_wspace',
               'fit_root_files/Charmonium_2017_D0Dstar_cosphi0p750_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_cosphi0p500_wspace',]
csv_name = 'fom/Charmonium_2017_D0Dstar_cosphi.csv'

case = [0.990, 0.985, 0.980, 0.975, 0.950, 0.900, 0.850, 0.800, 0.750, 0.500]

type = 'copshi'
'''

##########################################################################################################################################################################################################################################
############################################################################################# Good configs ###############################################################################################################################
##########################################################################################################################################################################################################################################

########################################################################################### Decay length significance ###########################################################################################

cases_dlSig3p0={'Charmonium_2017_D0Dstar_dlSig3p0' : [{'fit_parameters' : {'mean_jpsi' : [3.09355, 3.05, 3.15], 'sigma_gauss' : [0.04, 0.000001, 1], 'sigma_cb' : [0.02, 0.000001, 1],
                                                                  'frac_gauss_jpsi' : [0.4, 0.0001, 1.0],  'frac_cb' : [0.6, 0.0001, 1.0], 'alpha' : 1.4, 'n' : 8.8,
                                                                  'exp_coef' : [-3.2, -7, 1], 'frac_exp' : [0.4, 0.0, 1.0], 'dstar_mean' : [0.145495, 0.142, 0.158],
                                                                  'dstar_sigma_1' : [0.00508973, 0.0001, 0.01], 'dstar_sigma_2' : [0.000456236, 0.0001, 0.01], 'gauss1_frac' : [0.3, 0, 1], 
                                                                  'gauss2_frac' : [0.3, 0, 1], 'p0' : [0.0004, -0.0003, 0.0009], 'p1' : [4.5, 4.4, 4.8], 'p2' : [0.15, 0.12, 0.18],}},
                                            {'files' : ['Charmonium_2017_D0Dstar_dlSig3p0_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_dlSig3p0_2Dfit.root',
                                                        'fit_plots/Charmonium_2017_D0Dstar_dlSig3p0_2Dfit.png', 'fit_plots/Dstar_component_2Dfit_dlSig3p0.png',
                                                        'fit_plots/Jpsi_component_2Dfit_dlSig3p0.png', 'fit_plots/Charmonium_2017_D0Dstar_dlSig3p0_correlation_dlSig3p0.png',
                                                        'data_root_files/Charmonium_2017_D0Dstar_dlSig3p0.root']}],} 

cases_dlSig2p9={'Charmonium_2017_D0Dstar_dlSig2p9' : [{'fit_parameters' : {'mean_jpsi' : [3.09355, 3.05, 3.15], 'sigma_gauss' : [0.04, 0.000001, 1], 'sigma_cb' : [0.02, 0.000001, 1],
                                                                  'frac_gauss_jpsi' : [0.4, 0.0001, 1.0],  'frac_cb' : [0.6, 0.0001, 1.0], 'alpha' : 2, 'n' : 8.8,  #alpha: 1.4, n: 8.8
                                                                  'exp_coef' : [-3.2, -7, 1], 'frac_exp' : [0.4, 0.0, 1.0], 'dstar_mean' : [0.145495, 0.142, 0.158],
                                                                  'dstar_sigma_1' : [0.00508973, 0.0001, 0.01], 'dstar_sigma_2' : [0.000456236, 0.0001, 0.01], 'gauss1_frac' : [0.3, 0, 1], 
                                                                  'gauss2_frac' : [0.3, 0, 1], 'p0' : [0.0004, -0.0003, 0.0009], 'p1' : [4.5, 4.4, 4.8], 'p2' : [0.15, 0.12, 0.18],}},
                                            {'files' : ['Charmonium_2017_D0Dstar_dlSig2p9_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_dlSig2p9_2Dfit.root',
                                                        'fit_plots/Charmonium_2017_D0Dstar_dlSig2p9_2Dfit.png', 'fit_plots/Dstar_component_2Dfit_dlSig2p9.png',
                                                        'fit_plots/Jpsi_component_2Dfit_dlSig2p9.png', 'fit_plots/Charmonium_2017_D0Dstar_dlSig2p9_correlation_dlSig2p9.png',
                                                        'data_root_files/Charmonium_2017_D0Dstar_dlSig2p9.root']}],} 

cases_dlSig2p8={'Charmonium_2017_D0Dstar_dlSig2p8' : [{'fit_parameters' : {'mean_jpsi' : [3.09355, 3.05, 3.15], 'sigma_gauss' : [0.04, 0.000001, 1], 'sigma_cb' : [0.02, 0.000001, 1],
                                                                  'frac_gauss_jpsi' : [0.4, 0.0001, 1.0],  'frac_cb' : [0.6, 0.0001, 1.0], 'alpha' : 3.5, 'n' : 8.8,  #alpha: 1.4, n: 8.8
                                                                  'exp_coef' : [-3.2, -7, 1], 'frac_exp' : [0.4, 0.0, 1.0], 'dstar_mean' : [0.145495, 0.142, 0.158],
                                                                  'dstar_sigma_1' : [0.00508973, 0.0001, 0.01], 'dstar_sigma_2' : [0.000456236, 0.0001, 0.01], 'gauss1_frac' : [0.3, 0, 1], 
                                                                  'gauss2_frac' : [0.3, 0, 1], 'p0' : [0.0004, -0.0003, 0.0009], 'p1' : [4.5, 4.4, 4.8], 'p2' : [0.15, 0.12, 0.18],}},
                                            {'files' : ['Charmonium_2017_D0Dstar_dlSig2p8_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_dlSig2p8_2Dfit.root',
                                                        'fit_plots/Charmonium_2017_D0Dstar_dlSig2p8_2Dfit.png', 'fit_plots/Dstar_component_2Dfit_dlSig2p8.png',
                                                        'fit_plots/Jpsi_component_2Dfit_dlSig2p8.png', 'fit_plots/Charmonium_2017_D0Dstar_dlSig2p8_correlation_dlSig2p8.png',
                                                        'data_root_files/Charmonium_2017_D0Dstar_dlSig2p8.root']}],}         

cases_dlSig2p7={'Charmonium_2017_D0Dstar_dlSig2p7' : [{'fit_parameters' : {'mean_jpsi' : [3.09355, 3.05, 3.15], 'sigma_gauss' : [0.04, 0.000001, 1], 'sigma_cb' : [0.02, 0.000001, 1],
                                                                  'frac_gauss_jpsi' : [0.4, 0.0001, 1.0],  'frac_cb' : [0.6, 0.0001, 1.0], 'alpha' : 4.1, 'n' : 8.8,  #alpha: 1.4, n: 8.8
                                                                  'exp_coef' : [-3.2, -7, 1], 'frac_exp' : [0.4, 0.0, 1.0], 'dstar_mean' : [0.145495, 0.142, 0.158],
                                                                  'dstar_sigma_1' : [0.00508973, 0.0001, 0.01], 'dstar_sigma_2' : [0.000456236, 0.0001, 0.01], 'gauss1_frac' : [0.3, 0, 1], 
                                                                  'gauss2_frac' : [0.3, 0, 1], 'p0' : [0.0004, -0.0003, 0.0009], 'p1' : [4.5, 4.4, 4.8], 'p2' : [0.15, 0.12, 0.18],}},
                                            {'files' : ['Charmonium_2017_D0Dstar_dlSig2p7_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_dlSig2p7_2Dfit.root',
                                                        'fit_plots/Charmonium_2017_D0Dstar_dlSig2p7_2Dfit.png', 'fit_plots/Dstar_component_2Dfit_dlSig2p7.png',
                                                        'fit_plots/Jpsi_component_2Dfit_dlSig2p7.png', 'fit_plots/Charmonium_2017_D0Dstar_dlSig2p7_correlation_dlSig2p7.png',
                                                        'data_root_files/Charmonium_2017_D0Dstar_dlSig2p7.root']}],}     

cases_dlSig2p6={'Charmonium_2017_D0Dstar_dlSig2p6' : [{'fit_parameters' : {'mean_jpsi' : [3.09355, 3.05, 3.15], 'sigma_gauss' : [0.04, 0.000001, 1], 'sigma_cb' : [0.02, 0.000001, 1],
                                                                  'frac_gauss_jpsi' : [0.4, 0.0001, 1.0],  'frac_cb' : [0.6, 0.0001, 1.0], 'alpha' : 4.1, 'n' : 8.8,  #alpha: 1.4, n: 8.8
                                                                  'exp_coef' : [-3.2, -7, 1], 'frac_exp' : [0.4, 0.0, 1.0], 'dstar_mean' : [0.145495, 0.142, 0.158],
                                                                  'dstar_sigma_1' : [0.00508973, 0.0001, 0.01], 'dstar_sigma_2' : [0.000456236, 0.0001, 0.01], 'gauss1_frac' : [0.3, 0, 1], 
                                                                  'gauss2_frac' : [0.3, 0, 1], 'p0' : [0.0004, -0.0003, 0.0009], 'p1' : [4.5, 4.4, 4.8], 'p2' : [0.15, 0.12, 0.18],}},
                                            {'files' : ['Charmonium_2017_D0Dstar_dlSig2p6_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_dlSig2p6_2Dfit.root',
                                                        'fit_plots/Charmonium_2017_D0Dstar_dlSig2p6_2Dfit.png', 'fit_plots/Dstar_component_2Dfit_dlSig2p6.png',
                                                        'fit_plots/Jpsi_component_2Dfit_dlSig2p6.png', 'fit_plots/Charmonium_2017_D0Dstar_dlSig2p6_correlation_dlSig2p6.png',
                                                        'data_root_files/Charmonium_2017_D0Dstar_dlSig2p6.root']}],}                                

cases_dlSig2p5={'Charmonium_2017_D0Dstar_dlSig2p5' : [{'fit_parameters' : {'mean_jpsi' : [3.09355, 3.05, 3.15], 'sigma_gauss' : [0.04, 0.000001, 1], 'sigma_cb' : [0.02, 0.000001, 1],
                                                                  'frac_gauss_jpsi' : [0.4, 0.0001, 1.0],  'frac_cb' : [0.6, 0.0001, 1.0], 'alpha' : 4.1, 'n' : 8.8,  #alpha: 1.4, n: 8.8
                                                                  'exp_coef' : [-3.2, -7, 1], 'frac_exp' : [0.4, 0.0, 1.0], 'dstar_mean' : [0.145495, 0.142, 0.158],
                                                                  'dstar_sigma_1' : [0.00508973, 0.0001, 0.01], 'dstar_sigma_2' : [0.000456236, 0.0001, 0.01], 'gauss1_frac' : [0.3, 0, 1], 
                                                                  'gauss2_frac' : [0.3, 0, 1], 'p0' : [0.0004, -0.0003, 0.0009], 'p1' : [4.5, 4.4, 4.8], 'p2' : [0.15, 0.12, 0.18],}},
                                            {'files' : ['Charmonium_2017_D0Dstar_dlSig2p5_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_dlSig2p5_2Dfit.root',
                                                        'fit_plots/Charmonium_2017_D0Dstar_dlSig2p5_2Dfit.png', 'fit_plots/Dstar_component_2Dfit_dlSig2p5.png',
                                                        'fit_plots/Jpsi_component_2Dfit_dlSig2p5.png', 'fit_plots/Charmonium_2017_D0Dstar_dlSig2p5_correlation_dlSig2p5.png',
                                                        'data_root_files/Charmonium_2017_D0Dstar_dlSig2p5.root']}],}           

cases_dlSig2p0={'Charmonium_2017_D0Dstar_dlSig2p0' : [{'fit_parameters' : {'mean_jpsi' : [3.09355, 3.05, 3.15], 'sigma_gauss' : [0.04, 0.000001, 1], 'sigma_cb' : [0.02, 0.000001, 1],
                                                                  'frac_gauss_jpsi' : [0.4, 0.0001, 1.0],  'frac_cb' : [0.6, 0.0001, 1.0], 'alpha' : 1.4, 'n' : 8.8,
                                                                  'exp_coef' : [-3.2, -7, 1], 'frac_exp' : [0.4, 0.0, 1.0], 'dstar_mean' : [0.145495, 0.142, 0.158],
                                                                  'dstar_sigma_1' : [0.00508973, 0.0001, 0.01], 'dstar_sigma_2' : [0.000456236, 0.0001, 0.01], 'gauss1_frac' : [0.3, 0, 1], 
                                                                  'gauss2_frac' : [0.3, 0, 1], 'p0' : [0.0004, -0.0003, 0.0009], 'p1' : [4.5, 4.4, 4.8], 'p2' : [0.15, 0.12, 0.18],}},
                                            {'files' : ['Charmonium_2017_D0Dstar_dlSig2p0_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_dlSig2p0_2Dfit.root',
                                                        'fit_plots/Charmonium_2017_D0Dstar_dlSig2p0_2Dfit.png', 'fit_plots/Dstar_component_2Dfit_dlSig2p0.png',
                                                        'fit_plots/Jpsi_component_2Dfit_dlSig2p0.png', 'fit_plots/Charmonium_2017_D0Dstar_dlSig2p0_correlation_dlSig2p0.png',
                                                        'data_root_files/Charmonium_2017_D0Dstar_dlSig2p0.root']}],} 

cases_dlSig1p5={'Charmonium_2017_D0Dstar_dlSig1p5' : [{'fit_parameters' : {'mean_jpsi' : [3.09355, 3.05, 3.15], 'sigma_gauss' : [0.04, 0.000001, 1], 'sigma_cb' : [0.02, 0.000001, 1],
                                                                  'frac_gauss_jpsi' : [0.4, 0.0001, 1.0],  'frac_cb' : [0.6, 0.0001, 1.0], 'alpha' : 1.4, 'n' : 8.8,
                                                                  'exp_coef' : [-3.2, -7, 1], 'frac_exp' : [0.4, 0.0, 1.0], 'dstar_mean' : [0.145495, 0.142, 0.158],
                                                                  'dstar_sigma_1' : [0.00508973, 0.0001, 0.01], 'dstar_sigma_2' : [0.000456236, 0.0001, 0.01], 'gauss1_frac' : [0.3, 0, 1], 
                                                                  'gauss2_frac' : [0.3, 0, 1], 'p0' : [0.0004, -0.0003, 0.0009], 'p1' : [4.5, 4.4, 4.8], 'p2' : [0.15, 0.12, 0.18],}},
                                            {'files' : ['Charmonium_2017_D0Dstar_dlSig1p5_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_dlSig1p5_2Dfit.root',
                                                        'fit_plots/Charmonium_2017_D0Dstar_dlSig1p5_2Dfit.png', 'fit_plots/Dstar_component_2Dfit_dlSig1p5.png',
                                                        'fit_plots/Jpsi_component_2Dfit_dlSig1p5.png', 'fit_plots/Charmonium_2017_D0Dstar_dlSig1p5_correlation_dlSig1p5.png',
                                                        'data_root_files/Charmonium_2017_D0Dstar_dlSig1p5.root']}],} 
cases_dlSig1p0={'Charmonium_2017_D0Dstar_dlSig1p0' : [{'fit_parameters' : {'mean_jpsi' : [3.09355, 3.05, 3.15], 'sigma_gauss' : [0.04, 0.000001, 1], 'sigma_cb' : [0.02, 0.000001, 1],
                                                                  'frac_gauss_jpsi' : [0.4, 0.0001, 1.0],  'frac_cb' : [0.6, 0.0001, 1.0], 'alpha' : 1.4, 'n' : 8.8,
                                                                  'exp_coef' : [-3.2, -7, 1], 'frac_exp' : [0.4, 0.0, 1.0], 'dstar_mean' : [0.145495, 0.142, 0.158],
                                                                  'dstar_sigma_1' : [0.00508973, 0.0001, 0.01], 'dstar_sigma_2' : [0.000456236, 0.0001, 0.01], 'gauss1_frac' : [0.3, 0, 1], 
                                                                  'gauss2_frac' : [0.3, 0, 1], 'p0' : [0.0004, -0.0003, 0.0009], 'p1' : [4.5, 4.4, 4.8], 'p2' : [0.15, 0.12, 0.18],}},
                                            {'files' : ['Charmonium_2017_D0Dstar_dlSig1p0_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_dlSig1p0_2Dfit.root',
                                                        'fit_plots/Charmonium_2017_D0Dstar_dlSig1p0_2Dfit.png', 'fit_plots/Dstar_component_2Dfit_dlSig1p0.png',
                                                        'fit_plots/Jpsi_component_2Dfit_dlSig1p0.png', 'fit_plots/Charmonium_2017_D0Dstar_dlSig1p0_correlation_dlSig1p0.png',
                                                        'data_root_files/Charmonium_2017_D0Dstar_dlSig1p0.root']}],} 
case_dlSig0p5={'Charmonium_2017_D0Dstar_dlSig0p5' : [{'fit_parameters' : {'mean_jpsi' : [3.09355, 3.05, 3.15], 'sigma_gauss' : [0.04, 0.000001, 1], 'sigma_cb' : [0.02, 0.000001, 1],
                                                                  'frac_gauss_jpsi' : [0.4, 0.0001, 1.0],  'frac_cb' : [0.6, 0.0001, 1.0], 'alpha' : 1.4, 'n' : 8.8,
                                                                  'exp_coef' : [-3.2, -7, 1], 'frac_exp' : [0.4, 0.0, 1.0], 'dstar_mean' : [0.145495, 0.142, 0.158],
                                                                  'dstar_sigma_1' : [0.00508973, 0.0001, 0.01], 'dstar_sigma_2' : [0.000456236, 0.0001, 0.01], 'gauss1_frac' : [0.3, 0, 1], 
                                                                  'gauss2_frac' : [0.3, 0, 1], 'p0' : [0.002, 0.001, 0.004], 'p1' : [4.5, 4.4, 4.8], 'p2' : [0.15, 0.12, 0.18],}},
                                            {'files' : ['Charmonium_2017_D0Dstar_dlSig0p5_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_dlSig0p5_2Dfit.root',
                                                        'fit_plots/Charmonium_2017_D0Dstar_dlSig0p5_2Dfit.pn    g', 'fit_plots/Dstar_component_2Dfit_dlSig0p5.png',
                                                        'fit_plots/Jpsi_component_2Dfit_dlSig0p5.png', 'fit_plots/Charmonium_2017_D0Dstar_dlSig0p5_correlation_dlSig0p5.png',
                                                        'data_root_files/Charmonium_2017_D0Dstar_dlSig0p5.root']}],} # Signal and background components are not ok :(
                                                    
'''
yield_files = ['fit_root_files/Charmonium_2017_D0Dstar_dlSig3p0_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_dlSig2p9_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_dlSig2p8_wspace',
               'fit_root_files/Charmonium_2017_D0Dstar_dlSig2p7_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_dlSig2p6_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_dlSig2p5_wspace',
               'fit_root_files/Charmonium_2017_D0Dstar_dlSig2p0_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_dlSig1p5_wspace', 'fit_root_files/Charmonium_2017_D0Dstar_dlSig1p0_wspace']

csv_name = 'fom/Charmonium_2017_D0Dstar_dlSig.csv'

case = [3.0, 2.9, 2.8, 2.7, 2.6, 2.5, 2.0, 1.5, 1.0]

type = 'dl Significance'
'''