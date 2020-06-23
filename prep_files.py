#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 00:16:05 2020

@author: vishalr
"""


from Bio import SeqIO

patient_0 = 'Wuhan_Hu_1.fasta' #refernce sequence file
region = 'covseq0414.fasta' #file with sequences of all the cases to be analyzed in FASTA format
file_dir = '/sequence_files/' #directory for storing the prepared files which will be input to alignment software
seq_list = []   #list of all the patient cases

for first_record in SeqIO.parse(open(patient_0, mode='r'), 'fasta'):
    first_record.description=' '.join(first_record.description.split()[1:])       
    print('SequenceID = '  + first_record.id)
    #print('Description = ' + first_record.description + '\n')
    for seq_record in SeqIO.parse(open(region, mode='r'), 'fasta'):
        try:
            seq_record.description=' '.join(seq_record.description.split()[1:])    
            #print('SequenceID = '  + seq_record.id)
            #print('Description = ' + seq_record.description + '\n')
            a = seq_record.id
            a = (a.split('|'))[1]
            seq_list.append(a)
            # write new fasta file for each case with two seqences, the refernce and the sequence to be aligned
            with open(file_dir+a+'.fasta', 'w') as f_out:
                r=SeqIO.write(seq_record, f_out, 'fasta')
                if r!=1: print('Error while writing sequence:  ' + seq_record.id)
                r=SeqIO.write(first_record, f_out, 'fasta')
                if r!=1: print('Error while writing sequence:  ' + first_record.id)
        except:
            print('skipped' + seq_record.id)
                
#print(len(list_files))
            
new_list = 'list_files.txt' #record all cases
with open(new_list,'w') as f:
    for i in seq_list:
        f.write('%s\n'%i)