# coding: utf-8

import time
import os
from tqdm import tqdm

from coffea.util import save
from nanoAODplus_processor.HistogramingProcessor import HistogramingProcessor

def plotter(name, analysis_type):
    print("Starting plots creation")

    print("Saving histograms in output/" + name )

    tstart = time.time()

    p = HistogramingProcessor(name, analysis_type)
    files = ["output/" + name + "/" + name +".coffea"]
    out = p.accumulator.identity()
    for f in tqdm(files, desc="Processing", unit=" files", total=len(files)):
        out += p.process(f, analysis_type)

    save(out, "output/" + name + "/" + name + "_hists.coffea")

    elapsed = round(time.time() - tstart, 2)

    print(f"Finished in: {elapsed} s")