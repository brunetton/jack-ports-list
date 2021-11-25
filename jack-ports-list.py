#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Usage:
    {self_filename} [options]
    {self_filename} -h | --help

Options:
    --audio     only list audio ports
    --midi      only list midi
    --inputs    only list inputs
    --outputs   only list outputs
    -n          make output grepeable (remove all output made for humans)
"""

from pathlib import Path

import docopt
import itertoolz
import jack
from docopt import docopt


# Parse args
args = docopt(__doc__.format(self_filename=Path(__file__).name))

# Main loop
client = jack.Client('')
ports_list = client.get_ports()

# Filter
# TODO: use get_ports() function
filter_str = None  # Used for display
if args["--audio"]:
    ports_list = filter(lambda p: p.is_audio, ports_list)
    filter_str = "AUDIO"
if args["--midi"]:
    ports_list = filter(lambda p: p.is_midi, ports_list)
    filter_str = "MIDI"
if args["--inputs"]:
    ports_list = filter(lambda p: p.is_input, ports_list)
if args["--outputs"]:
    ports_list = filter(lambda p: p.is_output, ports_list)

# Display
groups = itertoolz.groupby(lambda e: e.is_input, ports_list)
for is_input in [True, False]:
    # Iter inputs then outputs
    # current_group in (groups[True], groups[False]):
    current_group = groups[is_input]
    if not args['-n']:
        print("** " + ('{} '.format(filter_str) if filter_str else '') + ("INPUTS" if is_input else "OUTPUTS"))
    for port in current_group:
        print(port.name)
    if len(current_group) > 1 and not args['-n']:
        print()

client.close()
