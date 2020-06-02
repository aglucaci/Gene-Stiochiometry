#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 16:13:14 2020

@author: Alexander G Lucaci

# Reference
https://opentextbc.ca/biology/chapter/9-1-the-structure-of-dna/
"""


class GeneStoichiometry():
    
    #Definitions
    Adenine = {"C": 5, "N": 5, "O": 0, "H": 5}
    Thymine = {"C": 5, "N": 2, "O": 2, "H": 6}
    Cytosine = {"C": 4, "N": 2, "O": 1, "H": 6}
    Guanine = {"C": 4, "N": 6, "O": 1, "H": 5}
    
    def __init__(self):
        #current_gene = gene
        #print("init Processing:", gene)
        #C, H, O, N = self.sum_nucleotides_elements(gene)
        #print("C:",C, H, O, N)
        pass
        
    def sum_nucleotides_elements(self, gene):
        # Adenine, Thymine, Cytosine, Guanine
        C, H, O, N = 0, 0, 0, 0
        
        for char in gene.upper():
            if char == "T":
                C += self.Thymine["C"]
                H += self.Thymine["H"]
                O += self.Thymine["O"]
                N += self.Thymine["N"]
            elif char == "C":
                C += self.Cytosine["C"]
                H += self.Cytosine["H"]
                O += self.Cytosine["O"]
                N += self.Cytosine["N"]
            elif char == "G":
                C += self.Guanine["C"]
                H += self.Guanine["H"]
                O += self.Guanine["O"]
                N += self.Guanine["N"]
            elif char == "A":
                C += self.Adenine["C"]
                H += self.Adenine["H"]
                O += self.Adenine["O"]
                N += self.Adenine["N"]
            else:
                pass
                #character unknown.
            #end if
        #end for
        return C, H, O, N
    #end method
            
    
    def return_values(self):
        pass
    
    def reduce_equation(self):
        pass

#end class



# Load the Fasta, Driver code
x =  GeneStoichiometry()
C, H, O, N = x.sum_nucleotides_elements("AAAGGGCCCTTT")

print("C:", C, H, O, N)