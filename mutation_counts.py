#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 11:59:06 2020

@author: vishalr
"""

from Bio import AlignIO
import numpy as np

muscle_exe = r"/home/vishalr/Downloads/covid19/muscle3.8.31_i86linux64" #specify the location of your muscle exe file

list_files = 'list_files.txt' ##record of all cases
seq_list = []

with open(list_files,'r') as f:
    for line in f:
        line = line[:-1]
        seq_list.append(line)

mut_count = np.zeros((len(seq_list),29903)) #total count of mutations at each position in the genome       
for seq in range(len(seq_list)):
    output_alignment = "/aligned_files/aln_"+seq_list[seq]+".fasta"
    MultipleSeqAlignment = AlignIO.read(output_alignment, "fasta") 
    align_array = np.array([list(rec) for rec in MultipleSeqAlignment], np.character)
    itr = 0
    count = np.zeros(29903)
    for i in range(len(align_array[1])):
        if(align_array[1,i] == b'-'): 
            continue
        else:
            if(align_array[0,i] != b'N'):
                if(align_array[0,i] != align_array[1,i]):
                    count[itr] = count[itr] + 1
            itr = itr+1
    for i in range(len(count)):
        mut_count[seq][i]=count[i]
    print(seq_list[seq])
np.save('mut_counts.npy',mut_count) 

#sum mut_counts.npy over all cases to obtain an aggregate profile which can be used for estimation.
# If there are long gaps (>10bp) in the alignment, they should be removed as an extra step before aggregation.
