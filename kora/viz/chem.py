import os
os.system('pip install py3Dmol')
import kora.install.rdkit

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol


def plot(smiles, size=(200,200), style='stick'):
    """ 
    Visualize a molecule from its formula (smiles)
    Adapted from https://birdlet.github.io/2019/10/02/py3dmol_example 
    """
    mol = Chem.MolFromSmiles(smiles)
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol)
    AllChem.MMFFOptimizeMolecule(mol)
    block = Chem.MolToMolBlock(mol)

    viewer = py3Dmol.view(width=size[0], height=size[1])
    viewer.addModel(block, 'mol')
    viewer.setStyle({style:{}})
    viewer.zoomTo()
    viewer.show()
