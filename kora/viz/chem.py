import os
os.system('pip install py3Dmol')
import kora.install.rdkit

from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol
from IPython.core.magic import register_line_magic


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


@register_line_magic
def ch(line):
  plot(line.strip(), size=(500,300))
