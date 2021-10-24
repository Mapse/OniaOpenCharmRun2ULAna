# coding: utf-8

import time
import os
from tqdm import tqdm

from coffea.util import save
from nanoAODplus_processor.MonteCarloHistogramingProcessor import MonteCarloHistogramingProcessor
from nanoAODplus_processor.HistogramingProcessor import HistogramingProcessor

def plotter(name, analysis_type):
    print("Starting plots creation")

    print("Saving histograms in output/" + name )

    tstart = time.time()
    if (analysis_type == 'mc'):
        p = MonteCarloHistogramingProcessor(name)

    elif (analysis_type == 'data'):
        p = HistogramingProcessor(name)
        
    files = ["output/" + name + "/" + name +".coffea"]
    out = p.accumulator.identity()
    for f in tqdm(files, desc="Processing", unit=" files", total=len(files)):
        out += p.process(f)

    save(out, "output/" + name + "/" + name + "_hists.coffea")

    elapsed = round(time.time() - tstart, 2)

    print(f"Finished in: {elapsed} s")