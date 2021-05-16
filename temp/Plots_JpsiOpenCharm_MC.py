import os

import awkward as ak
from coffea.util import load

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
    plt.savefig('Reconstructed_primary_vertex.png')
    plt.clf()

    ## Gen Particles section

    ## ----------- Gen Particles section ----------- ##

    # Gen Particle ID
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
    plt.clf()

    ## Gen Dstar












genPlots(file_path='../output/test_Monte_Carlo_2017_new_code/test_Monte_Carlo_2017_new_code_hists.coffea',
         process_name="new_processing")