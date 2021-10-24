import ROOT
import math

ROOT.EnableImplicitMT()

ERAS = ['A', 'C', 'D', 'E', 'F']
chain = ROOT.TChain("JpsiDstar")
save_path = "../output/test_cut_background_2d/"


for i in ERAS:
     save_path = "/afs/cern.ch/work/m/mabarros/public/CMSSW_10_6_12/src/OniaOpenCharmRun2ULAna/fit/Data_to_fit/" 
     dataset = "Charmonium2017" + i
     print(save_path + dataset + "_JpsiDstar.root")
     chain.Add(save_path + dataset + "_JpsiDstar.root")



########## Some root files to test

#rootfile = "DstarJpsi_asso_charmonium_2018B.root"si_DstardmCut_asso_charmonium_2018B.root"

colors_hex = ['#e41a1c','#377eb8','#4daf4a','#984ea3','#ff7f00','#ffff33']
colors = []

TColor = ROOT.TColor()

for color in colors_hex:
     colors.append(TColor.GetColor(color))

#file = ROOT.TFile.Open(save_path + rootfile)

jpsi_mass = ROOT.RooRealVar("jpsi_mass", "Mass Jpsi", 2.95, 3.25)
dstar_mass = ROOT.RooRealVar("dstar_mass", "Dstar Delta m ", 0.14, 0.16)

data = ROOT.RooDataSet("data", 
                       "Data 2D Jpsi + Dstar", 
                       ROOT.RooArgSet(jpsi_mass, dstar_mass), 
                       ROOT.RooFit.Import(chain)) # OBS use file.asso in case of unique file

#datajpsi = ROOT.RooDataSet("data", "Data 2D Jpsi + Dstar", chain.jpsi_mass, ROOT.RooArgSet(jpsi_mass))
#datadstar = ROOT.RooDataSet("data", "Data 2D Jpsi + Dstar", chain.dstar_mass, ROOT.RooArgSet(dstar_mass))

## Jpsi Signal: Crystal Ball and Gaussian

# Jpsi pdg mass
Mjpsi = 3.09 

# mass
mjpsi =ROOT.RooRealVar("mass_jpsi", "PDG mass Jpsi", Mjpsi)

mean_jpsi = ROOT.RooRealVar("mean_jpsi", "", 3.09355, 3.05, 3.15)

sigma_gauss = ROOT.RooRealVar("sigma_gauss", "", 0.04, 0.000001, 1)
sigma_cb = ROOT.RooRealVar("sigma_cb", "", 0.02, 0.000001, 1)

frac_gauss = ROOT.RooRealVar("frac_gauss","", 0.4, 0.0, 1.0)
frac_cb = ROOT.RooRealVar("frac_cb","", 0.6, 0.0, 1.0)

alpha = ROOT.RooRealVar("alpha", "", 1.2)
n = ROOT.RooRealVar("n", "", 8.8)

signal1 = ROOT.RooGaussian("gauss", "", jpsi_mass, mean_jpsi, sigma_gauss)
signal2 = ROOT.RooCBShape("crystal ball", "", jpsi_mass, mean_jpsi, sigma_cb, alpha, n)

# Background PDF
exp_coef = ROOT.RooRealVar("exp_coef", "", -3.2, -5, 5)

back_exp = ROOT.RooExponential("back_exp", "", jpsi_mass, exp_coef)

# Model definition and fitting
jpsi_model = ROOT.RooAddPdf("model", "", ROOT.RooArgList(signal1, signal2, back_exp),
                       ROOT.RooArgList(frac_gauss, frac_cb), ROOT.kTRUE)

# Dstar Signal Double Gaussian - same mean

dstar_mean = ROOT.RooRealVar("dstar_mean", "Dstar Gaussian Mean", 0.1455, 0.142, 0.158)
dstar_sigma1 = ROOT.RooRealVar("dstar_sigma_1", "Dstar Gaussian 1 Sigma", 0.001, 0.000001, 1.0)
dstar_sigma2 = ROOT.RooRealVar("dstar_sigma_2", "Dstar Gaussian 2 Sigma", 0.001, 0.000001, 1.0)
gauss1_frac = ROOT.RooRealVar("gauss1_frac", "Dstar Gaussian Fraction", 0.3, 0, 1)
gauss2_frac = ROOT.RooRealVar("gauss2_frac", "Dstar Signal Fraction", 0.3, 0, 1)

g1 = ROOT.RooGaussian("g1", "Dstar Gaussian 1", dstar_mass, dstar_mean, dstar_sigma1)
g2 = ROOT.RooGaussian("g2", "Dstar Gaussian 2", dstar_mass, dstar_mean, dstar_sigma2)

# Dstar Background = Phenomenological Threshold Function 

p0 = ROOT.RooRealVar("p0","", 1.4, -2, 20)
p1 = ROOT.RooRealVar('p1',"", 19, -20, 20)
p2 = ROOT.RooRealVar('p2',"", 1.8, 1, 20)

dstar_bkg = ROOT.RooGenericPdf("dstar_bkg","Dstar Background PDF","(1 - exp(-(@0 -0.13957)/@1)) * (@0/0.13957)**@2 + @3 * (@0/0.13957 - 1)",
                          ROOT.RooArgList(dstar_mass,p0,p1,p2))

dstar_model = ROOT.RooAddPdf("dstar_model", "Dstar Model", ROOT.RooArgList(g1, g2, dstar_bkg),
                       ROOT.RooArgList(gauss1_frac, gauss2_frac), ROOT.kTRUE)

model2D = ROOT.RooProdPdf("model2D", "2D Model Upsilon + Dstar", ROOT.RooArgList(jpsi_model, dstar_model))
result = model2D.fitTo(data, ROOT.RooFit.Save())

result.floatParsFinal().Print("S")

""" c1 = ROOT.TCanvas("c1")
frame_jpsi = jpsi_mass.frame(ROOT.RooFit.Title("Dimuon Invariant mass"))
data.plotOn(frame_jpsi, ROOT.RooFit.Name("Data"), ROOT.RooFit.DataError(ROOT.RooAbsData.SumW2))
jpsi_model.plotOn(frame_jpsi, ROOT.RooFit.Name("Jpsi Model"))
frame_jpsi.Draw()
c1.Draw() """

""" c2 = ROOT.TCanvas("c2")
frame_dstar = dstar_mass.frame(ROOT.RooFit.Title("Dstar delta m"))
data.plotOn(frame_dstar, ROOT.RooFit.Name("Data"), ROOT.RooFit.DataError(ROOT.RooAbsData.SumW2))
dstar_model.plotOn(frame_dstar, ROOT.RooFit.Name("Dstar Model"))
frame_dstar.Draw()
c2.Draw() """

c3 = ROOT.TCanvas("c3")
ph2 = dstar_mass.createHistogram("dstar vs jpsi pdf", jpsi_mass)
model2D.fillHistogram(ph2,ROOT.RooArgList(dstar_mass,jpsi_mass))
ph2.Draw("SURF")
c3.Draw()

""" c4 = ROOT.TCanvas("c4")
dh2 = dstar_mass.createHistogram("dstar vs jpsi data", jpsi_mass)
data.fillHistogram(dh2,ROOT.RooArgList(dstar_mass,jpsi_mass))
dh2.Rebin2D(3,3)
dh2.Draw("LEGO")
c4.Draw() """

#c1.SaveAs("Jpsi_associated.png")
#c2.SaveAs("Dstar_associated.png")
c3.SaveAs("SurfPlot_JpsiDstar.png")
#c4.SaveAs("Fit2D_JpsiDstar.png")


# To save workspace
wspace = ROOT.RooWorkspace("JpsiDstar_fit")

getattr(wspace, "import")(data)
getattr(wspace, "import")(model2D)
getattr(wspace, "import")(result)

wspace.writeToFile("JpsiDstar_wspace.root")

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
print("Xi square for Dstar is: {}".format(frame_dstar.chiSquare(8)))

print("-----------------------Yield section -----------------------")

print("Jpsi:")

# Number of signal events: Nsignal = Ntotal * [fcrystall + (1 - fcrystall) * fgauss]
nsignaljpsi = datajpsi.sumEntries() * (frac_cb.getVal() + (1 - frac_cb.getVal()) * frac_gauss.getVal())

# Number of background events: Nback = Ntotal (1 - fgauss) * (1 - fcrystall) * fexponential
# Or: Ntotal - Nsignal
nbackgroundjpsi = datajpsi.sumEntries() * (1 - frac_gauss.getVal()) * (1 - frac_cb.getVal())

print("The number of signal events for J/psi is: {}".format(nsignaljpsi))
print("The number of background events for J/psi is: {}".format(nbackgroundjpsi))
print("The number of s/sqrt(b) for Dstar is : {}".format(nsignaljpsi/math.sqrt(nbackgroundjpsi)))

print("Dstar")

# M = fgauss1 * Gaussian1 + (1 - fgauss1) [fgauss2 * Gaussian2 + (1 - fgauss2) * PTF]

# Number of signal events: Nsignal = Ntotal * [fgauss1 + (1 - fgauss1) * fgauss2]
nsignaldstar = datadstar.sumEntries() * (gauss1_frac.getVal() + (1 - gauss1_frac.getVal()) * gauss2_frac.getVal())

# Number of background events: Nback = Ntotal (1 - fgauss) * (1 - fcrystall) * fexponential
# or Ntotal - Nsignal
nbackgrounddstar = datadstar.sumEntries() * (1 - gauss1_frac.getVal()) * (1 - gauss2_frac.getVal())

print("The number of signal events for Dstar is: {}".format(nsignaldstar))
print("The number of background events for Dstar is: {}".format(nbackgrounddstar))
print("The number of s/sqrt(b) for Dstar is : {}".format(nsignaldstar/math.sqrt(nbackgrounddstar)))
 """