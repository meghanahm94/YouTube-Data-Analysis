#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 15:29:14 2019

@author: sivarams
"""

import os
import glob
import pandas as pd

os.chdir("/Users/sivarams/Downloads/Trending-YouTube-Scraper-master/output")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])

#export to csv
combined_csv.to_csv("mv_combined_csv.csv", index=False, encoding='utf-8-sig')