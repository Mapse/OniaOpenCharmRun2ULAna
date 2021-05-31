import awkward as ak
import numpy as np
import coffea.processor as processor
from coffea.util import save

from coffea.nanoevents.methods import candidate
ak.behavior.update(candidate.behavior)

import random

from tools.collections import *

D0_PDG_MASS = 1.864

loose = 0

def association(cand1, cand2):
    ''' Function for association of the particles. The cuts that operates on all of them and 
    computation of quantities can go here. individual cuts can go on the main processing'''

    #cut_dstar_back = ((cand2.deltamr > 0.143) & (cand2.deltamr < 0.148))
    #cand2 = cand2[cut_dstar_back]

    asso = ak.cartesian([cand1, cand2])    

    asso = asso[asso.slot0.vtxIdx == asso.slot1.vtxIdx]
    asso = asso[ak.num(asso) > 0]
    cand1 = ak.zip({
            'pt': asso.slot0.pt,
            'eta': asso.slot0.eta,
            'phi': asso.slot0.phi,
            'mass': asso.slot0.mass,
            'charge': asso.slot0.charge}, with_name="PtEtaPhiMCandidate")

    cand2 = ak.zip({
            'pt': asso.slot1.pt,
            'eta': asso.slot1.eta,
            'phi': asso.slot1.phi,
            'mass': asso.slot1.mass,
            'charge': asso.slot1.charge}, with_name="PtEtaPhiMCandidate")

    asso['deltarap'] = asso.slot0.rap - asso.slot1.rap
    asso['cand'] = cand1 + cand2
    
    return asso

def mc_matching(muonrec1, muonrec2, dimurec, *genpart):
    ''' Function for the matching between the reco and gen particles. The cuts that operates on all of them and 
    computation of quantities can go here. individual cuts can go on the main processing. The first candidate
    is chosen to be the reconstructed one'''

    #mc_matching(Muon.slot0, Muon.slot1, Gen_particles)
    #mc_matching(Muon.slot0, Muon.slot0, Muon1_Gen, Muon2_Gen)

    match1 = ak.cartesian([muonrec1, genpart[0]])
    match1 = match1[match1.slot0.simIdx == match1.slot1.Id]
    dimurec = dimurec[match1.slot0.simIdx == match1.slot1.Id]
    match1 = match1[ak.num(match1) > 0]

    if (len(genpart) == 1):
        match2 = ak.cartesian([muonrec2, genpart[0]])
        match2 = match2[match2.slot0.simIdx == match2.slot1.Id]
        dimurec = dimurec[match2.slot0.simIdx == match2.slot1.Id]
        match2 = match2[ak.num(match2) > 0]
    elif (len(genpart) == 2):
        match2 = ak.cartesian([muonrec2, genpart[1]])
        match2 = match2[match2.slot0.simIdx == match2.slot1.Id]
        dimurec = dimurec[match2.slot0.simIdx == match2.slot1.Id]
        match2 = match2[ak.num(match2) > 0]
 
    muonrec1 = ak.zip({
            'pt': match1.slot0.pt,
            'eta': match1.slot0.eta,
            'phi': match1.slot0.phi,
            'mass': match1.slot0.mass,
            'Id': match1.slot0.Id,
            'simIdx' : match1.slot0.simIdx}, with_name="PtEtaPhiMCandidate")

    muongen1 = ak.zip({
            'pt': match1.slot1.pt,
            'eta': match1.slot1.eta,
            'phi': match1.slot1.phi,
            'mass': match1.slot1.mass,
            'Id' : match1.slot1.Id,
            'pdgId': match1.slot1.pdgId,
            'genPartIdxMother': match1.slot1.genPartIdxMother,
            'parpdgId' : match1.slot1.parpdgId}, with_name="PtEtaPhiMCandidate")

    muonrec2 = ak.zip({
            'pt': match2.slot0.pt,
            'eta': match2.slot0.eta,
            'phi': match2.slot0.phi,
            'mass': match2.slot0.mass,
            'Id': match2.slot0.Id,
            'simIdx' : match2.slot0.simIdx}, with_name="PtEtaPhiMCandidate")

    muongen2 = ak.zip({
            'pt': match2.slot1.pt,
            'eta': match2.slot1.eta,
            'phi': match2.slot1.phi,
            'mass': match2.slot1.mass,
            'Id' : match2.slot1.Id,
            'pdgId': match2.slot1.pdgId,
            'genPartIdxMother': match2.slot1.genPartIdxMother,
            'parpdgId' : match2.slot1.parpdgId}, with_name="PtEtaPhiMCandidate")
        
    return muonrec1, muongen1, muonrec2, muongen2, dimurec

class MonteCarloEventSelectorProcessor(processor.ProcessorABC):
    def __init__(self, analyzer_name, analysis_type):
        self.analyzer_name = analyzer_name
        self.analysis_type = analysis_type

        self._accumulator = processor.dict_accumulator({
            'cutflow': processor.defaultdict_accumulator(int),
        })

    @property
    def accumulator(self):
        return self._accumulator

    def process(self, events):
        output = self.accumulator.identity()

        ############### Cuts
        # Dimu cuts: charge = 0, mass cuts and chi2...
        # test if there is any events in the file
        if len(events) == 0:
            return output

        ############### Get the main primary vertex properties ############### 
        Primary_vertex = ak.zip({**get_vars_dict(events, primary_vertex_cols)})

        ############### Get the gen particles ############### 

        if (self.analysis_type == 'mc'): 

            # All gen particles
            Gen_particles = ak.zip({**get_vars_dict(events, gen_part_cols)})

            # Gen Muons
            Gen_Muon = Gen_particles[(Gen_particles.pdgId == 13) | (Gen_particles.pdgId == -13)]

            # Gen Jpsi
            Gen_Jpsi = Gen_particles[Gen_particles.pdgId == 443]

            # Gen D0
            Gen_D0 = Gen_particles[(Gen_particles.pdgId == 421) | (Gen_particles.pdgId == -421)]

            # Gen Dstar
            Gen_Dstar_all = Gen_particles[(Gen_particles.pdgId == 413) | (Gen_particles.pdgId == -413)]
            
            # Forces it to has only two daughters
            Gen_Dstar_all = Gen_Dstar_all[Gen_Dstar_all.numberOfDaughters == 2]
                        
            # Dstar daughters: D0
            Gen_D0Dstar = ak.cartesian([Gen_D0, Gen_Dstar_all])  # This associates each candidate in an array with each candidate in the other array
    
            # Require the id for D0 mothers as the id for Dstar
            Gen_D0Dstar = Gen_D0Dstar[Gen_D0Dstar.slot0.genPartIdxMother == Gen_D0Dstar.slot1.Id]
            Gen_D0Dstar = Gen_D0Dstar[ak.num(Gen_D0Dstar) > 0]
            
            # Put the candidate D0 back to it array
            Gen_D0OfDstar = ak.zip({
                        'pt': Gen_D0Dstar.slot0.pt,
                        'eta': Gen_D0Dstar.slot0.eta,
                        'phi': Gen_D0Dstar.slot0.phi,
                        'mass': Gen_D0Dstar.slot0.mass}, with_name="PtEtaPhiMCandidate")
            
            # This is the final Dstar we want
            Gen_Dstar = ak.zip({
                        'pt': Gen_D0Dstar.slot1.pt,
                        'eta': Gen_D0Dstar.slot1.eta,
                        'phi': Gen_D0Dstar.slot1.phi,
                        'mass': Gen_D0Dstar.slot1.mass,
                        'vx': Gen_D0Dstar.slot1.vx,
                        'vy': Gen_D0Dstar.slot1.vy,
                        'vz': Gen_D0Dstar.slot1.vz}, with_name="PtEtaPhiMCandidate")
            Gen_Dstar = Gen_Dstar[ak.num(Gen_Dstar) == 3]

            # test
            """ asso = ak.cartesian([Gen_Dstar, Gen_Jpsi])    

            asso = asso[(asso.slot0.vx == asso.slot1.vx) & (asso.slot0.vy == asso.slot1.vy) & (asso.slot0.vz == asso.slot1.vz) ]
            asso = asso[ak.num(asso) > 0]
            Gen_Dstar = ak.zip({
                    'pt': asso.slot0.pt,
                    'eta': asso.slot0.eta,
                    'phi': asso.slot0.phi,
                    'mass': asso.slot0.mass,
                    'vx': asso.slot0.vx,
                    'vy': asso.slot0.vy,
                    'vz': asso.slot0.vz}, with_name="PtEtaPhiMCandidate")
            Gen_Jpsi = ak.zip({
                    'pt': asso.slot1.pt,
                    'eta': asso.slot1.eta,
                    'phi': asso.slot1.phi,
                    'mass': asso.slot1.mass,
                    'vx': asso.slot1.vx,
                    'vy': asso.slot1.vy,
                    'vz': asso.slot1.vz}, with_name="PtEtaPhiMCandidate") """

            
        elif (self.analysis_type == 'data'):
            Gen_particles = ak.zip([[]])
              
        ############### Get All the interesting candidates from NTuples
        Dimu = ak.zip({**get_vars_dict(events, dimu_cols)}, with_name="PtEtaPhiMCandidate")
        Muon = ak.zip({**get_vars_dict(events, muon_cols)}, with_name="PtEtaPhiMCandidate")
        D0 = ak.zip({'mass': events.D0_mass12, **get_vars_dict(events, d0_cols)}, with_name="PtEtaPhiMCandidate")
        Dstar = ak.zip({'mass': (events.Dstar_D0mass + events.Dstar_deltamr),
                        'charge': events.Dstar_pischg,
                        **get_vars_dict(events, dstar_cols)}, 
                        with_name="PtEtaPhiMCandidate")

        output['cutflow']['Number of events'] += len(events)
        output['cutflow']['Number of Dimu'] += ak.sum(ak.num(Dimu))
        output['cutflow']['all D0']      += ak.sum(ak.num(D0))
        output['cutflow']['all Dstar']   += ak.sum(ak.num(Dstar))

        ############### Dimu cuts charge = 0, mass cuts and chi2...
        Dimu = Dimu[Dimu.charge == 0]
        output['cutflow']['Dimu 0 charge'] += ak.sum(ak.num(Dimu))

        Dimu = Dimu[((Dimu.mass > 8.5) & (Dimu.mass < 11.5)) | ((Dimu.mass > 2.9) & (Dimu.mass < 3.3)) | ((Dimu.mass > 3.35) & (Dimu.mass < 4.05))]
        output['cutflow']['Quarkonia mass'] += ak.sum(ak.num(Dimu))
        
        # Prompt/nomprompt cut for jpsi
        dimuon_prompt_cut = (Dimu.dlSig > 0) & (Dimu.dlSig < 2.5)
        dimuon_nonprompt_cut = (Dimu.dlSig > 4) 
        #Dimu = Dimu[dimuon_nonprompt_cut]
        #output['cutflow']['Dimu prompt'] += ak.sum(ak.num(Dimu))

        # Pointing angle cut for jpsi
        dimuon_pointing_cut = (Dimu.cosphi > 0.99)
        #Dimu = Dimu[dimuon_pointing_cut]

        ############### Get the Muons from Dimu, for cuts in their params
        Muon = ak.zip({'0': Muon[Dimu.t1muIdx], '1': Muon[Dimu.t2muIdx]})

        # SoftId and Global Muon cuts
        soft_id = (Muon.slot0.softId > 0) & (Muon.slot1.softId > 0)
        Dimu = Dimu[soft_id]
        Muon = Muon[soft_id]
        output['cutflow']['Dimu muon softId'] += ak.sum(ak.num(Dimu))

        global_muon = (Muon.slot0.isGlobal > 0) & (Muon.slot1.isGlobal > 0)
        Dimu = Dimu[global_muon]
        Muon = Muon[global_muon]
        output['cutflow']['Dimu muon global'] += ak.sum(ak.num(Dimu))

        # pt and eta cuts
        if loose:
            muon_pt_cut = (Muon.slot0.pt > 1) & (Muon.slot1.pt > 1)

        else:
            
            muon_pt_cut = (Muon.slot0.pt > 3) & (Muon.slot1.pt > 3)
        
        Dimu = Dimu[muon_pt_cut]
        Muon = Muon[muon_pt_cut]
        output['cutflow']['Dimu muon pt cut'] += ak.sum(ak.num(Dimu))

        muon_eta_cut = (np.absolute(Muon.slot0.eta) <= 2.4) & (np.absolute(Muon.slot1.eta) <= 2.4)
        Dimu = Dimu[muon_eta_cut]
        Muon = Muon[muon_eta_cut]
        
        output['cutflow']['Dimu muon eta cut'] += ak.sum(ak.num(Dimu))

        """ ################################################################## Matching of the muon
        
        Muon1_Rec, Muon1_Gen, Muon2_Rec, Muon2_Gen, dimurec = mc_matching(Muon.slot0, Muon.slot1, Dimu, Gen_particles)
        ##################33possibilidade: Pegar as gen particles como muons!!!!!!!!!!!!!!!!!!!
        Gendimu_match_dimu = ak.zip([Muon1_Gen, Muon2_Gen])

        Gendimu_same_mother = Gendimu_match_dimu[Gendimu_match_dimu.slot0.genPartIdxMother == Gendimu_match_dimu.slot1.genPartIdxMother]
        Gendimu_same_mother = Gendimu_same_mother[Gendimu_same_mother.slot0.parpdgId == 443]

        Muon1_Gen = ak.zip({
            'pt': Gendimu_same_mother.slot0.pt,
            'eta': Gendimu_same_mother.slot0.eta,
            'phi': Gendimu_same_mother.slot0.phi,
            'mass': Gendimu_same_mother.slot0.mass,
            'Id' : Gendimu_same_mother.slot0.Id,
            'pdgId': Gendimu_same_mother.slot0.pdgId,
            'genPartIdxMother': Gendimu_same_mother.slot0.genPartIdxMother,
            'parpdgId' : Gendimu_same_mother.slot0.parpdgId}, with_name="PtEtaPhiMCandidate")

        Muon2_Gen = ak.zip({
            'pt': Gendimu_same_mother.slot1.pt,
            'eta': Gendimu_same_mother.slot1.eta,
            'phi': Gendimu_same_mother.slot1.phi,
            'mass': Gendimu_same_mother.slot1.mass,
            'Id' : Gendimu_same_mother.slot1.Id,
            'pdgId': Gendimu_same_mother.slot1.pdgId,
            'genPartIdxMother': Gendimu_same_mother.slot1.genPartIdxMother,
            'parpdgId' : Gendimu_same_mother.slot1.parpdgId}, with_name="PtEtaPhiMCandidate")

        Muon1_Rec, Muon1_Gen, Muon2_Rec, Muon2_Gen, dimurec = mc_matching(Muon1_Rec, Muon2_Rec, dimurec, Muon1_Gen, Muon2_Gen)
        #print(ak.sum(ak.num(Muon1_Rec))) """
        #print(ak.sum(ak.num(dimurec)))
        #Muon = ak.zip({'0': Muon1_Rec, '1': Muon2_Rec})
        #Muon = ak.zip({'0': Muon[Dimu.t1muIdx], '1': Muon[Dimu.t2muIdx]})
        #print(Dimu.t1muIdx)
        #print(Muon.slot0.Id)
        #Dimu = Dimu[Dimu.t1muIdx == Muon.Id]
        #Dimu == Dimu[Muon.Id]
        #print(Dimu)
        
        #Muon.slot0 = Muon1_Rec
        #Muon.slot1 = Muon2_Rec

        #print(Muon.slot0)
        #print("sdsadsadsadsad")
        #print(Muon1_Rec)

        #Muon = ak.zip({'0': Muon[Dimu.t1muIdx], '1': Muon[Dimu.t2muIdx]})



        
        #dimu_pt_cut = (Dimu.pt > 22) & (Dimu.pt < 26)
        #Dimu = Dimu[dimu_pt_cut]

        #dimu_rap_cut = (Dimu.rap > 1.2) & (Dimu.rap < 1.8)
        #Dimu = Dimu[dimu_rap_cut]

        Dimu['is_ups'] = (Dimu.mass > 8.5) & (Dimu.mass < 11.5)
        Dimu['is_jpsi'] = (Dimu.mass > 2.9) & (Dimu.mass < 3.3)
        Dimu['is_psi'] = (Dimu.mass > 3.35) & (Dimu.mass < 4.05)

        ############### Cuts for D0
        D0 = D0[~D0.hasMuon]
        D0noncut = D0
        output['cutflow']['D0 trk muon cut'] += ak.sum(ak.num(D0))

        if loose:
            D0 = D0[(D0.t1pt > 0.4) & (D0.t2pt > 0.4)]
            output['cutflow']['D0 trk pt cut'] += ak.sum(ak.num(D0))

            D0 = D0[(D0.t1chindof < 4) & (D0.t2chindof < 4)]
            output['cutflow']['D0 trk chi2 cut'] += ak.sum(ak.num(D0))

            D0 = D0[(D0.t1nValid > 2) & (D0.t2nValid > 2) & (D0.t1nPix > 1) & (D0.t2nPix > 1)]
            output['cutflow']['D0 trk hits cut'] += ak.sum(ak.num(D0))

            D0 = D0[(D0.t1dxy < 0.1) & (D0.t2dxy < 0.1)]
            output['cutflow']['D0 trk dxy cut'] += ak.sum(ak.num(D0))

            D0 = D0[(D0.t1dz < 1.) & (D0.t2dz < 1.)]
            output['cutflow']['D0 trk dz cut'] += ak.sum(ak.num(D0))
        
        else:
            
            #D0 = D0[(D0.t1pt > 0.8) & (D0.t2pt > 0.8)]
            output['cutflow']['D0 trk pt cut'] += ak.sum(ak.num(D0))

            #D0 = D0[(D0.t1chindof < 2.5) & (D0.t2chindof < 2.5)]
            output['cutflow']['D0 trk chi2 cut'] += ak.sum(ak.num(D0))

            #D0 = D0[(D0.t1nValid > 4) & (D0.t2nValid > 4) & (D0.t1nPix > 1) & (D0.t1nPix > 1)]
            output['cutflow']['D0 trk hits cut'] += ak.sum(ak.num(D0))

            #D0 = D0[(D0.t1dxy < 0.1) & (D0.t2dxy < 0.1)]
            output['cutflow']['D0 trk dxy cut'] += ak.sum(ak.num(D0))

            #D0 = D0[(D0.t1dz < 1.) & (D0.t2dz < 1.)]
            output['cutflow']['D0 trk dz cut'] += ak.sum(ak.num(D0))

        # D0 cosphi
        if loose:
            D0 = D0[D0.cosphi > 0.1]

        else:

            #D0 = D0[D0.cosphi > 0.99]
            print("yeah")
        output['cutflow']['D0 cosphi cut'] += ak.sum(ak.num(D0))

        # D0 dl Significance
        if loose:
            D0 = D0[D0.dlSig > 5.]
        else:

            #D0 = D0[D0.dlSig > 5.]
            print("yeah")
        output['cutflow']['D0 dlSig cut'] += ak.sum(ak.num(D0))

        # D0 pt
        D0 = D0[D0.pt > 3.]
        output['cutflow']['D0 pt cut'] += ak.sum(ak.num(D0))

        #D0 = D0noncut

        ############### Cuts for Dstar

        # trks cuts
        Dstar = Dstar[~Dstar.hasMuon]
        output['cutflow']['Dstar trk muon cut'] += ak.sum(ak.num(Dstar))

        Dstar = Dstar[(Dstar.Kpt > 0.5) & (Dstar.pipt > 0.5)]
        output['cutflow']['Dstar trk pt cut'] += ak.sum(ak.num(Dstar))

        Dstar = Dstar[(Dstar.Kchindof < 2.5) & (Dstar.pichindof < 2.5)]
        output['cutflow']['Dstar trk pt cut'] += ak.sum(ak.num(Dstar))

        Dstar = Dstar[(Dstar.KnValid > 4) & (Dstar.pinValid > 4) & (Dstar.KnPix > 1) & (Dstar.pinPix > 1)]
        output['cutflow']['Dstar trk hits cut'] += ak.sum(ak.num(Dstar))

        Dstar = Dstar[(Dstar.Kdxy < 0.1) & (Dstar.pidxy < 0.1)]
        output['cutflow']['Dstar trk pt cut'] += ak.sum(ak.num(Dstar))

        Dstar = Dstar[(Dstar.Kdz < 1) & (Dstar.pidz < 1)]
        output['cutflow']['Dstar trk pt cut'] += ak.sum(ak.num(Dstar))

        # pis cuts
        Dstar = Dstar[Dstar.pispt > 0.3]
        output['cutflow']['Dstar pis pt cut'] += ak.sum(ak.num(Dstar))

        Dstar = Dstar[Dstar.pischindof < 3]
        output['cutflow']['Dstar pis chi2 cut'] += ak.sum(ak.num(Dstar))

        Dstar = Dstar[Dstar.pisnValid > 2]
        output['cutflow']['Dstar pis hits cut'] += ak.sum(ak.num(Dstar))

        # D0 of Dstar cuts
        Dstar = Dstar[Dstar.D0cosphi > 0.99]
        output['cutflow']['Dstar D0 cosphi cut'] += ak.sum(ak.num(Dstar))

        Dstar = Dstar[(Dstar.D0mass < D0_PDG_MASS + 0.028) & (Dstar.D0mass > D0_PDG_MASS - 0.028)]
        output['cutflow']['Dstar D0 mass cut'] += ak.sum(ak.num(Dstar))

        Dstar = Dstar[Dstar.D0pt > 3]
        output['cutflow']['Dstar D0 pt cut'] += ak.sum(ak.num(Dstar))

        Dstar = Dstar[Dstar.D0dlSig > 3]
        output['cutflow']['Dstar D0 dlSig cut'] += ak.sum(ak.num(Dstar))

        Dstar['wrg_chg'] = (Dstar.Kchg == Dstar.pichg)

        ############### Dimu Monte Carlo Matching
        #rec, gen = mc_matching(Dimu, Gen_Jpsi)
        #print(rec)
        #print(gen)

        ############### Dimu + OpenCharm associations

        DimuDstar = association(Dimu, Dstar)

        ############### Final computation of number of objects
        output['cutflow']['Dimu final']    += ak.sum(ak.num(Dimu))
        output['cutflow']['D0 final']      += ak.sum(ak.num(D0))
        output['cutflow']['Dstar final']   += ak.sum(ak.num(Dstar))
        output['cutflow']['Dimu Dstar Associated'] += ak.sum(ak.num(DimuDstar))

        ############### Leading and Trailing muon separation Gen_particles
        leading_mu = (Muon.slot0.pt > Muon.slot1.pt)
        Muon_lead = ak.where(leading_mu, Muon.slot0, Muon.slot1)
        Muon_trail = ak.where(~leading_mu, Muon.slot0, Muon.slot1)

        ############### Create the accumulators to save output

        # Primary vertex accumulator
        primary_vertex_acc = processor.dict_accumulator({})
        for var in Primary_vertex.fields:
            primary_vertex_acc[var] = processor.column_accumulator(ak.to_numpy(Primary_vertex[var]))
        output["Primary_vertex"] = primary_vertex_acc

        # Gen Particles accumulator
        gen_part_acc = processor.dict_accumulator({})
        if (self.analysis_type == 'mc'):
            for var in Gen_particles.fields:
                gen_part_acc[var] = processor.column_accumulator(ak.to_numpy(ak.flatten(Gen_particles[var])))
            gen_part_acc['nGenPart'] = processor.column_accumulator(ak.to_numpy(ak.num(Gen_particles))) 
            output["Gen_particles"] = gen_part_acc

        # Gen Muon accumulator
        gen_muon_acc = processor.dict_accumulator({})
        if (self.analysis_type == 'mc'):
            for var in Gen_Muon.fields:
                gen_muon_acc[var] = processor.column_accumulator(ak.to_numpy(ak.flatten(Gen_Muon[var])))
            gen_muon_acc['nGenMuon'] = processor.column_accumulator(ak.to_numpy(ak.num(Gen_Muon))) 
            output["Gen_Muon"] = gen_muon_acc

        # Gen Jpsi accumulator
        gen_jpsi_acc = processor.dict_accumulator({})
        if (self.analysis_type == 'mc'):
            for var in Gen_Jpsi.fields:
                gen_jpsi_acc[var] = processor.column_accumulator(ak.to_numpy(ak.flatten(Gen_Jpsi[var])))
            gen_jpsi_acc['nGenJpsi'] = processor.column_accumulator(ak.to_numpy(ak.num(Gen_Jpsi))) 
            output["Gen_Jpsi"] = gen_jpsi_acc
            
        # Gen D0 accumulator
        gen_d0_acc = processor.dict_accumulator({})
        if (self.analysis_type == 'mc'):
            for var in Gen_D0.fields:
                gen_d0_acc[var] = processor.column_accumulator(ak.to_numpy(ak.flatten(Gen_D0[var])))
            gen_d0_acc['nGenD0'] = processor.column_accumulator(ak.to_numpy(ak.num(Gen_D0[var])))
            output["Gen_D0"] = gen_d0_acc

        # Gen Dstar accumulator
        gen_dstar_acc = processor.dict_accumulator({})
        if (self.analysis_type == 'mc'):
            for var in Gen_Dstar.fields:
                gen_dstar_acc[var] = processor.column_accumulator(ak.to_numpy(ak.flatten(Gen_Dstar[var])))
            gen_dstar_acc['nGenDstar'] = processor.column_accumulator(ak.to_numpy(ak.num(Gen_Dstar[var])))
            output["Gen_Dstar"] = gen_dstar_acc
            
    
        muon_lead_acc = processor.dict_accumulator({})
        for var in Muon_lead.fields:
            muon_lead_acc[var] = processor.column_accumulator(ak.to_numpy(ak.flatten(Muon_lead[var])))
        muon_lead_acc["nMuon"] = processor.column_accumulator(ak.to_numpy(ak.num(Muon_lead)))
        output["Muon_lead"] = muon_lead_acc
        

        muon_trail_acc = processor.dict_accumulator({})
        for var in Muon_trail.fields:
            muon_trail_acc[var] = processor.column_accumulator(ak.to_numpy(ak.flatten(Muon_trail[var])))
        muon_trail_acc["nMuon"] = processor.column_accumulator(ak.to_numpy(ak.num(Muon_trail)))
        output["Muon_trail"] = muon_trail_acc

        dimu_acc = processor.dict_accumulator({})
        for var in Dimu.fields:
            if (var.startswith('t')): continue
            dimu_acc[var] = processor.column_accumulator(ak.to_numpy(ak.flatten(Dimu[var])))
        dimu_acc["nDimu"] = processor.column_accumulator(ak.to_numpy(ak.num(Dimu)))
        output["Dimu"] = dimu_acc

        D0_acc = processor.dict_accumulator({})
        D0_trk_acc = processor.dict_accumulator({})
        for var in D0.fields:
            if (var.startswith('t')):
                D0_trk_acc[var] = processor.column_accumulator(ak.to_numpy(ak.flatten(D0[var])))
            else:
                D0_acc[var] = processor.column_accumulator(ak.to_numpy(ak.flatten(D0[var])))
        D0_acc["nD0"] = processor.column_accumulator(ak.to_numpy(ak.num(D0)))
        output["D0"] = D0_acc
        output["D0_trk"] = D0_trk_acc

        Dstar_acc = processor.dict_accumulator({})
        Dstar_D0_acc = processor.dict_accumulator({})
        Dstar_trk_acc = processor.dict_accumulator({})
        for var in Dstar.fields:
            if var.startswith('D0'):
                Dstar_D0_acc[var] = processor.column_accumulator(ak.to_numpy(ak.flatten(Dstar[var])))
            elif (var.startswith('K') or var.startswith('pi')):
                Dstar_trk_acc[var] = processor.column_accumulator(ak.to_numpy(ak.flatten(Dstar[var])))
            else:
                Dstar_acc[var] = processor.column_accumulator(ak.to_numpy(ak.flatten(Dstar[var])))
        Dstar_acc["nDstar"] = processor.column_accumulator(ak.to_numpy(ak.num(Dstar)))
        output["Dstar"] = Dstar_acc
        output["Dstar_D0"] = Dstar_D0_acc
        output["Dstar_trk"] = Dstar_trk_acc

        DimuDstar_acc = processor.dict_accumulator({})
        DimuDstar_acc['Dimu'] = processor.dict_accumulator({})
        DimuDstar_acc['Dstar'] = processor.dict_accumulator({})
        for var in DimuDstar.fields:
            if (var == '0') or (var =='1'):
                continue
            elif var == 'cand':
                for i0 in DimuDstar[var].fields:
                    DimuDstar_acc[i0] = processor.column_accumulator(ak.to_numpy(ak.flatten(DimuDstar[var][i0])))
            else:
                DimuDstar_acc[var] = processor.column_accumulator(ak.to_numpy(ak.flatten(DimuDstar[var])))

        for var in DimuDstar.slot0.fields:
            DimuDstar_acc['Dimu'][var] = processor.column_accumulator(ak.to_numpy(ak.flatten(DimuDstar.slot0[var])))

        for var in DimuDstar.slot1.fields:
            DimuDstar_acc['Dstar'][var] = processor.column_accumulator(ak.to_numpy(ak.flatten(DimuDstar.slot1[var])))
        DimuDstar_acc['nDimuDstar'] = processor.column_accumulator(ak.to_numpy(ak.num(DimuDstar)))
        output['DimuDstar'] = DimuDstar_acc

        file_hash = str(random.getrandbits(128)) + str(len(events))
        save(output, "output/" + self.analyzer_name + "/" + self.analyzer_name + "_" + file_hash + ".coffea")

        # return dummy accumulator
        return processor.dict_accumulator({
                'cutflow': output['cutflow']
        })

    def postprocess(self, accumulator):
        return accumulator
