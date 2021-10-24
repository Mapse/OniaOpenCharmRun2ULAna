import os

import awkward as ak
from coffea.util import load
from coffea import hist
import argparse

import matplotlib.pyplot as plt

import create_plots as crep


from coffea.nanoevents.methods import candidate
ak.behavior.update(candidate.behavior)

## Argparse section
parser = argparse.ArgumentParser(description='JpsiDstar plots')

parser.add_argument("-a", "--all", help="All plots", action="store_true")
parser.add_argument("-m", "--muons", help="Muon plots", action="store_true")
parser.add_argument("-j", "--jpsi", help="Jpsi plots", action="store_true")
parser.add_argument("-d", "--dstar", help="Dstar plots", action="store_true")

file = '../output/test_Monte_Carlo_2017_trigger/test_Monte_Carlo_2017_trigger_hists.coffea'

args = parser.parse_args()

def genPlots(file_path, process_name):

    hists = load(file)

    ## ----------- Vertex sections ----------- ##

    

     # Primary vertex distributions
    ax = crep.create_plot1d(hists['Primary_vertex_npvs'])
    plt.savefig('mc_plots/' + process_name + 'Reconstructed_primary_vertex.png')
    plt.clf()

    ## Gen Particles section

    ## ----------- Gen Particles section ----------- ##

    # Gen Muon pT
    ax = crep.create_plot1d(hists['GenMuon_p'].sum('eta', 'phi'))
    plt.savefig('mc_plots/' + process_name + '/Gen_Muon_pt.png')
    plt.clf()

    # Gen Muon eta
    ax = crep.create_plot1d(hists['GenMuon_p'].sum('pt', 'phi'))
    plt.savefig('mc_plots/' + process_name + '/Gen_Muon_eta.png')
    plt.clf()

    # Gen Muon phi
    ax = crep.create_plot1d(hists['GenMuon_p'].sum('eta', 'pt'))
    plt.savefig('mc_plots/' + process_name + '/Gen_Muon_phi.png')
    plt.clf()

    """# Gen Particle ID
    ax = crep.create_plot1d(hists['GenPart_pdgId'])
    plt.savefig('mc_plots/' + process_name + '/Gen_particles_Id.png')
    plt.clf()

    ## Gen Jpsi

    # Gen Jpsi mass
    ax = crep.create_plot1d(hists['GenJpsi_mass'])
    plt.savefig('mc_plots/' + process_name + '/Gen_jpsi_mass.png')
    plt.clf()

    # Gen Jpsi pT
    ax = crep.create_plot1d(hists['GenJpsi_p'].sum('eta', 'phi'))
    plt.savefig('mc_plots/' + process_name + '/Gen_jpsi_pt.png')
    plt.clf()

    # Gen Jpsi eta
    ax = crep.create_plot1d(hists['GenJpsi_p'].sum('pt', 'phi'))
    plt.savefig('mc_plots/' + process_name + '/Gen_jpsi_eta.png')
    plt.clf()

    # Gen Jpsi phi
    ax = crep.create_plot1d(hists['GenJpsi_p'].sum('eta', 'pt'))
    plt.savefig('mc_plots/' + process_name + '/Gen_jpsi_phi.png')
    plt.clf() """

    """ ax = crep.create_plot1d(hists['GenJpsi_vx'])
    #ax = hists['GenJpsi_vx']
    #ax.rebin("VertexX", hist.Bin("VertexX", "Vertex x [cm]", 50, -0.1, 0.1))
    plt.savefig('mc_plots/' + process_name + '/GenJpsi_vx.png')
    plt.clf()

    ax = crep.create_plot1d(hists['GenJpsi_vy'])
    plt.savefig('mc_plots/' + process_name + '/GenJpsi_vy.png')
    plt.clf()

    ax = crep.create_plot1d(hists['GenJpsi_vz'])
    plt.savefig('mc_plots/' + process_name + '/GenJpsi_vz.png')
    plt.clf() """

    ## Gen Dstar

    # Gen Dstar mass
    """ ax = crep.create_plot1d(hists['GenDstar_deltam'])
    plt.savefig('mc_plots/' + process_name + '/Gen_dstar_deltam.png')
    plt.clf() """

    # Gen Dstar pT
    """ ax = crep.create_plot1d(hists['GenDstar_p'].sum('eta', 'phi'))
    plt.savefig('mc_plots/' + process_name + '/Gen_dstar_pt.png')
    plt.clf()

    # Gen Dstar eta
    ax = crep.create_plot1d(hists['GenDstar_p'].sum('pt', 'phi'))
    plt.savefig('mc_plots/' + process_name + '/Gen_dstar_eta.png')
    plt.clf()

    # Gen Dstar phi
    ax = crep.create_plot1d(hists['GenDstar_p'].sum('eta', 'pt'))
    plt.savefig('mc_plots/' + process_name + '/Gen_dstar_phi.png')
    plt.clf() 

    ax = crep.create_plot1d(hists['GenDstar_vx'])
    plt.savefig('mc_plots/' + process_name + '/GenDstar_vx.png')
    plt.clf()

    ax = crep.create_plot1d(hists['GenDstar_vy'])
    plt.savefig('mc_plots/' + process_name + '/GenDstar_vy.png')
    plt.clf()

    ax = crep.create_plot1d(hists['GenDstar_vz'])
    plt.savefig('mc_plots/' + process_name + '/GenDstar_vz.png')
    plt.clf()"""

def recPlots(file_path, process_name):

    hists = load(file)

    if (args.jpsi or args.all):
        ## Jpsi

        # Reco Jpsi mass
        ax = crep.create_plot1d(hists['Jpsi_mass'])
        plt.savefig('mc_plots/' + process_name + '/Reco_jpsi_mass.png')
        plt.clf()

        # Reco Jpsi pT
        ax = crep.create_plot1d(hists['Jpsi_p'].sum('eta', 'phi'))
        plt.savefig('mc_plots/' + process_name + '/Reco_jpsi_pt.png')
        plt.clf()

        # Reco Jpsi eta
        ax = crep.create_plot1d(hists['Jpsi_p'].sum('pt', 'phi'))
        plt.savefig('mc_plots/' + process_name + '/Reco_jpsi_eta.png')
        plt.clf()

        # Reco Jpsi phi
        ax = crep.create_plot1d(hists['Jpsi_p'].sum('eta', 'pt'))
        plt.savefig('mc_plots/' + process_name + '/Reco_jpsi_phi.png')
        plt.clf()

        # Reco Jpsi decay length
        ax = crep.create_plot1d(hists['Jpsi_dl'])
        plt.savefig('mc_plots/' + process_name + '/Reco_jpsi_dl.png')
        plt.clf()

        # Reco Jpsi decay length - Log scale
        ax = crep.create_plot1d(hists['Jpsi_dlSig'])
        ax.set_yscale('log')
        ax.set_xlim(-1,2) 
        ax.set_ylim(10, 1.8e6)
        ax.set_xlabel('Decay lenght [cm]')
        plt.savefig('mc_plots/' + process_name + '/Reco_jpsi_dl_logscale.png')
        plt.clf()

        # Reco Jpsi significance decay length
        ax = crep.create_plot1d(hists['Jpsi_dl'])
        plt.savefig('mc_plots/' + process_name + '/Reco_jpsi_dlSig.png')
        plt.clf()

        # Reco Jpsi significance decay length - Log scale
        ax = crep.create_plot1d(hists['Jpsi_dlSig'])
        ax.set_yscale('log')
        ax.set_xlim(-1,2) 
        ax.set_ylim(10, 1.8e6)
        ax.set_xlabel('Decay lenght [cm]')
        plt.savefig('mc_plots/' + process_name + '/Reco_jpsi_dlSig_logscale.png')
        plt.clf()

        # Reco Jpsi significance decay length
        ax = crep.create_plot1d(hists['Jpsi_cosphi'])
        plt.savefig('mc_plots/' + process_name + '/Reco_jpsi_cosphi.png')
        plt.clf()
    
    if (args.dstar or args.all):
        ## Dstar

        # Reco Dstar right charge mass
        ax = crep.create_plot1d(hists['Dstar_deltamr'].integrate('chg', 'right charge'))
        plt.savefig('mc_plots/' + process_name + '/Reco_dstar_right_charge_dmass.png')
        plt.clf()

        # Reco Dstar right charge pT
        ax = crep.create_plot1d(hists['Dstar_p'].integrate('chg', 'right charge').sum('eta','phi'))
        plt.savefig('mc_plots/' + process_name + '/Reco_dstar_right_charge_pt.png')
        plt.clf()

        # Reco Dstar right charge eta
        ax = crep.create_plot1d(hists['Dstar_p'].integrate('chg', 'right charge').sum('pt','phi'))
        plt.savefig('mc_plots/' + process_name + '/Reco_dstar_right_charge_eta.png')
        plt.clf()

        # Reco Dstar right charge phi
        ax = crep.create_plot1d(hists['Dstar_p'].integrate('chg', 'right charge').sum('eta','pt'))
        plt.savefig('mc_plots/' + process_name + '/Reco_dstar_right_charge_phi.png')
        plt.clf()

        # Reco Dstar wrong charge mass
        ax = crep.create_plot1d(hists['Dstar_deltamr'].integrate('chg', 'wrong charge'))
        plt.savefig('mc_plots/' + process_name + '/Reco_dstar_wrong_charge_dmass.png')
        plt.clf()

        # Reco Dstar wrong charge pT
        ax = crep.create_plot1d(hists['Dstar_p'].integrate('chg', 'wrong charge').sum('eta','phi'))
        plt.savefig('mc_plots/' + process_name + '/Reco_dstar_wrong_charge_pt.png')
        plt.clf()

        # Reco Dstar wrong charge eta
        ax = crep.create_plot1d(hists['Dstar_p'].integrate('chg', 'wrong charge').sum('pt','phi'))
        plt.savefig('mc_plots/' + process_name + '/Reco_dstar_wrong_charge_eta.png')
        plt.clf()

        # Reco Dstar wrong charge phi
        ax = crep.create_plot1d(hists['Dstar_p'].integrate('chg', 'wrong charge').sum('eta','pt'))
        plt.savefig('mc_plots/' + process_name + '/Reco_dstar_wrong_charge_phi.png')
        plt.clf()

        # Dstar rgth-wrg chg plot
        hist_wrg_chg = hists['Dstar_deltamr'].integrate('chg', 'wrong charge')
        hist_rgt_chg = hists['Dstar_deltamr'].integrate('chg', 'right charge')
        
        w = crep.get_dstar_weight(hist_rgt_chg, hist_wrg_chg)
        hist_wrg_chg.scale(w)
        
        ax, rax = crep.ratio_plot(hist_rgt_chg, hist_wrg_chg)
        
        handles, labels = ax.get_legend_handles_labels()
        labels = ['right charge', 'wrong charge']
        
        leg = ax.legend(handles, labels)
        
        rax.set_xlabel('$\Delta m$ [GeV]')
        plt.savefig('mc_plots/' + process_name + '/Reco_dstar_comparison_plot.png')
        print(f"weight: {w}")
        plt.clf()

        ## Dstar signal plot - background extracted

        # Takes the negative from the scaled wrong charged histogram.
        hist_wrg_chg.scale(-1)
        # Takes the difference between the right charge and scaled wrong charged
        histo = hist_rgt_chg + hist_wrg_chg
        #hist_wrg_chg.scale(1)
        ax = crep.create_plot1d(histo)
        ax.legend().remove()
        plt.savefig('mc_plots/' + process_name + '/Reco_dstar_no_background.png')
        plt.clf()

        ## Reco Dstar daughters section

        # Dstar D0 Kaon pT
        ax = crep.create_plot1d(hists['Dstar_K_p'].sum('eta','phi'))
        plt.savefig('mc_plots/' + process_name + '/Reco_dstar_K_pt.png')
        plt.clf()

        # Dstar D0 Kaon eta
        ax = crep.create_plot1d(hists['Dstar_K_p'].sum('pt','phi'))
        plt.savefig('mc_plots/' + process_name + '/Reco_dstar_K_eta.png')
        plt.clf()

        # Dstar D0 Kaon phi
        ax = crep.create_plot1d(hists['Dstar_K_p'].sum('pt','eta'))
        plt.savefig('mc_plots/' + process_name + '/Reco_dstar_K_phi.png')
        plt.clf()

        # Dstar D0 Pion pT
        ax = crep.create_plot1d(hists['Dstar_pi_p'].sum('eta','phi'))
        plt.savefig('mc_plots/' + process_name + '/Reco_dstar_pi_pt.png')
        plt.clf()

        # Dstar D0 Pion eta
        ax = crep.create_plot1d(hists['Dstar_pi_p'].sum('pt','phi'))
        plt.savefig('mc_plots/' + process_name + '/Reco_dstar_pi_eta.png')
        plt.clf()

        # Dstar D0 Pion phi
        ax = crep.create_plot1d(hists['Dstar_pi_p'].sum('pt','eta'))
        plt.savefig('mc_plots/' + process_name + '/Reco_dstar_pi_phi.png')
        plt.clf()

        # Dstar Pion slow pT
        ax = crep.create_plot1d(hists['Dstar_pis_p'].sum('eta','phi'))
        plt.savefig('mc_plots/' + process_name + '/Reco_dstar_pis_pt.png')
        plt.clf()

        # Dstar Pion slow eta
        ax = crep.create_plot1d(hists['Dstar_pis_p'].sum('pt','phi'))
        plt.savefig('mc_plots/' + process_name + '/Reco_dstar_pis_eta.png')
        plt.clf()

        # Dstar Pion slow phi
        ax = crep.create_plot1d(hists['Dstar_pis_p'].sum('pt','eta'))
        plt.savefig('mc_plots/' + process_name + '/Reco_dstar_pis_phi.png')
        plt.clf()


        


        



        

    







""" genPlots(file_path='../output/test_Monte_Carlo_2017_new_code/test_Monte_Carlo_2017_new_code_hists.coffea',
         process_name="new_processing") """
recPlots(file_path='../output/test_Monte_Carlo_2017_new_code/test_Monte_Carlo_2017_new_code_hists.coffea',
         process_name="new_processing")
