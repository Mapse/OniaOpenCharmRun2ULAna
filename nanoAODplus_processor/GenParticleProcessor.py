from coffea import hist
from coffea.analysis_objects import JaggedCandidateArray
import coffea.processor as processor
from awkward import JaggedArray
import numpy as np

class GenParticleProcessor(processor.ProcessorABC):
   def __init__(self):
      dataset_axis = hist.Cat("dataset", "Process")

      Muon_lead_pt_axis = hist.Bin("pt", r"$p_{T,\mu}$ [GeV]", 3000, 0.25, 300)
      Muon_trail_pt_axis = hist.Bin("pt", r"$p_{T,\mu}$ [GeV]", 3000, 0.25, 300)
      Muon_eta_axis = hist.Bin("eta", r"$\eta_{\mu}$", 60, -3.0, 3.0)
      Muon_phi_axis = hist.Bin("phi", r"$\phi_{\mu}$", 70, -3.5, 3.5)

      Dimuon_mass_axis = hist.Bin("mass", r"$m_{\mu\mu}$ [GeV]", 200, 8.5, 10.5)
      Dimuon_pt_axis = hist.Bin("pt", r"$p_{T,\mu\mu}$ [GeV]", 3000, 0.25, 300)
      Dimuon_eta_axis = hist.Bin("eta", r"$\eta_{\mu\mu}$", 100, -5.0, 5.0)
      Dimuon_phi_axis = hist.Bin("phi", r"$\phi_{\mu\mu}$", 70, -3.5, 3.5)

      D0_mass_axis = hist.Bin("mass", r"$m_{D^0}$ [GeV]", 10, 1.2, 2.2)
      D0_pt_axis = hist.Bin("pt", r"$p_{T,D^0}$ [GeV]", 3000, 0.25, 300)
      D0_eta_axis = hist.Bin("eta", r"$\eta_{D^0}$", 100, -5.0, 5.0)
      D0_phi_axis = hist.Bin("phi", r"$\phi_{D^0}$", 70, -3.5, 3.5)

      D0_rec_mass_axis = hist.Bin("mass", r"$m_{D^0}$ [GeV]", 10, 1.85, 1.90)
      D0_rec_pt_axis = hist.Bin("pt", r"$p_{T,D^0}$ [GeV]", 3000, 0.25, 300)
      D0_rec_eta_axis = hist.Bin("eta", r"$\eta_{D^0}$", 100, -5.0, 5.0)
      D0_rec_phi_axis = hist.Bin("phi", r"$\phi_{D^0}$", 70, -3.5, 3.5)

      Dplus_rec_mass_axis = hist.Bin("mass", r"$m_{D^+}$ [GeV]", 10, 1.86, 1.88)
      Dplus_rec_pt_axis = hist.Bin("pt", r"$p_{T,D^+}$ [GeV]", 3000, 0.25, 300)
      Dplus_rec_eta_axis = hist.Bin("eta", r"$\eta_{D^+}$", 100, -5.0, 5.0)
      Dplus_rec_phi_axis = hist.Bin("phi", r"$\phi_{D^+}$", 70, -3.5, 3.5)

      Dsplus_rec_mass_axis = hist.Bin("mass", r"$m_{D^+_s}$ [GeV]", 10, 1.86, 2.00)
      Dsplus_rec_pt_axis = hist.Bin("pt", r"$p_{T,D^+_s}$[GeV]" , 3000, 0.25, 300)
      Dsplus_rec_eta_axis = hist.Bin("eta", r"$\eta_{D^+_s}$", 100, -5.0, 5.0)
      Dsplus_rec_phi_axis = hist.Bin("phi", r"$\phi_{D^+_s}$", 70, -3.5, 3.5)

      Dstarplus_rec_mass_axis = hist.Bin("mass", r"$m_{D^{*+}}$ [GeV]", 10, 1.86, 2.00)
      Dstarplus_rec_pt_axis = hist.Bin("pt", r"$p_{T,D^{*+}}$[GeV]" , 3000, 0.25, 300)
      Dstarplus_rec_eta_axis = hist.Bin("eta", r"$\eta_{D^{*+}s}$", 100, -5.0, 5.0)
      Dstarplus_rec_phi_axis = hist.Bin("phi", r"$\phi_{D^{*+}}$", 70, -3.5, 3.5)

      Lambdacplus_rec_mass_axis = hist.Bin("mass", r"$m_{\Lambda_c^+}$ [GeV]", 10, 2.00, 2.20)
      Lambdacplus_rec_pt_axis = hist.Bin("pt", r"$p_{T,\Lambda_c^+}$[GeV]" , 3000, 0.25, 300)
      Lambdacplus_rec_eta_axis = hist.Bin("eta", r"$\eta_{\Lambda_c^+}$", 100, -5.0, 5.0)
      Lambdacplus_rec_phi_axis = hist.Bin("phi", r"$\phi_{\Lambda_c^+}$", 70, -3.5, 3.5)
      
      self._accumulator = processor.dict_accumulator({
         'Muon_lead_pt': hist.Hist("Counts", dataset_axis, Muon_lead_pt_axis),
         'Muon_trail_pt': hist.Hist("Counts", dataset_axis, Muon_trail_pt_axis),
         'Muon_eta': hist.Hist("Counts", dataset_axis, Muon_eta_axis),
         'Muon_phi': hist.Hist("Counts", dataset_axis, Muon_phi_axis),
         'Dimuon_mass': hist.Hist("Counts", dataset_axis, Dimuon_mass_axis),
         'Dimuon_pt': hist.Hist("Counts", dataset_axis, Dimuon_pt_axis),
         'Dimuon_eta': hist.Hist("Counts", dataset_axis, Dimuon_eta_axis),
         'Dimuon_phi': hist.Hist("Counts", dataset_axis, Dimuon_phi_axis),
         'D0_mass': hist.Hist("Counts", dataset_axis, D0_mass_axis),
         'D0_pt': hist.Hist("Counts", dataset_axis, D0_pt_axis),
         'D0_eta': hist.Hist("Counts", dataset_axis, D0_eta_axis),
         'D0_phi': hist.Hist("Counts", dataset_axis, D0_phi_axis),
         'D0_rec_mass': hist.Hist("Counts", dataset_axis, D0_rec_mass_axis),
         'D0_rec_pt': hist.Hist("Counts", dataset_axis, D0_rec_pt_axis),
         'D0_rec_eta': hist.Hist("Counts", dataset_axis, D0_rec_eta_axis),
         'D0_rec_phi': hist.Hist("Counts", dataset_axis, D0_rec_phi_axis),
         'Dplus_rec_mass': hist.Hist("Counts", dataset_axis, Dplus_rec_mass_axis),
         'Dplus_rec_pt': hist.Hist("Counts", dataset_axis, Dplus_rec_pt_axis),
         'Dplus_rec_eta': hist.Hist("Counts", dataset_axis, Dplus_rec_eta_axis),
         'Dplus_rec_phi': hist.Hist("Counts", dataset_axis, Dplus_rec_phi_axis),
         'Dsplus_rec_mass': hist.Hist("Counts", dataset_axis, Dsplus_rec_mass_axis),
         'Dsplus_rec_pt': hist.Hist("Counts", dataset_axis, Dsplus_rec_pt_axis),
         'Dsplus_rec_eta': hist.Hist("Counts", dataset_axis, Dsplus_rec_eta_axis),
         'Dsplus_rec_phi': hist.Hist("Counts", dataset_axis, Dsplus_rec_phi_axis),
         'Dstarplus_rec_mass': hist.Hist("Counts", dataset_axis, Dstarplus_rec_mass_axis),
         'Dstarplus_rec_pt': hist.Hist("Counts", dataset_axis, Dstarplus_rec_pt_axis),
         'Dstarplus_rec_eta': hist.Hist("Counts", dataset_axis, Dstarplus_rec_eta_axis),
         'Dstarplus_rec_phi': hist.Hist("Counts", dataset_axis, Dstarplus_rec_phi_axis),
         'Lambdacplus_rec_mass': hist.Hist("Counts", dataset_axis, Lambdacplus_rec_mass_axis),
         'Lambdacplus_rec_pt': hist.Hist("Counts", dataset_axis, Lambdacplus_rec_pt_axis),
         'Lambdacplus_rec_eta': hist.Hist("Counts", dataset_axis, Lambdacplus_rec_eta_axis),
         'Lambdacplus_rec_phi': hist.Hist("Counts", dataset_axis, Lambdacplus_rec_phi_axis),
         'cutflow': processor.defaultdict_accumulator(int),
      })
    
   @property
   def accumulator(self):
      return self._accumulator
    
   def process(self, df):
      output = self.accumulator.identity()
      
      # GenParticles
      dataset = df['dataset']
      if df['nGenPart'].size != 0:
         GenPart = JaggedCandidateArray.candidatesfromcounts(
               df['nGenPart'],
               pt=df['GenPart_pt'],
               eta=df['GenPart_eta'],
               phi=df['GenPart_phi'],
               mass=df['GenPart_mass'],
               charge=df['GenPart_charge'],
               pdgId=df['GenPart_pdgId'],
               vx=df['GenPart_vx'],
               vy=df['GenPart_vy'],
               vz=df['GenPart_vz'],
               mpdgId=df['GenPart_mpdgId'],
               mvx=df['GenPart_mvx'],
               mvy=df['GenPart_mvy'],
               mvz=df['GenPart_mvz'],
               )
      else: 
         GenPart = JaggedCandidateArray.candidatesfromcounts(
               np.array([]),
               pt=np.array([]),
               eta=np.array([]),
               phi=np.array([]),
               mass=np.array([]),
               charge=np.array([]),
               pdgId=np.array([]),
               vx=np.array([]),
               vy=np.array([]),
               vz=np.array([]),
               mpdgId=np.array([]),
               mvx=np.array([]),
               mvy=np.array([]),
               mvz=np.array([]),
               )

      # Particle selection
      protonid = (np.absolute(GenPart.pdgId) == 2212)
      Proton = GenPart[protonid]

      muonid = (np.absolute(GenPart.pdgId) == 13)
      Muon = GenPart[muonid]

      upsilonid = (np.absolute(GenPart.pdgId) == 553)
      Upsilon = GenPart[upsilonid]

      kaonid = (np.absolute(GenPart.pdgId) == 321)
      Kaon = GenPart[kaonid]

      pionid = (np.absolute(GenPart.pdgId) == 211)
      Pion = GenPart[pionid]

      ########################## D0 reconstructed selection ##########################

      #Take non slow pions
      Pion_not_slow = Pion[Pion['__fast_pt'] > 0.3] 
      output['cutflow']['Non Slow Pion'] += Pion_not_slow.counts.sum()
      D0_rec = Kaon.cross(Pion_not_slow)

      opposite_charge_D0 = (D0_rec.i0['charge'] * D0_rec.i1['charge'] < 0)
      D0_rec = D0_rec[opposite_charge_D0]
      output['cutflow']['opposite_charge_D0'] += D0_rec.counts.sum()

      same_vtx_D0 = ((D0_rec.i0['vx'] == D0_rec.i1['vx']) & (D0_rec.i0['vy'] == D0_rec.i1['vy']) & (D0_rec.i0['vz'] == D0_rec.i1['vz']))
      D0_rec = D0_rec[same_vtx_D0]
      output['cutflow']['same_vtx_D0'] += D0_rec.counts.sum()

      mass_cut_D0 = ((D0_rec.mass < 1.89) & (D0_rec.mass > 1.86))
      D0_rec = D0_rec[mass_cut_D0]
      output['cutflow']['mass_cut_D0'] += D0_rec.counts.sum()

      ########################## End of D0 reconstruction ##########################


      d0id = (np.absolute(GenPart.pdgId) == 421)
      D0 = GenPart[d0id]

      ######################## D+ reconstructed selection ########################

      Pion_pion = Pion.distincts()
      same_charge_pion_pion = (Pion_pion.i0['charge'] * Pion_pion.i1['charge'] > 0)
      Pion_pion = Pion_pion[same_charge_pion_pion]
      output['cutflow']['same_charge_pion_pion'] += Pion_pion.counts.sum()

      same_vtx_pion_pion = ((Pion_pion.i0['vx'] == Pion_pion.i1['vx']) & (Pion_pion.i0['vy'] == Pion_pion.i1['vy']) & (Pion_pion.i0['vz'] == Pion_pion.i1['vz']))
      Pion_pion = Pion_pion[same_vtx_pion_pion]
      output['cutflow']['same_vtx_pion_pion'] += Pion_pion.counts.sum()
      
      Dplus_rec = Pion_pion.cross(Kaon)
      opposite_charge_dplus_rec = ( Dplus_rec.i0.i0['charge'] * Dplus_rec.i1['charge'] < 0)
      Dplus_rec = Dplus_rec[opposite_charge_dplus_rec]
      output['cutflow']['opposite_charge_dplus_rec'] += Dplus_rec.counts.sum()

      Dplus_rec_same_vtx = ( (Dplus_rec.i0.i0['vx'] == Dplus_rec.i1['vx']) & (Dplus_rec.i0.i0['vy'] == Dplus_rec.i1['vy']) & (Dplus_rec.i0.i0['vz'] == Dplus_rec.i1['vz']))
      Dplus_rec = Dplus_rec[Dplus_rec_same_vtx]
      output['cutflow']['dplus_rec_same_vtx'] += Dplus_rec.counts.sum()

      Dplus_mass_cut = ((Dplus_rec.mass < 1.872) & (Dplus_rec.mass > 1.866))
      Dplus_rec = Dplus_rec[Dplus_mass_cut]
      output['cutflow']['Dplus_mass_cut'] += Dplus_rec.counts.sum()

      ######################## End of D+ reconstructed selection ########################

      ######################## Ds+ reconstructed selection ########################

      Kaon_kaon = Kaon.distincts()

      opposite_charge_kaon_kaon = (Kaon_kaon.i0['charge'] * Kaon_kaon.i1['charge'] < 0)
      Kaon_kaon = Kaon_kaon[opposite_charge_kaon_kaon]
      output['cutflow']['opposite_charge_kaon_kaon'] += Kaon_kaon.counts.sum()

      same_vtx_kaon_kaon = ((Kaon_kaon.i0['vx'] == Kaon_kaon.i1['vx']) & (Kaon_kaon.i0['vy'] == Kaon_kaon.i1['vy']) & (Kaon_kaon.i0['vz'] == Kaon_kaon.i1['vz']))
      Kaon_kaon = Kaon_kaon[same_vtx_kaon_kaon]
      output['cutflow']['same_vtx_kaon_kaon'] += Kaon_kaon.counts.sum()

      Kaon_kaon = Kaon_kaon[(Kaon_kaon.mass < 1.04)]

      Dsplus_rec = Kaon_kaon.cross(Pion)
      output['cutflow']['dsplus_rec'] += Dsplus_rec.counts.sum()

      Dsplus_rec_same_vtx = ((Dsplus_rec.i0.i0['vx'] == Dsplus_rec.i1['vx']) & (Dsplus_rec.i0.i0['vy'] == Dsplus_rec.i1['vy']) & (Dsplus_rec.i0.i0['vz'] == Dsplus_rec.i1['vz']))
      Dsplus_rec = Dsplus_rec[Dsplus_rec_same_vtx] 
      output['cutflow']['dsplus_rec_same_vtx'] += Dsplus_rec.counts.sum()

      Dsplus_mass_cut = ((Dsplus_rec.mass < 1.990) & (Dsplus_rec.mass > 1.930))
      Dsplus_rec = Dsplus_rec[Dsplus_mass_cut]
      output['cutflow']['Dsplus_mass_cut'] += Dsplus_rec.counts.sum()

      ######################## End of Ds+ reconstructed selection ########################

      ########################  D*+ reconstructed selection ##############################

      # Take slow pions
      Pion_slow = Pion[Pion['__fast_pt'] < 0.3]
      output['cutflow']['Pion Slow'] += Pion_slow.counts.sum()

      Dstarplus_rec = D0_rec.cross(Pion_slow)
      output['cutflow']['Dstarplus_rec bare'] += Dstarplus_rec.counts.sum()

      Dstarplus_rec_same_vtx = ((Dstarplus_rec.i0.i0['vx'] == Dstarplus_rec.i1['vx']) & (Dstarplus_rec.i0.i0['vy'] == Dstarplus_rec.i1['vy']) & (Dstarplus_rec.i0.i0['vz'] == Dstarplus_rec.i1['vz']))
      Dstarplus_rec = Dstarplus_rec[Dstarplus_rec_same_vtx]
      output['cutflow']['Dstarplus_rec_same_vtx'] += Dstarplus_rec.counts.sum()

      Dstarplus_mass_cut = ((Dstarplus_rec.mass < 2.036) & (Dstarplus_rec.mass > 1.970))
      Dstarplus_rec = Dstarplus_rec[Dstarplus_mass_cut]
      output['cutflow']['Dstarplus_mass_cut'] += Dstarplus_rec.counts.sum()

      ######################## End of D*+ reconstructed selection ########################

      ########################  Lambda_c+ reconstructed selection ##############################

      Proton_kaon = Proton.cross(Kaon)
      output['cutflow']['Proton_Kaon'] += Proton_kaon.counts.sum()

      Proton_kaon_opposite_charge = (Proton_kaon.i0['charge'] * Proton_kaon.i1['charge'] < 0)
      Proton_kaon = Proton_kaon[Proton_kaon_opposite_charge]
      output['cutflow']['Proton_kaon_opposite_charge'] += Proton_kaon.counts.sum()

      Proton_kaon_same_vtx = ((Proton_kaon.i0['vx'] == Proton_kaon.i1['vx']) & (Proton_kaon.i0['vy'] == Proton_kaon.i1['vy']) & (Proton_kaon.i0['vz'] == Proton_kaon.i1['vz']))
      Proton_kaon = Proton_kaon[Proton_kaon_same_vtx]     
      output['cutflow']['Proton_kaon_same_vtx'] += Proton_kaon.counts.sum() 

      Lambda_cplus = Proton_kaon.cross(Pion) 
      output['cutflow']['Lambda_cplus'] += Lambda_cplus.counts.sum() 

      Lambda_cplus_same_vtx = ((Lambda_cplus.i0.i0['vx'] == Lambda_cplus.i1['vx']) & (Lambda_cplus.i0.i0['vy'] == Lambda_cplus.i1['vy']) & (Lambda_cplus.i0.i0['vz'] == Lambda_cplus.i1['vz']))
      Lambda_cplus = Lambda_cplus[Lambda_cplus_same_vtx]
      output['cutflow']['Lambda_cplus_same_vtx'] += Lambda_cplus.counts.sum()

      #Lambda_cplus_pt_cut = Lambda_cplus[Lambda_cplus.pt > 0.5]
      #Lambda_cplus = Lambda_cplus[Lambda_cplus_pt_cut]
      #output['cutflow']['Lambda_cplus_pt_cut'] += Lambda_cplus.counts.sum()

      Lambda_cplus_mass_cut = ((Lambda_cplus.mass < 2.1) & (Lambda_cplus.mass > 2.3))
      Lambda_cplus_rec = Lambda_cplus[Lambda_cplus_mass_cut]
      output['cutflow']['Lambda_cplus_mass_cut'] += Lambda_cplus_rec.counts.sum() 
      

      ######## 
      Dimuon = Muon.distincts()
      
      opposite_charge = (Dimuon.i0['charge'] * Dimuon.i1['charge'] < 0)
      Dimuon = Dimuon[opposite_charge]

      same_vtx = ((Dimuon.i0['vx'] == Dimuon.i1['vx']) & (Dimuon.i0['vy'] == Dimuon.i1['vy']) & (Dimuon.i0['vz'] == Dimuon.i1['vz']))
      Dimuon = Dimuon[same_vtx]

      mass_cut = ((Dimuon.mass < 12) & (Dimuon.mass > 7))
      Dimuon = Dimuon[mass_cut]

      leading_mu = (Dimuon.i0.pt.content > Dimuon.i1.pt.content)
      Muon_lead = JaggedCandidateArray.candidatesfromoffsets(Dimuon.offsets, 
                                                       pt=np.where(leading_mu, Dimuon.i0.pt.content, Dimuon.i1.pt.content),
                                                       eta=np.where(leading_mu, Dimuon.i0.eta.content, Dimuon.i1.eta.content),
                                                       phi=np.where(leading_mu, Dimuon.i0.phi.content, Dimuon.i1.phi.content),
                                                       mass=np.where(leading_mu, Dimuon.i0.mass.content, Dimuon.i1.mass.content),
                                                       mpdgId=np.where(leading_mu, Dimuon.i0.mpdgId.content, Dimuon.i1.mpdgId.content))

      Muon_trail = JaggedCandidateArray.candidatesfromoffsets(Dimuon.offsets, 
                                                       pt=np.where(~leading_mu, Dimuon.i0.pt.content, Dimuon.i1.pt.content),
                                                       eta=np.where(~leading_mu, Dimuon.i0.eta.content, Dimuon.i1.eta.content),
                                                       phi=np.where(~leading_mu, Dimuon.i0.phi.content, Dimuon.i1.phi.content),
                                                       mass=np.where(~leading_mu, Dimuon.i0.mass.content, Dimuon.i1.mass.content),
                                                       mpdgId=np.where(leading_mu, Dimuon.i0.mpdgId.content, Dimuon.i1.mpdgId.content))
      
      output['Muon_lead_pt'].fill(dataset=dataset, pt=Muon_lead.pt.flatten())
      output['Muon_trail_pt'].fill(dataset=dataset, pt= Muon_trail.pt.flatten())
      output['Muon_eta'].fill(dataset=dataset, eta=Muon_lead.eta.flatten())
      output['Muon_eta'].fill(dataset=dataset, eta=Muon_trail.eta.flatten())
      output['Muon_phi'].fill(dataset=dataset, phi=Muon_lead.phi.flatten())
      output['Muon_phi'].fill(dataset=dataset, phi=Muon_trail.phi.flatten())

      output['Dimuon_mass'].fill(dataset=dataset, mass=Dimuon.mass.flatten())
      output['Dimuon_pt'].fill(dataset=dataset, pt=Dimuon.pt.flatten())
      output['Dimuon_eta'].fill(dataset=dataset, eta=Dimuon.eta.flatten())
      output['Dimuon_phi'].fill(dataset=dataset, phi=Dimuon.phi.flatten())

      output['D0_mass'].fill(dataset=dataset, mass=D0.mass.flatten())
      output['D0_pt'].fill(dataset=dataset, pt=D0.pt.flatten())
      output['D0_eta'].fill(dataset=dataset, eta=D0.eta.flatten())
      output['D0_phi'].fill(dataset=dataset, phi=D0.phi.flatten())

      output['D0_rec_mass'].fill(dataset=dataset, mass=D0_rec.mass.flatten())
      output['D0_rec_pt'].fill(dataset=dataset, pt=D0_rec.pt.flatten())
      output['D0_rec_eta'].fill(dataset=dataset, eta=D0_rec.eta.flatten())
      output['D0_rec_phi'].fill(dataset=dataset, phi=D0_rec.phi.flatten())

      output['Dplus_rec_mass'].fill(dataset=dataset, mass=Dplus_rec.mass.flatten())
      output['Dplus_rec_pt'].fill(dataset=dataset, pt=Dplus_rec.pt.flatten())
      output['Dplus_rec_eta'].fill(dataset=dataset, eta=Dplus_rec.eta.flatten())
      output['Dplus_rec_phi'].fill(dataset=dataset, phi=Dplus_rec.phi.flatten())

      output['Dsplus_rec_mass'].fill(dataset=dataset, mass=Dsplus_rec.mass.flatten())
      output['Dsplus_rec_pt'].fill(dataset=dataset, pt=Dsplus_rec.pt.flatten())
      output['Dsplus_rec_eta'].fill(dataset=dataset, eta=Dsplus_rec.eta.flatten())
      output['Dsplus_rec_phi'].fill(dataset=dataset, phi=Dsplus_rec.phi.flatten())

      output['Dstarplus_rec_mass'].fill(dataset=dataset, mass=Dstarplus_rec.mass.flatten())
      output['Dstarplus_rec_pt'].fill(dataset=dataset, pt=Dstarplus_rec.pt.flatten())
      output['Dstarplus_rec_eta'].fill(dataset=dataset, eta=Dstarplus_rec.eta.flatten())
      output['Dstarplus_rec_phi'].fill(dataset=dataset, phi=Dstarplus_rec.phi.flatten())

      output['Lambdacplus_rec_mass'].fill(dataset=dataset, mass=Lambda_cplus_rec.mass.flatten())
      output['Lambdacplus_rec_pt'].fill(dataset=dataset, pt=Lambda_cplus_rec.pt.flatten())
      output['Lambdacplus_rec_eta'].fill(dataset=dataset, eta=Lambda_cplus_rec.eta.flatten())
      output['Lambdacplus_rec_phi'].fill(dataset=dataset, phi=Lambda_cplus_rec.phi.flatten())
      
      return output

   def postprocess(self, accumulator):
      return accumulator