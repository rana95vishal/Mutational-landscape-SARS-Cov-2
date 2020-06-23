#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:41:33 2020

@author: vishalr
"""

from Bio.Align.Applications import MuscleCommandline

muscle_exe = r"/home/vishalr/Downloads/covid19/muscle3.8.31_i86linux64" #specify the location of your muscle exe file

list_files = 'list_files.txt' ##record of all cases
seq_list = []

with open(list_files,'r') as f:
    for line in f:
        line = line[:-1]
        seq_list.append(line)
  
#alignment using muscle      
itr = 0
for seq in seq_list:
    itr = itr + 1
    try:
        input_sequences = "/sequence_files/"+seq+".fasta"
        output_alignment = "/aligned_files/aln_"+seq+".fasta"
        muscle_cline = MuscleCommandline(muscle_exe, input=input_sequences, out=output_alignment)
        stdout, stderr = muscle_cline()
        print(seq,itr)
    except:
        print("skipped",seq,itr)

