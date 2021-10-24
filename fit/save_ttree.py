from coffea.util import load
import numpy as np

import uproot3
import argparse

### Description
# This code is used to produce ttrees (root files) from a coffea data in order to use it on roofit to do the fitting.
# Depending on the parser one call create the root files for:
# jpsi: mass and decay length ntuples.
# psi: mass and decay length ntuples.
# dstar: delta mass ntuple
# dzero: mass ntuple


### File section

# Usual file
file = '../output/Charmonium2018B_test/Charmonium2018B_test.coffea'
# Output name
out_name = 'charmonium_2018B.root'
# Load the file
acc = load(file)


## Argparse section
parser = argparse.ArgumentParser(description="Creates a root file to be an input to roofit")
parser.add_argument("-j", "--jpsi", help="Root file for jpsi mass and decay length", action="store_true")
parser.add_argument("-p", "--psi", help="Root file for psi mass and decay length", action="store_true")
parser.add_argument("-ds", "--dstar", help="Root file for dstar delta mass", action="store_true")
parser.add_argument("-dz", "--dzero", help="Root file for dzero mass and decay length", action="store_true")
args = parser.parse_args()


## Jpsi mass and decay length

# Mass
jpsi_mass = acc['Dimu']['mass'].value[acc['Dimu']['is_jpsi'].value]
# Decay length
dl_jpsi = acc['Dimu']['dl'].value[acc['Dimu']['is_jpsi'].value]

## Psi mass and decay length

# Mass
psi_mass = acc['Dimu']['mass'].value[acc['Dimu']['is_psi'].value]
# Decay length
dl_psi = acc['Dimu']['dl'].value[acc['Dimu']['is_jpsi'].value]

# Dstar    
all_data_dstar = acc['Dstar']['deltamr'].value[~acc['Dstar']['wrg_chg'].value]
cut = all_data_dstar[(all_data_dstar >= 0.14) & (all_data_dstar <= 0.16)]

dstar_mass = cut[:]

# Dzero    
all_data_dzero = acc['D0']['mass21'].value
cut = all_data_dzero[(all_data_dzero > 1.75) & (all_data_dzero < 1.96)]

dzero_mass = cut[:]

## File generation section

if args.jpsi:
     print("Creating file for jpsi")
     with uproot3.recreate('jpsi' + '_' + out_name) as f:
          f['Jpsi'] = uproot3.newtree({"mass": "float32", "jpsi_dl" : "float32"})
          f['Jpsi'].extend({"mass": jpsi_mass, "jpsi_dl": dl_jpsi})