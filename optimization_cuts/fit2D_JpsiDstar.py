from cmath import sqrt
from webbrowser import BackgroundBrowser
import ROOT
import math
import argparse
from tqdm import tqdm

from uncertainties import ufloat
from uncertainties.umath import * 

import config_fit_2d as config

# Enable multicore
ROOT.EnableImplicitMT()

## Argparse section
parser = argparse.ArgumentParser(description='JpsiDstar 2D fit')
parser.add_argument("-f", "--fit", help="Fit the data", action="store_true")
parser.add_argument("-y", "--yields", help="Calculate the yields", action="store_true")
parser.add_argument("-t", "--testfit", help="Fit for one specific files", action="store_true")
parser.add_argument("-s", "--severaldata", help="Fit for files from the ERAS", action="store_true")

args = parser.parse_args()

"""
    This function do the 2D fit for the association between Jpsi and Dstar
it also calculates the chi^2/d.o.f for the fit projection for both particles
and compute the number of candidates for signal and background.

"""

def fit2DJpsiDstar(opt):

    # Root file with data
    '''if (args.testfit): 
        file = ROOT.TFile.Open(config.dict_fls["save_path_single_file"])
        rootdata = file.asso'''

    ### Fitting part

    # Jpsi mass parameter
    jpsi_mass = ROOT.RooRealVar("jpsi_mass", "Mass Jpsi", 2.95, 3.25)
    # Dstar mass parameter
    dstar_mass = ROOT.RooRealVar("dstar_mass", "Dstar Delta m ", 0.14, 0.16)

    # Root file with data

    # Opens each root file
    
    root_file = ROOT.TFile.Open(opt[1]['files'][6])

    # Opens the corresponding ntuple
    rootdata = root_file.asso

    # Takes the data from the file
    data = ROOT.RooDataSet("data", "Data 2D Jpsi + Dstar",
                        ROOT.RooArgSet(jpsi_mass, dstar_mass),
                        ROOT.RooFit.Import(rootdata))



    # Individual data for jpsi and dstar
    #datajpsi = ROOT.RooDataSet("data", "Data 2D Jpsi + Dstar", file.asso, ROOT.RooArgSet(jpsi_mass))
    #datadstar = ROOT.RooDataSet("data", "Data 2D Jpsi + Dstar", file.asso, ROOT.RooArgSet(dstar_mass))

    ## Jpsi Signal: Crystal Ball and Gaussian with same mean
    
    # Mean
    mean_jpsi = ROOT.RooRealVar("mean_jpsi", "", opt[0]['fit_parameters']['mean_jpsi'][0], opt[0]['fit_parameters']['mean_jpsi'][1], opt[0]['fit_parameters']['mean_jpsi'][2])
    # Sigmas
    sigma_gauss = ROOT.RooRealVar("sigma_gauss", "", opt[0]['fit_parameters']['sigma_gauss'][0], opt[0]['fit_parameters']['sigma_gauss'][1], opt[0]['fit_parameters']['sigma_gauss'][2])
    sigma_cb = ROOT.RooRealVar("sigma_cb", "", opt[0]['fit_parameters']['sigma_cb'][0], opt[0]['fit_parameters']['sigma_cb'][1], opt[0]['fit_parameters']['sigma_cb'][2])
    # PDFs fractions
    frac_gauss_jpsi = ROOT.RooRealVar("frac_gauss_jpsi","", opt[0]['fit_parameters']['frac_gauss_jpsi'][0], opt[0]['fit_parameters']['frac_gauss_jpsi'][1], opt[0]['fit_parameters']['frac_gauss_jpsi'][2])
    frac_cb = ROOT.RooRealVar("frac_cb","", opt[0]['fit_parameters']['frac_cb'][0], opt[0]['fit_parameters']['frac_cb'][1], opt[0]['fit_parameters']['frac_cb'][2])
    # Alpha and n for Crystal Ball
    alpha = ROOT.RooRealVar("alpha", "", opt[0]['fit_parameters']['alpha'])
    n = ROOT.RooRealVar("n", "", opt[0]['fit_parameters']['n'])
    # Signal definition
    gauss = ROOT.RooGaussian("gauss", "", jpsi_mass, mean_jpsi, sigma_gauss)
    crystal_ball = ROOT.RooCBShape("crystal_ball", "", jpsi_mass, mean_jpsi, sigma_cb, alpha, n)

    """ jpsi_signal = ROOT.RooAddPdf("jpsi_signal", "", ROOT.RooArgList(gauss, crystal_ball),
                        ROOT.RooArgList(frac_gauss_jpsi)) """

    ## Jpsi Background: Exponential

    # Exponential coefficient
    exp_coef = ROOT.RooRealVar("exp_coef", "", opt[0]['fit_parameters']['exp_coef'][0], opt[0]['fit_parameters']['exp_coef'][1], opt[0]['fit_parameters']['exp_coef'][2])
    # Background definition
    back_exp = ROOT.RooExponential("back_exp", "", jpsi_mass, exp_coef)
    # Background fraction
    frac_exp = ROOT.RooRealVar("frac_exp", "", opt[0]['fit_parameters']['frac_exp'][0], opt[0]['fit_parameters']['frac_exp'][1], opt[0]['fit_parameters']['frac_exp'][2])

    # Jpsi model definition 
    jpsi_model = ROOT.RooAddPdf("jpsi_model", "", ROOT.RooArgList(gauss, crystal_ball, back_exp),
                ROOT.RooArgList(frac_gauss_jpsi, frac_cb))

    ## Dstar Signal: Double Gaussian with same mean

    # Mean
    dstar_mean = ROOT.RooRealVar("dstar_mean", "Dstar Gaussian Mean", opt[0]['fit_parameters']['dstar_mean'][0], opt[0]['fit_parameters']['dstar_mean'][1], opt[0]['fit_parameters']['dstar_mean'][2])
    #dstar_mean.setConstant(True)
    # Sigmas
    dstar_sigma1 = ROOT.RooRealVar("dstar_sigma_1", "Dstar Gaussian 1 Sigma", opt[0]['fit_parameters']['dstar_sigma_1'][0], opt[0]['fit_parameters']['dstar_sigma_1'][1], opt[0]['fit_parameters']['dstar_sigma_1'][2])
    dstar_sigma2 = ROOT.RooRealVar("dstar_sigma_2", "Dstar Gaussian 2 Sigma", opt[0]['fit_parameters']['dstar_sigma_2'][0], opt[0]['fit_parameters']['dstar_sigma_2'][1], opt[0]['fit_parameters']['dstar_sigma_2'][2])
    #dstar_sigma1.setConstant(True)
    #dstar_sigma2.setConstant(True)
    # PDFs fractions
    gauss1_frac = ROOT.RooRealVar("gauss1_frac", "Dstar Gaussian Fraction", opt[0]['fit_parameters']['gauss1_frac'][0], opt[0]['fit_parameters']['gauss1_frac'][1], opt[0]['fit_parameters']['gauss1_frac'][2])
    gauss2_frac = ROOT.RooRealVar("gauss2_frac", "Dstar Signal Fraction", opt[0]['fit_parameters']['gauss2_frac'][0], opt[0]['fit_parameters']['gauss2_frac'][1], opt[0]['fit_parameters']['gauss2_frac'][2])
    # Signal definition
    g1 = ROOT.RooGaussian("gauss1", "Dstar Gaussian 1", dstar_mass, dstar_mean, dstar_sigma1)
    g2 = ROOT.RooGaussian("gauss2", "Dstar Gaussian 2", dstar_mass, dstar_mean, dstar_sigma2)

    """ dstar_signal = ROOT.RooAddPdf("dstar_signal", "", ROOT.RooArgList(g1, g2),
                        ROOT.RooArgList(gauss1_frac)) """

    ## Dstar Background: Phenomenological Threshold Function 

    # Coefficients
    p0 = ROOT.RooRealVar("p0","", opt[0]['fit_parameters']['p0'][0], opt[0]['fit_parameters']['p0'][1], opt[0]['fit_parameters']['p0'][2])
    #p0.setConstant(True)
    p1 = ROOT.RooRealVar('p1',"", opt[0]['fit_parameters']['p1'][0], opt[0]['fit_parameters']['p1'][1], opt[0]['fit_parameters']['p1'][2])
    #p1.setConstant(True)
    p2 = ROOT.RooRealVar('p2',"", opt[0]['fit_parameters']['p2'][0], opt[0]['fit_parameters']['p2'][1], opt[0]['fit_parameters']['p2'][2])
    #p2.setConstant(True)
    # Background definition
    dstar_bkg = ROOT.RooGenericPdf("dstar_bkg","Dstar Background PDF","(1 - exp(-(@0 -0.13957)/@1)) * (@0/0.13957)**@2 + @3 * (@0/0.13957 - 1)",
                        ROOT.RooArgList(dstar_mass,p0,p1,p2))
    # Background fraction
    #frac_thr = ROOT.RooRealVar("frac_thr", "", 0.4, 0.0, 1.0)
    # Dstar model definition
    dstar_model = ROOT.RooAddPdf("dstar_model", "Dstar Model", ROOT.RooArgList(g1, g2, dstar_bkg),
                    ROOT.RooArgList(gauss1_frac, gauss2_frac), ROOT.kTRUE)
    # 2D model definition
    model2D = ROOT.RooProdPdf("model2D", "2D Model Upsilon + Dstar", ROOT.RooArgList(jpsi_model, dstar_model))
    # Fitting
    result = model2D.fitTo(data, ROOT.RooFit.Save())
    # Print the results on screen
    result.floatParsFinal().Print("S")
    
    ## Canvas definitions 

    # Canvas for Jpsi 
    c1 = ROOT.TCanvas("c1")
    
    # Fame for Jpsi
    frame_jpsi = jpsi_mass.frame(ROOT.RooFit.Title("Dimuon Invariant mass"))
    frame_jpsi.GetXaxis().SetTitle("#\mu^+\mu^- #invariant \ mass[GeV]")
    
    # Plot the Jpsi data
    data.plotOn(frame_jpsi, ROOT.RooFit.Name("Data"), ROOT.RooFit.DataError(ROOT.RooAbsData.SumW2))

    # Plot the Jpsi signal
    jpsi_model.plotOn(frame_jpsi, ROOT.RooFit.Name("Signal"), ROOT.RooFit.Components("gauss,crystal_ball"),
                ROOT.RooFit.LineStyle(config.styles["signal"]), ROOT.RooFit.LineColor(config.colors["signal"]))
    
    # Plot for Jpsi background
    jpsi_model.plotOn(frame_jpsi, ROOT.RooFit.Name("Background"), ROOT.RooFit.Components("back_exp"),
                ROOT.RooFit.LineStyle(config.styles["background"]), ROOT.RooFit.LineColor(config.colors["background"]))

    # Plot for the Model
    jpsi_model.plotOn(frame_jpsi, ROOT.RooFit.Name("Model"), ROOT.RooFit.LineStyle(config.styles["model"]),
                ROOT.RooFit.LineColor(config.colors["model"]))

    leg_jpsi = ROOT.TLegend(0.7, 0.7, 0.88, 0.89)
    leg_jpsi.AddEntry(frame_jpsi.findObject("Data"), "Data", "LEP")
    leg_jpsi.AddEntry(frame_jpsi.findObject("Model"), "Model Fit", "L")
    leg_jpsi.AddEntry(frame_jpsi.findObject("Signal"), "Signal Fit", "L")
    leg_jpsi.AddEntry(frame_jpsi.findObject("Background"), "Background fit", "L")

    frame_jpsi.Draw()
    leg_jpsi.Draw("same")
    c1.Draw()
    c1.SaveAs(opt[1]['files'][4])
    
    # Canvas for Dstar 
    c2 = ROOT.TCanvas("Dstar Canvas")

    # Frame
    frame_dstar = dstar_mass.frame(ROOT.RooFit.Title("Dstar delta m"))
    frame_dstar.GetXaxis().SetTitle("M(k\pi\pi_s) - M(k\pi) [GeV]")
    
    # Dstar data
    data.plotOn(frame_dstar, ROOT.RooFit.Name("Data"), ROOT.RooFit.DataError(ROOT.RooAbsData.SumW2))
    
    # Dstar signal
    dstar_model.plotOn(frame_dstar, ROOT.RooFit.Name("Signal"), ROOT.RooFit.Components("gauss1,gauss2"),
                    ROOT.RooFit.LineStyle(config.styles["signal"]), ROOT.RooFit.LineColor(config.colors["signal"]))

    # Dstar background
    dstar_model.plotOn(frame_dstar, ROOT.RooFit.Name("Background"), ROOT.RooFit.Components("dstar_bkg"),
                    ROOT.RooFit.LineStyle(config.styles["background"]), ROOT.RooFit.LineColor(config.colors["background"]))
    
    # Dstar Model
    dstar_model.plotOn(frame_dstar, ROOT.RooFit.Name("Model"), ROOT.RooFit.LineStyle(config.styles["model"]),
                    ROOT.RooFit.LineColor(config.colors["model"]))

    # Legends
    leg_dstar = ROOT.TLegend(0.7, 0.7, 0.88, 0.89)
    leg_dstar.AddEntry(frame_dstar.findObject("Data"), "Data", "LEP")
    leg_dstar.AddEntry(frame_dstar.findObject("Model"), "Model Fit", "L")
    leg_dstar.AddEntry(frame_dstar.findObject("Signal"), "Signal Fit", "L")
    leg_dstar.AddEntry(frame_dstar.findObject("Background"), "Background fit", "L")

    frame_dstar.Draw()
    leg_dstar.Draw("same")
    c2.Draw()
    
    ## Legend

    ## Top text right
    
    right = ROOT.TLatex()
    right.SetNDC()
    right.SetTextFont(43)
    right.SetTextSize(30)
    right.SetTextAlign(13)
    right.DrawLatex(.10,.95,"#bf{CMS} #scale[0.7]{#it{Preliminary}}")
    right.SetTextSize(20)
    right.DrawLatex(.80,.94 , config.lumi)

    c2.SaveAs(opt[1]['files'][3])

    # Mass correlation
    c3 = ROOT.TCanvas("Mass correlation")
    ph2 = dstar_mass.createHistogram("dstar vs jpsi pdf", jpsi_mass)
    model2D.fillHistogram(ph2,ROOT.RooArgList(dstar_mass,jpsi_mass))
    ph2.Draw("SURF")
    c3.Draw()
    c3.SaveAs(opt[1]['files'][2])

    # 2D fitting
    c4 = ROOT.TCanvas("2D fitting")
    dh2 = dstar_mass.createHistogram("dstar vs jpsi data", jpsi_mass)
    data.fillHistogram(dh2,ROOT.RooArgList(dstar_mass,jpsi_mass))
    dh2.Rebin2D(3,3)
    dh2.Draw("LEGO")
    c4.Draw()
    c4.SaveAs(opt[1]['files'][5]) 

    #### Not being used ###
    # Chi square
    print("-----------------------Xi square-----------------------")

    """ # Jpsi
    print("Jpsi:")
    n_param = result.floatParsFinal().getSize()
    reduce_chi_square_jpsi_notSure = frame_jpsi.chiSquare(n_param)
    print(f"Xi square for J/psi is (I don't know): {reduce_chi_square_jpsi_notSure}") """

    """ # Dstar
    print("Dstar:")
    reduce_chi_square_dstar_notSure = frame_dstar.chiSquare(n_param)
    print(f"Xi square for Dstar is (I don't know): {reduce_chi_square_dstar_notSure}") """
    
   
    ###########################################################
    # To save workspace
    wspace = ROOT.RooWorkspace(opt[1]['files'][0])
    
    getattr(wspace, "import")(data)
    getattr(wspace, "import")(model2D)

    wspace.writeToFile(opt[1]['files'][1])

    # Jpsi chi square  
    chi_square_jpsi = frame_jpsi.chiSquare(config.nparm_jpsi)
    print(f"Xi square for J/psi is: {chi_square_jpsi}")
    # Dstar chi square
    chi_square_dstar = frame_dstar.chiSquare(config.nparm_dstar)
    print(f"Xi square for Dstar is: {chi_square_dstar}")
    
    with open(opt[1]['files'][1].replace('.root', '') + '.txt', 'w') as f:
        f.write(str(chi_square_jpsi))
        f.write('\n')
        f.write(str(chi_square_dstar))


def yields_jpsidstar(yield_list=config.yield_files):

    import csv
    import numpy as np
    
    with open(config.csv_name, 'w') as c:
        # Creates the csv writer
        writer = csv.writer(c)
        # write a row to the csv file
        header = ['Case', 'N_evts_total', 'Nevt_Jpsi', 'Nevt_Jpsi_error', 'Nevt_Dstar', 'Nevt_Dstar_error', 'N_signal', 
                  'N_signal_err', 'N_background', 'N_background_err', 'chi_square_jpsi', 'chi_square_dstar' , 'FOM', 'FOM_err']
        writer.writerow(header)

        for f in yield_list:

            with open(f.replace('_wspace', '') + '_2Dfit.txt', 'r') as tx:
                list_chi = tx.readlines()
                chi_square_jpsi = float(list_chi[0])
                chi_square_dstar = float(list_chi[1])
               
            file_root = ROOT.TFile(f.replace('_wspace', '') + '_2Dfit.root')
            print()
            wspace = file_root.Get(f.replace('fit_root_files/', ''))

            print(wspace.var(""))

            model2D = wspace.pdf("model2D")
            
            components = model2D.getComponents()
            
            jpsi_mass = wspace.var("jpsi_mass")
            
            dstar_mass = wspace.var("dstar_mass")

            # Jpsi
            gauss = components.find("gauss")
            crystal_ball = components.find("crystal_ball")
            exponential = components.find("back_exp")

            """ gauss_integral = gauss.createIntegral(ROOT.RooArgSet(jpsi_mass, dstar_mass), ROOT.RooFit.NormSet(ROOT.RooArgSet(jpsi_mass, dstar_mass)))
            crystal_ball_integral = crystal_ball.createIntegral(ROOT.RooArgSet(jpsi_mass, dstar_mass), ROOT.RooFit.NormSet(ROOT.RooArgSet(jpsi_mass, dstar_mass)))
            exponential_integral = exponential.createIntegral(ROOT.RooArgSet(jpsi_mass, dstar_mass), ROOT.RooFit.NormSet(ROOT.RooArgSet(jpsi_mass, dstar_mass))) """

            # Dstar
            gauss1 = components.find("gauss1")
            gauss2 = components.find("gauss2")
            dstar_bkg = components.find("dstar_bkg")

            
            """ gauss1_integral = gauss1.createIntegral(ROOT.RooArgSet(dstar_mass, jpsi_mass), ROOT.RooFit.NormSet(ROOT.RooArgSet(dstar_mass, jpsi_mass)))
            gauss2_integral = gauss2.createIntegral(ROOT.RooArgSet(dstar_mass, jpsi_mass), ROOT.RooFit.NormSet(ROOT.RooArgSet(dstar_mass, jpsi_mass)))
            dstar_bkg_integral = dstar_bkg.createIntegral(ROOT.RooArgSet(dstar_mass, jpsi_mass), ROOT.RooFit.NormSet(ROOT.RooArgSet(dstar_mass, jpsi_mass)))

            print("Jpsi")
            gauss_integral.Print()
            crystal_ball_integral.Print()
            exponential_integral.Print()

            print("Dstar")
            gauss1_integral.Print()
            gauss2_integral.Print()
            dstar_bkg_integral.Print() """

            """ print("2D")
            model2D_integral = model2D.createIntegral(ROOT.RooArgSet(dstar_mass, jpsi_mass),
                                                    ROOT.RooFit.NormSet(ROOT.RooArgSet(dstar_mass, jpsi_mass)))
            model2D_integral.Print()  """

            print("Params")
            params = model2D.getVariables()
            data = wspace.data("data")

            # N events
            Nevts = data.sumEntries()

            ## Fractions jpsi

            # Frac. gaussian
            frac_gauss_jpsi = params.find("frac_gauss_jpsi")
            frac_gauss_jpsi_val = frac_gauss_jpsi.getVal()
            frac_gauss_jpsi_error = frac_gauss_jpsi.getError()

            # Frac. CB
            frac_cb = params.find("frac_cb")
            frac_cb_val = frac_cb.getVal()
            frac_cb_error = frac_cb.getError()
            #print(frac_gauss_jpsi.getError())

            ## Fractions dstar

            # Frac. gauss 1
            gauss1_frac = params.find("gauss1_frac")
            gauss1_frac_val = gauss1_frac.getVal()
            gauss1_frac_error = gauss1_frac.getError()

            # Frac. gauss 2
            gauss2_frac = params.find("gauss2_frac")
            gauss2_frac_val = gauss2_frac.getVal()
            gauss2_frac_error = gauss2_frac.getError()

            ## Contassssssss
            fjpsi_val = (frac_gauss_jpsi_val + frac_cb_val * (1 - frac_gauss_jpsi_val))
            fjpsi_error = (frac_gauss_jpsi_error + frac_cb_error * (1 - frac_gauss_jpsi_error))

            fbgjpsi_val = 1 - fjpsi_val
            fbgjpsi_error = 1 - fjpsi_error

            fdstar_val = (gauss1_frac_val + gauss2_frac_val * (1 - gauss1_frac_val))
            fdstar_error = (gauss1_frac_error + gauss2_frac_error * (1 - gauss1_frac_error))

            fbgstar_val = 1 - fdstar_val
            fbgstar_error = 1 - fdstar_error

            fcp1_val = fbgjpsi_val * fbgstar_val
            fcp2_val = fbgjpsi_val * fdstar_val
            fcp3_val = fjpsi_val * fbgstar_val
            fcp4_val = fjpsi_val * fdstar_val
            fcptotal_val = fcp1_val + fcp2_val + fcp3_val + fcp4_val

            fcp1_error = fbgjpsi_error * fbgstar_error
            fcp2_error = fbgjpsi_error * fdstar_error
            fcp3_error = fjpsi_error * fbgstar_error
            fcp4_error = fjpsi_error * fdstar_error
            fcptotal_error = fcp1_error + fcp2_error + fcp3_error + fcp4_error

            signal_val = Nevts*(fcp4_val)
            signal_error = Nevts*(fcp4_error)

            background_val = Nevts*(fcp1_val + fcp2_val + fcp3_val)
            background_error = Nevts*(fcp1_error + fcp2_error + fcp3_error)

            """ OLD APPROACH
            fom_val = signal_val/(signal_val + background_val)**0.5
            fom_error = np.abs(fom_val) * ((signal_error/signal_val)**2 + (background_error/(2*background_val))**2)**0.5 """

            # Used uncertaities to compute fom and error
            x = ufloat(signal_val, signal_error)
            y = ufloat(background_val, background_error)
            fom = x/(x + y)**0.5
            fom_val = fom.nominal_value
            fom_error = fom.std_dev
            

            nevts_jpsi_val = (Nevts*(fcp3_val+fcp4_val))
            nevts_jpsi_error = (Nevts*(fcp3_error+fcp4_error))

            nevts_dstar_val = (Nevts*(fcp2_val+fcp4_val))
            nevts_dstar_error = (Nevts*(fcp2_error+fcp4_error))

            row = [f, Nevts, nevts_jpsi_val, nevts_jpsi_error, nevts_dstar_val, nevts_dstar_error, signal_val, signal_error, 
                   background_val, background_error, chi_square_jpsi, chi_square_dstar, fom_val, fom_error]
            writer.writerow(row)

            

            msg = f"""Summary:
        Nevt total = {Nevts:.2f} 
        Nevt jpsi = {nevts_jpsi_val:.2f} +- {nevts_jpsi_error:.2f}
        Nevt dstar = {nevts_dstar_val:.2f} +- {nevts_dstar_error:.2f}
        Nevt signal = {(Nevts*(fcp4_val)):.2f} +- {(Nevts*(fcp4_error)):.2f}
        Nevt bg = {(background_val):.2f} +- {(background_error):.2f} 
        """

            print(msg)

    return params

if (args.fit):
    import time
    tstart = time.time()
    for opt in config.cases.values():
        fit2DJpsiDstar(opt)
    print(f'Process finished in: {time.time()-tstart:.2f} s')

if (args.yields):
    p = yields_jpsidstar()
    #print(p.Print("v"))
