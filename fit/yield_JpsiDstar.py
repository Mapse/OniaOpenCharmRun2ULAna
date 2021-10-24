import ROOT
import math

def pega(file="Jpsi_Dstar_fit.root"):
    
    file_root = ROOT.TFile(file)
    wspace = file_root.Get("JpsiDstart_workspace")

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







pega(file="Jpsi_Dstar_fit.root")