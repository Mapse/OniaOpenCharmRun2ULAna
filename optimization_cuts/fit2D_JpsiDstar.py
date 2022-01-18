import ROOT
import math
import argparse
from tqdm import tqdm

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

def fit2DJpsiDstar():

    # Root file with data
    if (args.testfit): 
        file = ROOT.TFile.Open(config.dict_fls["save_path_single_file"])
        rootdata = file.asso

    if (args.severaldata):
        chain = ROOT.TChain("JpsiDstar")
        for i in tqdm(config.dict_fls["eras"], desc="Loading", unit="eras", total=len(config.dict_fls["eras"])):
         
            dtset = config.dict_fls["dataset"] + i
            save_path = config.dict_fls["save_path"]
            chain.Add(save_path + dtset + "_JpsiDstar.root")
        rootdata = chain

    ### Fitting part

    # Jpsi mass parameter
    jpsi_mass = ROOT.RooRealVar("jpsi_mass", "Mass Jpsi", 2.95, 3.25)
    # Dstar mass parameter
    dstar_mass = ROOT.RooRealVar("dstar_mass", "Dstar Delta m ", 0.14, 0.16)

    # Take the data from the file
    data = ROOT.RooDataSet("data", 
                       "Data 2D Jpsi + Dstar", 
                       ROOT.RooArgSet(jpsi_mass, dstar_mass), 
                       ROOT.RooFit.Import(rootdata))
    # Individual data for jpsi and dstar
    #datajpsi = ROOT.RooDataSet("data", "Data 2D Jpsi + Dstar", file.asso, ROOT.RooArgSet(jpsi_mass))
    #datadstar = ROOT.RooDataSet("data", "Data 2D Jpsi + Dstar", file.asso, ROOT.RooArgSet(dstar_mass))

    ## Jpsi Signal: Crystal Ball and Gaussian with same mean

    # Mean
    mean_jpsi = ROOT.RooRealVar("mean_jpsi", "", 3.09355, 3.05, 3.15)
    # Sigmas
    sigma_gauss = ROOT.RooRealVar("sigma_gauss", "", 0.04, 0.000001, 1)
    sigma_cb = ROOT.RooRealVar("sigma_cb", "", 0.02, 0.000001, 1)
    # PDFs fractions
    frac_gauss_jpsi = ROOT.RooRealVar("frac_gauss_jpsi","", 0.4, 0.0, 1.0)
    frac_cb = ROOT.RooRealVar("frac_cb","", 0.6, 0.0, 1.0)
    # Alpha and n for Crystal Ball
    alpha = ROOT.RooRealVar("alpha", "", 1.2)
    n = ROOT.RooRealVar("n", "", 8.8)
    # Signal definition
    gauss = ROOT.RooGaussian("gauss", "", jpsi_mass, mean_jpsi, sigma_gauss)
    crystal_ball = ROOT.RooCBShape("crystal_ball", "", jpsi_mass, mean_jpsi, sigma_cb, alpha, n)

    """ jpsi_signal = ROOT.RooAddPdf("jpsi_signal", "", ROOT.RooArgList(gauss, crystal_ball),
                        ROOT.RooArgList(frac_gauss_jpsi)) """

    ## Jpsi Background: Exponential

    # Exponential coefficient
    exp_coef = ROOT.RooRealVar("exp_coef", "", -3.2, -5, 5)
    # Background definition
    back_exp = ROOT.RooExponential("back_exp", "", jpsi_mass, exp_coef)
    # Background fraction
    frac_exp = ROOT.RooRealVar("frac_exp", "", 0.4, 0.0, 1.0)

    # Jpsi model definition 
    jpsi_model = ROOT.RooAddPdf("jpsi_model", "", ROOT.RooArgList(gauss, crystal_ball, back_exp),
                   ROOT.RooArgList(frac_gauss_jpsi, frac_cb))

    ## Dstar Signal: Double Gaussian with same mean

    # Mean
    dstar_mean = ROOT.RooRealVar("dstar_mean", "Dstar Gaussian Mean", 0.1455, 0.142, 0.158)
    # Sigmas
    dstar_sigma1 = ROOT.RooRealVar("dstar_sigma_1", "Dstar Gaussian 1 Sigma", 0.005, 0.0001, 0.01)
    dstar_sigma2 = ROOT.RooRealVar("dstar_sigma_2", "Dstar Gaussian 2 Sigma", 0.001, 0.0001, 0.01)
    # PDFs fractions
    gauss1_frac = ROOT.RooRealVar("gauss1_frac", "Dstar Gaussian Fraction", 0.3, 0, 1)
    gauss2_frac = ROOT.RooRealVar("gauss2_frac", "Dstar Signal Fraction", 0.3, 0, 1)
    # Signal definition
    g1 = ROOT.RooGaussian("gauss1", "Dstar Gaussian 1", dstar_mass, dstar_mean, dstar_sigma1)
    g2 = ROOT.RooGaussian("gauss2", "Dstar Gaussian 2", dstar_mass, dstar_mean, dstar_sigma2)

    """ dstar_signal = ROOT.RooAddPdf("dstar_signal", "", ROOT.RooArgList(g1, g2),
                        ROOT.RooArgList(gauss1_frac)) """

    ## Dstar Background: Phenomenological Threshold Function 

    # Coefficients
    p0 = ROOT.RooRealVar("p0","", 0.005, -1, 1)
    p1 = ROOT.RooRealVar('p1',"", 5, 0, 10)
    p2 = ROOT.RooRealVar('p2',"", 0.12, 1, 20)

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
    #c1 = ROOT.TCanvas("c1")
    
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

    """ frame_jpsi.Draw()
    leg_jpsi.Draw("same")
    c1.Draw()
    c1.SaveAs(config.dict_fls["save_fit_jpsi"]) """
      
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

    c2.SaveAs(config.dict_fls["save_fit_dstar"])

    """ # Mass correlation
    c3 = ROOT.TCanvas("Mass correlation")
    ph2 = dstar_mass.createHistogram("dstar vs jpsi pdf", jpsi_mass)
    model2D.fillHistogram(ph2,ROOT.RooArgList(dstar_mass,jpsi_mass))
    ph2.Draw("SURF")
    c3.Draw()
    c3.SaveAs(config.dict_fls["save_correlation_JpsiDstar"])

    # 2D fitting
    c4 = ROOT.TCanvas("2D fitting")
    dh2 = dstar_mass.createHistogram("dstar vs jpsi data", jpsi_mass)
    data.fillHistogram(dh2,ROOT.RooArgList(dstar_mass,jpsi_mass))
    dh2.Rebin2D(3,3)
    dh2.Draw("LEGO")
    c4.Draw()
    c4.SaveAs(config.dict_fls["save_fit_2d"]) """

    #### Not being used ###
    """ # Chi square
    print("-----------------------Xi square-----------------------")

    # Jpsi
    print("Jpsi:")
    n_param = result.floatParsFinal().getSize()
    reduce_chi_square_jpsi = frame_jpsi.chiSquare(n_param)
    print("Xi square for J/psi is (I don't know): {}".format(reduce_chi_square_jpsi))
    print("Xi square for J/psi is: {}".format(frame_jpsi.chiSquare(6)))
    print(n_param)

    # Dstar
    print("Dstar:")
    reduce_chi_square_dstar = frame_dstar.chiSquare(n_param)
    print("Xi square for Dstar is (I don't know): {}".format(reduce_chi_square_dstar))
    print("Xi square for Dstar is: {}".format(frame_dstar.chiSquare(8))) """
    ###########################################################
    # To save workspace
    wspace = ROOT.RooWorkspace(config.dict_fls["wspace_name"])
    
    getattr(wspace, "import")(data)
    getattr(wspace, "import")(model2D)
    getattr(wspace, "import")(result)

    wspace.writeToFile(config.dict_fls["wspace_root"])

def yields_jpsidstar(file=config.dict_fls["wspace_root"]):
    
    file_root = ROOT.TFile(file)
    wspace = file_root.Get(config.dict_fls["wspace_name"])

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

    # Fracs jpsi
    frac_gauss_jpsi = params.find("frac_gauss_jpsi")
    frac_cb = params.find("frac_cb")

    # Fracs dstar
    gauss1_frac = params.find("gauss1_frac")
    gauss2_frac = params.find("gauss2_frac")

    ## Contassssssss
    fjpsi = (frac_gauss_jpsi.getVal() + frac_cb.getVal() * (1 - frac_gauss_jpsi.getVal()))
    fbgjpsi = 1 - fjpsi
    fdstar = (gauss1_frac.getVal() + gauss2_frac.getVal() * (1 - gauss1_frac.getVal()))
    fbgstar = 1 - fdstar

    fcp1 = fbgjpsi * fbgstar
    fcp2 = fbgjpsi * fdstar
    fcp3 = fjpsi * fbgstar
    fcp4 = fjpsi * fdstar
    fcptotal = fcp1 + fcp2 + fcp3 + fcp4

    msg = f"""Summary:
Nevt total = {Nevts}
Nevt jpsi = {Nevts*(fcp3+fcp4)}
Nevt dstar = {Nevts*(fcp2+fcp4)}
Nevt signal = {Nevts*(fcp4)}
Nevt bg = {Nevts*(fcp1 + fcp2 + fcp3)}
"""

    print(msg)

if (args.fit):
    fit2DJpsiDstar()

if (args.yields):
    yields_jpsidstar()