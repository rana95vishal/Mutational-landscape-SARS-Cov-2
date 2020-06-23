# Mutational-landscape-SARS-Cov-2
Estimating the Mutational Support and Distribution of SARS-Cov-2 in the Small Sample Regime.

1. The sequncing data used in the project can be downloaded from https://www.gisaid.org/ . The portal allows you to select cases and dowload the associated data in FASTA format. 

2. Sequence alignment has been performed using MUSCLE. The binary/executable file for the same can be downloaded from https://www.drive5.com/muscle/.

3. The combined FASTA file for all patients needs to be split and and formatted to include the refernce sequence (Wuhan-1 or regional Patient 1). Script prep_files.py can be used to prepare the files for alignment. 

4. alignment.py performs the alignment for each case and mutation_counts.py returns mutation profiles for all the cases which is combined to form an aggregate mutation profile. This aggregate mutation profile is used in Distribution estimation and Support estimation. 

5. Distribution estimation using Good-Turing estimator can be performed as described here: http://crr.ugent.be/papers/A%20Python%20program%20to%20calculate%20the%20Good-Turing%20algorithm.pdf

6. For Support estimation refer to the impementation at https://github.com/elichienxD/Support-estimation

7. GenomeDiagram plots showing the distibution of mutations along the SARS-Cov-2 genome given in manuscript can be genrated using genomeD.py

8. Patient 1 or reference sequence for different regions and the metadata associated with all the cases analyzed for the project can be found in the data folder.
