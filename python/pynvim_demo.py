#!/usr/bin/env python3
"""Demo pynvim from https://github.com/neovim/pynvim"""
import sys

from pynvim import attach

# Create a python API session attached to nvim started as follows:
#   NVIM_LISTEN_ADDRESS=/tmp/nvim nvim
try:
    nvim = attach('socket', path='/tmp/nvim')
except FileNotFoundError:
    print("Could not connect to nvim.")
    sys.exit(1)

# Now do some work.
buffer = nvim.current.buffer  # Get the current buffer
buffer[0] = 'replace first line'
buffer[:] = ['replace whole buffer']

nvim.command('split')

nvim.windows[1].height = 10

nvim.vars['global_var'] = [1, 2, 3]
vars = nvim.eval('g:global_var')
print(vars)
sys.exit(0)
