'''
this should contain all code neccesary to take a cif file, make a unit cell, create a supercell, 
generate radial function features for atoms in the cental unit cell of supercell, and then create a graph 
of the central unit cell with long range interactions captured by the radial functions.
Doped materials would be presented with a probabilistic node that would represent the dopand as present only 
'''

import torch 
from torch_geometric.data import Data
from ase.io import read, write

unit_cell = read('./train_cif_data/undoped_test.cif')


def make_super_cell(u_cell, matrix):
    '''
    u_cell : ase.atom.Atoms (need to load the unit cell from a cif file using ase)
    matrix : (x, y, z) matrix that will multiply the unit cell
    '''
    super_cell = u_cell*matrix
    return super_cell

#def get_ACSF(u_cell, )