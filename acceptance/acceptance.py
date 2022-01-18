from coffea.util import load
import uproot3
from ROOT import TFile, TH2D, TChain, TCanvas, TLatex, EnableImplicitMT
import argparse

# Enable multicore
EnableImplicitMT()

## Argparse section
parser = argparse.ArgumentParser(description='Acceptance studies')
parser.add_argument("-f", "--root_file", help="Create root file with data", action="store_true")
parser.add_argument("-p", "--plots", help="Produces acceptance plots", action="store_true")

args = parser.parse_args()

# File with coffea data
file = '../output/Monte_Carlo_2017_matching/Monte_Carlo_2017_matching.coffea'
# File to be created
root_file = "jpsi_acceptance.root"
# Figure name - quarkonia
fig_name = "Jpsi_Acceptance.png"

def create_ttree(file, root_file):
    # Load coffea file
    acc = load(file)
    # Take gen Jpsi pt and eta
    gen_jpsi_pt = acc['Gen_Jpsi']['pt'].value
    gen_jpsi_eta = acc['Gen_Jpsi']['eta'].value
    # Take rec Jpsi pt and eta
    rec_jpsi_pt = acc['Dimu']['pt'].value[acc['Dimu']['is_jpsi'].value]
    rec_jpsi_eta = acc['Dimu']['eta'].value[acc['Dimu']['is_jpsi'].value]
    
    # Use uproot t
    with uproot3.recreate(root_file) as f:
        f['gen_jpsi'] = uproot3.newtree({"gen_jpsi_pt": "float64",  "gen_jpsi_eta" : "float64"})
        f['gen_jpsi'].extend({"gen_jpsi_pt": gen_jpsi_pt, "gen_jpsi_eta" : gen_jpsi_eta})

        f['rec_jpsi'] = uproot3.newtree({"rec_jpsi_pt": "float64",  "rec_jpsi_eta" : "float64"})
        f['rec_jpsi'].extend({"rec_jpsi_pt": rec_jpsi_pt, "rec_jpsi_eta" : rec_jpsi_eta})

def acceptance(root_file):
       
    ## Rec Jpsi
    
    # Creates chain to open the file
    chain_rec = TChain("rec_jpsi")
    chain_rec.Add(root_file)
    
    # Takes pt and eta
    rec_jpsi_pt = chain_rec.AsMatrix(["rec_jpsi_pt"])
    rec_jpsi_eta = chain_rec.AsMatrix(["rec_jpsi_eta"])
    
    # Creates 2D histogram 
    rec_hist = TH2D('rec', '; ;; ', 50, 0, 40, 50, -2.5, 2.5,)
    rec_hist.SetStats(False)
    
    # Draw
    chain_rec.Draw("rec_jpsi_eta:rec_jpsi_pt>>rec")
    
    ## Gen Jpsi
    
    # Creates chain to open the file
    
    chain_gen = TChain("gen_jpsi")
    chain_gen.Add(root_file)
    
    # Takes pt and eta
    gen_jpsi_pt = chain_gen.AsMatrix(["gen_jpsi_pt"])
    gen_jpsi_eta = chain_gen.AsMatrix(["gen_jpsi_eta"])

    # Creates 2D histogram
    gen_hist = TH2D('gen', '; ;; ', 50, 0, 40, 50, -2.5, 2.5)
    gen_hist.SetStats(False)
    
    chain_gen.Draw("gen_jpsi_eta:gen_jpsi_pt>>gen")

    can = TCanvas("can", "histograms", 850, 650)

    can.Draw()
    
    gen_hist.Draw("colz")
    
    can = TCanvas("can", "histograms", 850, 650)
    rec_hist_clone = rec_hist
    rec_hist_clone.Divide(gen_hist)
    can.Draw()
    rec_hist_clone.SetStats(False)
    rec_hist_clone.Draw("colz")
    
    ## Axis
    
    # x axis - pT
    pt_ax = TLatex()
    pt_ax.SetNDC()
    pt_ax.SetTextFont(43)
    pt_ax.SetTextSize(20)
    pt_ax.DrawLatex(.8, 0.03, "J/#Psi p_{T} (GeV/c)")
    
    # y axis - eta
    eta_ax = TLatex()
    eta_ax.SetNDC()
    eta_ax.SetTextFont(43)
    eta_ax.SetTextSize(20)
    eta_ax.SetTextAngle(90)
    eta_ax.DrawLatex(0.05, 0.65, "J/#Psi pseudorapidity")
    
    can.SaveAs(fig_name)

if __name__ == '__main__':

    if (args.root_file and args.plots): 

        # Calls the function to create root file with the data and produce the plots
        create_ttree(file, root_file)
        acceptance(root_file)

    if (args.plots):
        # Calls the function to produce the plots
        acceptance(root_file)