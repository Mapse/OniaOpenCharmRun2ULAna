import ROOT
import math
import argparse

## Argparse section
parser = argparse.ArgumentParser(description='Dstar fit')

parser.add_argument("-f", "--fit", help="Fit the data", action="store_true")
parser.add_argument("-y", "--yields", help="Calculate the yields and the value of signal/sqrt(background)", action="store_true")
parser.add_argument("-p", "--pull", help="Pull histogram", action="store_true")
parser.add_argument("-c", "--chi", help="Calculate the Chi square reduced", action="store_true")

args = parser.parse_args()

# Root file with data 
file = ROOT.TFile.Open("../output/Charmonium2018B_test/dstar_charmonium_2018B.root")

def fit_Dstar(file=file):
    
    # Mass observable
    mass = ROOT.RooRealVar("mass", "", 0.14, 0.16)

    # Dataset creation
    data = ROOT.RooDataSet("data", "", file.Dstar, ROOT.RooArgSet(mass))

    ## Signal definition

    # Gaussian 1
    frac_g1 = ROOT.RooRealVar("frac_gauss1", "", 0.18, 0.0, 1.0)
    mean = ROOT.RooRealVar("mean","", 0.1455, 0.14, 0.16)
    sigma_g1 = ROOT.RooRealVar("sigma g1", "", 0.0002, 0.00001, 1.0)

    # Gaussian 2
    frac_g2 = ROOT.RooRealVar("frac_gauss2", "", 0.25, 0.0, 1.0)
    sigma_g2 = ROOT.RooRealVar("sigma g2", "", 0.0004, 0.00001, 1.0)

    # Pdfs

    gauss1 = ROOT.RooGaussian("gauss 1", "", mass, mean, sigma_g1)
    gauss2 = ROOT.RooGaussian("gauss 2", "", mass, mean, sigma_g2)

    ## Background

    # Phenomenological threshold function

    p0 = ROOT.RooRealVar("pzeroz","", 2.7e-3, 0.001, 5)
    p1 = ROOT.RooRealVar('pone',"", -2.4e-1, -4, 4)
    p2 = ROOT.RooRealVar('ptwo',"", 5, 3, 6)

    # Background pdf definition
    back = ROOT.RooGenericPdf("Phen thrs func","","(1 - exp(-(@0 -0.13957)/@1)) * (@0/0.13957)**@2 + @3 * (@0/0.13957 - 1)", ROOT.RooArgList(mass,p0,p1,p2))

    # Model definition and fitting
    model = ROOT.RooAddPdf("model", "", ROOT.RooArgList(gauss1, gauss2, back),
                        ROOT.RooArgList(frac_g1, frac_g2), ROOT.kTRUE)
    
    # Fit and save the result
    result = model.fitTo(data, ROOT.RooFit.Save())

    ################ Plots - Normal scale ################

    # Colors and styles
    colors = {"model" : 2, "signal" : 4, "background" : 3}
    styles = {"model" : 1, "signal" : 1, "background" : 2}

    # Canvas Definition
    can = ROOT.TCanvas("can", "histograms", 850, 650)

    # Frame creation
    frame1 = mass.frame(ROOT.RooFit.Title("Dataset: Charmonium 2018B"), ROOT.RooFit.Bins(99))
    frame1.GetXaxis().SetTitle("M(k\pi\pi_s) - M(k\pi) [GeV]")
    frame1.GetXaxis().SetLimits(0.138, 0.16)

    # Data
    data.plotOn(frame1, ROOT.RooFit.Name("Data"), ROOT.RooFit.DataError(ROOT.RooAbsData.SumW2))

    # Signal
    model.plotOn(frame1, ROOT.RooFit.Name("Signal"), ROOT.RooFit.Components("*gauss*"), ROOT.RooFit.LineStyle(styles["signal"]), ROOT.RooFit.LineColor(colors["signal"]))

    # Background
    model.plotOn(frame1, ROOT.RooFit.Name("Background"), ROOT.RooFit.Components("Phen thrs func"), ROOT.RooFit.LineStyle(styles["background"]), ROOT.RooFit.LineColor(colors["background"]))

    # Model
    model.plotOn(frame1, ROOT.RooFit.Name("Model"), ROOT.RooFit.LineStyle(styles["model"]), ROOT.RooFit.LineColor(colors["model"]))

    ## ChiSquare computation
    n_param = result.floatParsFinal().getSize()
    rcs = frame1.chiSquare(n_param)
    reduce_chi_square = ROOT.RooRealVar("chi", "", rcs)

    ## Legends

    leg = ROOT.TLegend(0.7, 0.7, 0.88, 0.89)
    leg.AddEntry(frame1.findObject("Data"), "Data", "LEP")
    leg.AddEntry(frame1.findObject("Model"), "Model Fit", "L")
    leg.AddEntry(frame1.findObject("Signal"), "Signal Fit", "L")
    leg.AddEntry(frame1.findObject("Background"), "Background fit", "L")

    # Draw the frame
    frame1.Draw()
    leg.Draw("same")

    # Draw the canvas
        

    # Save the image
    can.SaveAs("Dstar_data_fit.png")

    # Log plot
    ROOT.gPad.SetLogy()

    can.Draw()

    can.SaveAs("Dstar_fit_yaxislog.png")

    # To save workspace
    wspace = ROOT.RooWorkspace("Dstar_fit")

    getattr(wspace, "import")(data)
    getattr(wspace, "import")(model)
    getattr(wspace, "import")(reduce_chi_square)

    wspace.writeToFile("Dstar_fit.root")

## Function to yields computation

def calc_yields(file="Dstar_fit.root"):

    # File with Dstar fit 
    file_fit = ROOT.TFile.Open(file)
    # Workspace
    w = file_fit.Get("Dstar_fit")

    # Calculations
    # Number of signal events: Nsignal = Ntotal * [fgauss1 + (1 - fgauss1) * fgauss2]
    Ntotal = w.data("data").sumEntries()
    frac_g1 = w.var("frac_gauss1").getVal()
    frac_g2 = w.var("frac_gauss2").getVal()

    nsignal = Ntotal * (frac_g1 + (1 - frac_g1) * frac_g2)

    # Number of background events: Nback = Ntotal (1 - fgauss) * (1 - fcrystall) * fexponential
    # or Ntotal - Nsignal
    nbackground = Ntotal * (1 - frac_g1) * (1 - frac_g2)

    # Quality test
    ratio = nsignal/math.sqrt(nbackground)

    print(f"The number of signal events is: {nsignal}")
    print(f"The number of background events is: {nbackground}")
    print(f"The number of s/sqrt(b) is : {ratio}")

def pull_dist(file="Dstar_fit.root"):

    file_fit = ROOT.TFile.Open(file)
    print("Generating pull histogram...")
    w = file_fit.Get("Dstar_fit")

    model = w.pdf("model")
    data = w.data("data")
    mass = w.var("mass") 

    colors = {"model" : 2, "signal" : 4, "background" : 3}
    styles = {"model" : 1, "signal" : 1, "background" : 2}

    can = ROOT.TCanvas("can", "histograms", 850, 650)
    can.Divide(2)

    frame1 = mass.frame(ROOT.RooFit.Title("Dataset: Charmonium 2018B"))
    
    data.plotOn(frame1, ROOT.RooFit.Name("Data"), ROOT.RooFit.DataError(ROOT.RooAbsData.SumW2))
    model.plotOn(frame1, ROOT.RooFit.Name("Model"), ROOT.RooFit.LineStyle(styles["model"]), ROOT.RooFit.LineColor(colors["model"]))

    can.cd(1)
    frame1.Draw()

    histpull = frame1.pullHist()

    frame2 = mass.frame(ROOT.RooFit.Title("Pull Distribution"))
    frame2.GetXaxis().SetTitle("M(k\pi\pi_s) - M(k\pi) [GeV]")
    frame2.addPlotable(histpull, "P") 

    can.cd(2)
    frame2.Draw()
    can.Draw()

    can.SaveAs("Dstar_fit_pull.png") 

def calc_chi_reduced(file="Dstar_fit.root"):
    
    file_fit = ROOT.TFile.Open(file)
    w = file_fit.Get("Dstar_fit")

    chi = w.var("chi").getVal()

    print(f"Reduced chi square: {chi}")
  
if (args.fit):
    fit_Dstar(file=file)

if (args.yields):
    calc_yields(file="Dstar_fit.root")

if (args.pull):
    pull_dist(file="Dstar_fit.root")

if (args.chi):
    calc_chi_reduced(file="Dstar_fit.root")






