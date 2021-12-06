    # coding: utf-8

import time
import os

import coffea.processor as processor
from coffea.nanoevents import BaseSchema

from nanoAODplus_processor.EventSelectorProcessor import EventSelectorProcessor
from nanoAODplus_processor.MonteCarloEventSelectorProcessor import MonteCarloEventSelectorProcessor
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
parser.add_argument("-d", "--data", help="Run for data", action="store_true")
parser.add_argument("-c", "--mc", help="Run for monte carlo", action="store_true")
args = parser.parse_args()


# If the process is for data or mc
if (args.data):
    analysis_type = 'data'
    processor_instance = EventSelectorProcessor(args.name)
if (args.mc):
    analysis_type = 'mc'     
    processor_instance = MonteCarloEventSelectorProcessor(args.name)

if (args.select or args.analyze):
    config_yaml = yaml.load(open("config/multicore.yaml", "r"), Loader=yaml.FullLoader)

    tstart = time.time()
    
    #files = {'Charmonium2017AOD': filesets['Charmonium2017AOD'][:]}
    #files = {'Charmonium_new2017AOD': filesets['Charmonium_new2017AOD'][0:1]}

    #files = {'Charmonium2017AOD': filesets['Charmonium2017AOD'][:]}
    #files = {'Charmonium2018AOD': filesets['Charmonium2018AOD'][:]}
    files = {'MonteCarlo2017AOD': filesets['MonteCarlo2017AOD'][:]}
    #files = {'MonteCarlo2018AOD': filesets['MonteCarlo2018AOD'][:]}

    # creating necessary folders into dir output data
    os.system("mkdir -p output/" + args.name)
    os.system("rm -rf output/" + args.name + "/*")
         
    if config_yaml['executor'] == 'futures_executor': 
        
        output = processor.run_uproot_job(files,
                                        treename='Events',
                                        processor_instance=processor_instance,
                                        executor=processor.futures_executor, # Uses python futures to multiprocessing
                                        executor_args={"schema": BaseSchema, 'workers': config_yaml['n_cores']}, # BaseSchema returns a base.nano-events object
                                        chunksize=config_yaml['chunksize'],
                                        )
       

    elif config_yaml['executor'] == 'iterative_executor':
        output = processor.run_uproot_job(files,
                                        treename='Events',
                                        processor_instance=processor_instance,
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
    plotter(args.name, analysis_type)    