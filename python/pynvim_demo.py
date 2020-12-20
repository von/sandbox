#!/usr/bin/env python3
"""Demo pynvim from https://github.com/neovim/pynvim"""
import sys

from pynvim import attach

# Create a python API session attached
try:
    nvim = attach('socket', path='/tmp/nvim')
except FileNotFoundError:
    print("Could not connect to nvim.")
    sys.exit(1)

# Find or Create the demo buffer
demobufnum = nvim.eval('bufadd("pynvim_demo_buffer")')
print(f"Demo buffer is buffer #{demobufnum}")

print("Buffers:")
for buffer in nvim.buffers:
    if buffer.valid:
        print(f"{buffer.number}:{buffer.name}")
    if buffer.number == demobufnum:
        demobuf = buffer

print("Windows:")
for window in nvim.windows:
    print(f"  Buffer name: {window.buffer.name}"
          f" ({window.width}x{window.height})")

# Switch to demo buffer and do some work
nvim.command(f'buffer {demobufnum}')
count = int(demobuf[0])+1 if demobuf[0].isnumeric() else 1
# Count of number of times we've run in line 1
demobuf[0] = str(count)
# And append a new line...
demobuf.append('Hello world! This is the demo buffer!')

# nvim.command('split')
# nvim.windows[1].height = 10

nvim.vars['global_var'] = [1, 2, 3]
vars = nvim.eval('g:global_var')
print(vars)
sys.exit(0)
