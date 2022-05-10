from coffea import processor
from tqdm import tqdm

import awkward as ak
from coffea.util import load, save

from coffea.nanoevents.methods import candidate
ak.behavior.update(candidate.behavior)

import numpy as np
import config_trigger_processor as config


def build_p4(acc):
    p4 = ak.zip({'x': acc['x'].value, 
                 'y': acc['y'].value,
                 'z': acc['z'].value,
                 't': acc['t'].value}, with_name="LorentzVector")

    return p4

class TriggerProcessor(processor.ProcessorABC):
   
    '''
        
        A coffea processor class
        
     '''

    def __init__(self, analyzer_name):

        '''
        
        Initialize the processor with a name (can be any name) and an accumulator.
        
        '''
        self.analyzer_name = analyzer_name

        self._accumulator = processor.dict_accumulator({})
        
    @property
    def accumulator(self):
        return self._accumulator
     
    def process(self, acc):

        '''

        This function is used load the summed accumulator for the desired particles. Then for each DimuStar it creates
        an awkward vector, unflatten it and apply the desired trigger.
        
        acc (dict_accumulator): Summed accumulator with the particle information.


        '''
        # Creates the output
        output = self.accumulator.identity()
    
        # Opens the accumulator for each object (particles, vertices, trigger...

        # Takes the number of events with JpsiDstar before trigger
        DimuDstar_acc = acc['DimuDstar']
        HLT_2018_acc = acc['HLT_2018']
        DimuDstar_p4 = build_p4(DimuDstar_acc)     

        ## DimuDstar collection

        # Creates the pt, eta, phi, m lorentz vector.
        DimuDstar = ak.zip({
            'jpsi_mass' : DimuDstar_acc['Dimu']['mass'].value,
            'jpsi_pt' : DimuDstar_acc['Dimu']['pt'].value,
            'jpsi_eta' : DimuDstar_acc['Dimu']['eta'].value,
            'jpsi_phi' : DimuDstar_acc['Dimu']['phi'].value,
            'jpsi_rap' : DimuDstar_acc['Dimu']['rap'].value,
            'dstar_deltam' : DimuDstar_acc['Dstar']['deltam'].value,
            'dstar_deltamr' : DimuDstar_acc['Dstar']['deltamr'].value,
            'dstar_pt' : DimuDstar_acc['Dstar']['pt'].value,
            'dstar_eta' : DimuDstar_acc['Dstar']['eta'].value,
            'dstar_phi' : DimuDstar_acc['Dstar']['phi'].value,
            'dstar_rap' : DimuDstar_acc['Dstar']['rap'].value,
            'dimu_dstar_deltarap' : DimuDstar_acc['deltarap'].value,
            'dimu_dstar_mass' : DimuDstar_p4.mass, #is_jpsi & ~wrg_chg & dlSig & dlSig_D0Dstar
            'is_jpsi' : DimuDstar_acc['Dimu']['is_jpsi'].value,
            'wrg_chg': DimuDstar_acc['Dstar']['wrg_chg'].value,}, with_name='PtEtaPhiMCandidate')  
        
        # Unflatten it to apply trigger
        DimuDstar = ak.unflatten(DimuDstar, DimuDstar_acc['nDimuDstar'].value)
        # Takes available triggers
        hlt_filter_2018 = config.hlt_filter_2018
        hlt_filter = hlt_filter_2018

        HLT_acc = HLT_2018_acc

        print(f"You are running with the trigger(s): {hlt_filter}")
        
        # Loop over trigger list. Applies OR condition to the trigger selection.
        trigger_cut = HLT_acc[hlt_filter[0]].value
        for i in range(0, len(hlt_filter)):
            trigger_cut |= HLT_acc[hlt_filter[i]].value

        #DimuDstar = DimuDstar[DimuDstar.jpsi_pt > 25]

        # Number of events with Jpsi Dstar before trigger
        evts_with_jpsidstar_before_trigger = len(DimuDstar[ak.num(DimuDstar) > 0])

        # Trigger cut
        DimuDstar = DimuDstar[trigger_cut]

        # Number of events with Jpsi Dstar after trigger
        evts_with_dimudstar_after_trigger  = len(DimuDstar[ak.num(DimuDstar) > 0])

        print(evts_with_jpsidstar_before_trigger)
        print(evts_with_dimudstar_after_trigger)

        print(f'Trigger efficiency: {(evts_with_dimudstar_after_trigger / evts_with_jpsidstar_before_trigger)*100.0} %')


        return output

    def postprocess(self, accumulator):
        return accumulator     


if __name__ == '__main__':

    # Path to the .coffea file
    path_file = config.path_file

    # Takes the coffea file
    ini = path_file.find('output/') + 7
    fin = len(path_file) -1
    file_in = path_file + path_file[ini: fin] + '.coffea'

    #Loads the accumulator
    acc = load(file_in)
   
    # Instatiate trigger processor, the argument is just a name, it can be anything
    p = TriggerProcessor('Trigger_Efficiency')
    #calls the function
    p.process(acc)
