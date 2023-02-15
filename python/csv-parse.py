#!/usr/bin/env python3
"""Parse a comma-separated value (CSV) files."""

import csv

with open('csv-parse.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print("Name: {name} Value: {value} Note: {note}".format(**row))
