# coding: utf-8

import time
import os

import coffea.processor as processor
from coffea.nanoevents import BaseSchema

from nanoAODplus_processor.EventSelectorProcessor import EventSelectorProcessor
from data.fileset import filesets
import yaml

# for argument parsing
import argparse
parser = argparse.ArgumentParser(description="Onia Open Charm NanoAOD analyzer")
parser.add_argument("-n", "--name", help="Analyzer name", type=str, required=True)
parser.add_argument("-s", "--select", help="Do the evt selection", action="store_true")
parser.add_argument("-m","--merge", help="Merge the accumulators that were output from a analyzer", action="store_true")
parser.add_argument("-p","--plots", help="Create the plots from the merged accumulator", action="store_true")
parser.add_argument("-a","--analyze", help="Do the full analysis chain", action="store_true")
args = parser.parse_args()

if (args.select or args.analyze):
    config_yaml = yaml.load(open("config/multicore.yaml", "r"), Loader=yaml.FullLoader)

    tstart = time.time()


    files = {'Charmonium2017_2018AOD': filesets['Charmonium2017_2018AOD'][:]}
    #files = {'Charmonium2018AOD': filesets['Charmonium2018AOD'][1:100]}

    # creating necessary folders into dir output data
    os.system("mkdir -p output/" + args.name)
    os.system("rm -rf output/" + args.name + "/*")          

    if config_yaml['executor'] == 'futures_executor': 
        output = processor.run_uproot_job(files,
                                        treename='Events',
                                        processor_instance=EventSelectorProcessor(args.name),
                                        executor=processor.futures_executor, # Uses python futures to multiprocessing
                                        executor_args={"schema": BaseSchema, 'workers': config_yaml['n_cores']}, # BaseSchema returns a base.nano-events object
                                        chunksize=config_yaml['chunksize'],
                                        )

    elif config_yaml['executor'] == 'iterative_executor':
        output = processor.run_uproot_job(files,
                                        treename='Events',
                                        processor_instance=EventSelectorProcessor(args.name),
                                        executor=processor.iterative_executor,
                                        executor_args={'schema': BaseSchema},
                                        chunksize=config_yaml['chunksize'],
                                        )

    elapsed = round(time.time() - tstart, 2)
    print(f"Process finished in: {elapsed} s")

if (args.merge or args.analyze):
    from tools.merger import merger
    merger(args.name)

if (args.plots or args.analyze):
    from tools.plotter import plotter
    plotter(args.name)    
