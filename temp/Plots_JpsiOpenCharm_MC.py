import os

import awkward as ak
from coffea.util import load
from coffea import hist


import matplotlib.pyplot as plt

import create_plots as crep


from coffea.nanoevents.methods import candidate
ak.behavior.update(candidate.behavior)

file = '../output/test_Monte_Carlo_2017_new_code/test_Monte_Carlo_2017_new_code_hists.coffea'

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

    ## Jpsi

    # Gen Jpsi mass
    ax = crep.create_plot1d(hists['Jpsi_mass'])
    plt.savefig('mc_plots/' + process_name + '/Reco_jpsi_mass.png')
    plt.clf()

    # Gen Jpsi pT
    ax = crep.create_plot1d(hists['Jpsi_p'].sum('eta', 'phi'))
    plt.savefig('mc_plots/' + process_name + '/Reco_jpsi_pt.png')
    plt.clf()

    # Gen Jpsi eta
    ax = crep.create_plot1d(hists['Jpsi_p'].sum('pt', 'phi'))
    plt.savefig('mc_plots/' + process_name + '/Reco_jpsi_eta.png')
    plt.clf()

    # Gen Jpsi phi
    ax = crep.create_plot1d(hists['Jpsi_p'].sum('eta', 'pt'))
    plt.savefig('mc_plots/' + process_name + '/Reco_jpsi_phi.png')
    plt.clf()







genPlots(file_path='../output/test_Monte_Carlo_2017_new_code/test_Monte_Carlo_2017_new_code_hists.coffea',
         process_name="new_processing")
""" recPlots(file_path='../output/test_Monte_Carlo_2017_new_code/test_Monte_Carlo_2017_new_code_hists.coffea',
         process_name="new_processing") """
