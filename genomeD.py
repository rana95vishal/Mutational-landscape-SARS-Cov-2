#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 01:18:33 2020

@author: vishalr
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 10:43:46 2020

@author: rana9
"""


from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio.SeqFeature import SeqFeature, FeatureLocation
import numpy as np


#genome diagrams for distibution of mutations in SARS-Cov-2 genome using results for Good-Turing estimator
#the file *_result.npy contains the probability values in decreasing order
#the file *_GenePos.npy contains the postion along the genome for each of those probability values in *_result.npy.
path_r = 'Asia_result.npy'
path_g = 'Asia_GenePos.npy'
x1 = np.load(path_r,allow_pickle=True)
y1 = np.load(path_g,allow_pickle=True)
path_r = 'Europe_result.npy'
path_g = 'Europe_GenePos.npy'
x2 = np.load(path_r,allow_pickle=True)
y2 = np.load(path_g,allow_pickle=True)
path_r = 'NA_result.npy'
path_g = 'NA_GenePos.npy'
x3 = np.load(path_r,allow_pickle=True)
y3 = np.load(path_g,allow_pickle=True)

data_val = np.zeros(29903)
for i in ([0,1,9]):
    for j in range(len(y1[i])):
        data_val[y1[i][j]] = (x1[i][j])
data1 = [(i,data_val[i]) for i in range(29903)]

data_val = np.zeros(29903)
for i in ([0,1,9]):
    for j in range(len(y2[i])):
        data_val[y2[i][j]] = (x2[i][j])   
data2 = [(i,data_val[i]) for i in range(29903)]

data_val = np.zeros(29903)
for i in ([0,1,9]):
    for j in range(len(y3[i])):
        data_val[y3[i][j]] = (x3[i][j])
data3 = [(i,data_val[i]) for i in range(29903)]

Start = [266, 13469, 21563, 25393, 26245, 26523, 27202, 27394, 27894, 28274, 29558]
End = [13468, 21555, 25384, 26220, 26472, 27191, 27387, 27759, 28259, 29533, 29674]
colo = [colors.red,colors.pink,'','','','','','','',colors.red,'']
names = ["ORF1a","ORF1b","S","ORF3a","E","M","ORF6","ORF7a","ORF8","N","ORF10"]
gdd = GenomeDiagram.Diagram("Test Diagram")

gdt_data1 = gdd.new_track(1, greytrack=1,greytrack_labels = 1,
                         scale=0,scale_ticks=1,scale_largetick_interval=10000,scale_largetick_labels = 1,
                         scale_largeticks = 1,name = "Asia",axis_labels = 0)
gds_data1 = gdt_data1.new_set("graph")

gdt_data2 = gdd.new_track(1, greytrack=1,greytrack_labels = 1,
                         scale=0,scale_ticks=1,scale_largetick_interval=10000,scale_largetick_labels = 1,
                         scale_largeticks = 1,name = "Europe",axis_labels = 0)
gds_data2 = gdt_data2.new_set("graph")

gdt_data3 = gdd.new_track(1, greytrack=1,greytrack_labels = 1,
                         scale=0,scale_ticks=1,scale_largetick_interval=10000,scale_largetick_labels = 1,
                         scale_largeticks = 1,name = "North America",axis_labels = 0)
gds_data3 = gdt_data3.new_set("graph")

gdt_features = gdd.new_track(1, greytrack=1,scale=1,scale_ticks=0,name = "Genes",greytrack_labels = 1)
gds_features = gdt_features.new_set()


for i in ([0,1,9]):
    feature = SeqFeature(FeatureLocation(Start[i], End[i]), strand=+1)
    gds_features.add_feature(feature,
            color=colo[i],
            name = names[i],
            label=True,
            label_size=10,
            label_color=colors.black,
            label_angle = 0,
            sigil = "BOX",
            arrowshaft_height=0.05)


gds_data1.new_graph(data1,center = 0.0,colour = colors.blue)
gds_data2.new_graph(data2,center = 0.0,colour = colors.red)
gds_data3.new_graph(data3,center = 0.0,colour = colors.black)
gdd.draw(format="linear", pagesize=(25 * cm, 10 * cm), fragments=1, start=0, end=29903)
gdd.write("region_new.png", "PNG")