# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:15:24 2020

@author: Abdelrahman Al-Wali
"""

import os.path as osp
from easydict import EasyDict as edict

C = edict()
config = C
cfg = C

"""Data Config"""
C.data_dir = r"C:\Users\Abdelrahman Al-Wali\Desktop\BigDataProject"
C.data_name = "ticdata2000.txt"
C.data_path = osp.join(C.data_dir, C.data_name)
C.start_column = 24 - 1
C.last_column = C.start_column + 12
C.csv_file = "data_out.csv"

"""Sorting of rules"""
C.Sorting_of_rules = True #if True sorting by Lift,
                          # if False sorting by Leverage


"""HTML style for rules"""
C.css = """
<style type=\"text/css\">
table {
color: #333;
font-family: Helvetica, Arial, sans-serif;
width: 1000px;
border-collapse:
collapse; 
border-spacing: 0;
}

td, th {
border: 1px solid transparent; /* No more visible border */
height: 30px;
}

th {
background: #DFDFDF; /* Darken header a bit */
font-weight: bold;
text-align: left;
}

td {
background: #FAFAFA;
text-align: left;
}

table tr:nth-child(odd) td{
background-color: white;
}
</style>
"""
